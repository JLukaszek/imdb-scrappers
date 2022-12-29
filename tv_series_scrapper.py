import random
import requests
from bs4 import BeautifulSoup

link = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'


def main():
    response = requests.get(link)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    series_tags = soup.select('td.titleColumn')
    inner_series_tags = soup.select('td.titleColumn a')
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    def get_year(series_tag):
        series_split = series_tag.text.split()
        year = series_split[-1]
        return year

    years = [get_year(tag) for tag in series_tags]
    actors_list = [tag['title'] for tag in inner_series_tags]
    titles = [tag.text for tag in inner_series_tags]
    ratings = [round(float(tag['data-value']), 1) for tag in rating_tags]

    n_movies = len(titles)
    while True:
        idx = random.randrange(0, n_movies)
        print(f"Rank: {idx+1}, {titles[idx]} {years[idx]}, rating: {ratings[idx]}, starring: {actors_list[idx]}")
        user_input = input('Do You want another movie recommendation? (y/[n])? ')
        if user_input != 'y':
            break


if __name__ == '__main__':
    main()
