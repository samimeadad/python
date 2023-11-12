import pandas as pd

df = pd.read_html(
    "https://en.wikipedia.org/wiki/List_of_highest-grossing_films")

print(df[0])

df[0].to_excel("movie.xlsx")
