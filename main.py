import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")


with open("movies.txt", "w") as file:
    movie_titles = [movie.getText() for movie in all_movies]  # list comprehension
    movie_titles.reverse()
    for movie in movie_titles:
        file.write(f"{movie}\n")
