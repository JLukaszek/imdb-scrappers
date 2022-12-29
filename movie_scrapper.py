import random
import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top'


def main():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    movie_tags = soup.select('td.titleColumn')
    inner_movie_tags = soup.select('td.titleColumn a')
    rating_tags = soup.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag):
        movie_split = movie_tag.text.split()
        year = movie_split[-1]
        return year

    years = [get_year(tag) for tag in movie_tags]
    actors_list = [tag['title'] for tag in inner_movie_tags]
    titles = [tag.text for tag in inner_movie_tags]
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
