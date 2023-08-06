import pandas as pd
import requests

class Company:
    """ 
    A company is an object that holds the original content that a media company makes. 
    Examples of a Company are Netflix or HBO
    """
    def __init__(self,name,wiki_url,wiki_type,table_names = [],table_indexes = []):
        self.name = name
        self.wiki_url = wiki_url
        self.wiki_type = wiki_type
        self.table_names = table_names
        self.table_indexes = table_indexes
        if(self.wiki_type =="table"):
            self.set_table_genres()
            self.set_dataframe()
        else:
            print("Table based wikis are the only type implemented so far")
        
    def set_table_genres(self):
        re = requests.get(self.wiki_url, headers =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}).text
        df_list = pd.read_html(re)
        i = 0
        table_list = []
        for name in self.table_names:
            print(name)
            table_list.append(GenreTable(name,df_list[self.table_indexes[i]]))
            i = i + 1
        self.genres = table_list
    
    def get_genres(self):
        return self.genres
    
    def set_dataframe(self):
        df_list = []
        for genre in self.genres:
            df_list.append(genre.get_data())
        self.dataframe = pd.concat(df_list,ignore_index = True)
        
    def get_dataframe(self):
        return self.dataframe

class GenreTable:
    """
    A genre is an object that holds the content of a specific genre that a media company makes.
    Examples of a genre are Drama or Comedy
    """
    def __init__(self,name,dataframe,verbose = True):
        self.name = name
        self.set_data(dataframe)
        self.verbose = verbose
        if(verbose):
            print("Successfully made",self.name,"Genre object")
            
    def get_data(self):
        return self.data
        
    def set_data(self, dataframe):
        Title = self.get_column(dataframe,"Title")
        if ("-" in self.name):
            # table name is main genre
            Genre = pd.Series(index=range(0,dataframe.shape[0]),name = "Genre")
            Genre = Genre.fillna(self.name.split(" - ")[0])
            # genre column of table is subgenre
            SubGenre = pd.Series(index=range(0,dataframe.shape[0]),name = "SubGenre")
            SubGenre = SubGenre.fillna(self.name.split(" - ")[1])
        else:
            # table name is main genre
            Genre = pd.Series(index=range(0,dataframe.shape[0]),name = "Genre")
            Genre = Genre.fillna(self.name)
            # genre column of table is subgenre
            SubGenre = self.get_column(dataframe,"Genre")
        Premiere = self.get_column(dataframe,"Premiere")
        Seasons = self.get_column(dataframe,"Seasons")
        Length = self.get_column(dataframe,"Length")
        Status = self.get_column(dataframe,"Status")
        
        frame = {'Title': Title,
                 'Genre' : Genre,
                 'SubGenre': SubGenre, 
                 'Premiere': Premiere, 
                 'Seasons': Seasons, 
                 'Length': Length,
                 'Status': Status} 
        result = pd.DataFrame(frame) 
        result.drop(result.index[result.Title == "Upcoming"], inplace = True)
        self.data = result
        
    def get_column(self,dataframe,colname):
        if(colname in dataframe.columns.values):
            column = dataframe.loc[:, colname]
        else:
            column = pd.Series(index=range(0,dataframe.shape[0]),name=colname)
        return column
        
