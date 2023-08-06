import pandas as pd
import imdb
class imdb_data:
    def __init__(self):
        self.df = pd.DataFrame()

    def get_series(self,movieID):
        """
        Takes in IMDB movieID and returns a dataframe of the episodes in the series and information about them
        """
        ia = imdb.IMDb()
        series = ia.get_movie(movieID)
        ia.update(series, 'episodes')
        print("Getting Information for:",series,"episodes")
        output_df = pd.DataFrame(columns=['kind','series_name','season','episode','original_air_date','rating','votes'])
        for season in sorted(series['episodes'].keys()):
            current_season = series['episodes'][season]
            for episode in sorted(current_season.keys()):
                current_episode = current_season[episode]
                row = pd.DataFrame([['tv series',series.data.get('title'),season,episode,current_episode.data.get('original air date'),round(current_episode.data.get('rating'),1),current_episode.data.get('votes')]],
                               columns=['kind','series_name','season','episode','original_air_date','rating','votes'])
                output_df = output_df.append(row)
        return output_df.reset_index(drop = True)
    
    def get_individual(self,movieID):
        """
        Takes in IMDB movieID and returns a dataframe of the relevant information
        """
        ia = imdb.IMDb()
        movie = ia.get_movie(movieID)
        if movie.data.get('kind') == 'tv series':
            count = 0
            ia.update(movie, 'episodes')
            for season in movie['episodes'].keys():
                for episode in movie['episodes'][season].keys():
                    count = count + 1
        else:
            count = 1
        data = movie.data
        return pd.DataFrame([[data.get('kind'),data.get('title'),'','',count,data.get('series years'),round(data.get('rating'),1),data.get('votes')]],
                    columns=['kind','series_name','season','episode','original_air_date','rating','votes'])

    
    def get_individual_with_budget(self,movie_name):
        """
        Takes in IMDB movieID and returns a dataframe of the relevant information
        """
        ia = imdb.IMDb()
        movieID = ia.search_movie(movie_name)[0].movieID
        movie = ia.get_movie(movieID)
        if movie.data.get('kind') == 'tv series':
            count = 0
            ia.update(movie, 'episodes')
            for season in movie['episodes'].keys():
                for episode in movie['episodes'][season].keys():
                    count = count + 1
        else:
            count = 1
        data = movie.data
        return pd.DataFrame([[data.get('kind'),data.get('title'),data.get('box office').get('Budget'),count,data.get('series years'),round(data.get('rating'),1),data.get('votes')]],
                    columns=['kind','series_name','budget','episode_count','original_air_date_year','rating','votes'])
    def get_tv_show_information(self,name,unravel = False):
        """
        Takes in the name of a movie or series and returns a row of information for movies or a dataframe for a series.
        Uses imdbpy library
        """
        ia = imdb.IMDb()
        content_search = ia.search_movie(name)
        content_type = content_search[0].data.get('kind')
        if (content_type == 'tv series') & unravel:
            return self.get_series(content_search[0].movieID)
        else:
            return self.get_individual(content_search[0].movieID)
    def get_list_tv_shows_data(self, content_list,unravel = False):
        """
        Takes in a list of tv show names and returns a dataframe with the relevant IMDB information. 
        If unravel is true then it will get episode level data from IMDB
        """
        output_df = pd.DataFrame(columns=['kind','series_name','season','episode','original_air_date','rating','votes'])
        for show_name in content_list:
            row = self.get_tv_show_information(show_name,unravel)
            output_df = output_df.append(row)
        return output_df.reset_index(drop = True)

    def get_list_mixed_data(self, content_list):
        """
        Takes in a list of tv shows and movies and returns a dataframe with the relevant IMDB information.
        """
        output_df = pd.DataFrame(columns=['kind','series_name','budget','episode_count','original_air_date_year','rating','votes'])
        for show_name in content_list:
            row = self.get_individual_with_budget(show_name)
            output_df = output_df.append(row)
        return output_df.reset_index(drop = True)
