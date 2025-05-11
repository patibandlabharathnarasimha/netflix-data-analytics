import pandas as pd
import plotly.express as px
import preswald
from preswald import connect, get_df,query,table,plotly,text

connect()  
df = get_df('data/netflix_titles.csv')

sql = "SELECT type,count(*) as count FROM data/netflix_titles.csv group by type"
tv_movies_df = query(sql, "data/netflix_titles.csv")
tv_movies_fig = px.pie(tv_movies_df, values='count', names='type')

text("TV Shows vs Movies on Netflix")
plotly(tv_movies_fig)
table(tv_movies_df)

sql_common_genre = "select listed_in as genre,count(*) as count from  data/netflix_titles.csv group by listed_in order by count desc limit 10"
most_common_genre_df = query(sql_common_genre, "data/netflix_titles.csv")
most_common_genre_fig = px.bar(most_common_genre_df.sort_values('count'), x='count', y='genre', orientation='h',text='count',title='Top 10 Most Common Genre on Netflix',labels={'count':'Number Of Titles','genre':'Genre'})
most_common_genre_fig.update_traces(textposition='inside',insidetextanchor='start', marker=dict(color='skyblue'))
most_common_genre_fig.update_layout(template='plotly_white',yaxis={'categoryorder':'total ascending'})
text("Most Common Genres")
plotly(most_common_genre_fig)
table(most_common_genre_df)
