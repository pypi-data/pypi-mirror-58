# ContentData

by Hunter Kempf

Get Content Data from Wikipedia and IMDb

Get Data from Wikipedia Example:
```python
from ContentData.WikiScrape import Company

url = 'https://en.wikipedia.org/wiki/List_of_original_programs_distributed_by_Netflix'
table_names = ["Drama",
               "Marvel series",
               "Comedy",
               "Animation",
               "Anime",
               "Children's programming - Animation",
               "Children's programming - Musical shorts",
               "Children's programming - Live action"]
table_indexes = range(0,len(table_names))

NFLX = Company("Netflix",url,table_names,table_indexes)
NFLX.get_dataframe()
```

Get Data from IMDb Example:
```python
from ContentData.IMDbScrape import imdb_data

IMDb = imdb_data()
IMDb.get_list_mixed_data(["House of Cards","Hemlock Grove"])
```

The WikiScrape section only handles tabular data similar to the netflix example. This can be further expanded to include List like data similar to the HBO wikipedia article.  