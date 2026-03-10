from bs4 import BeautifulSoup
import requests

# with open("website.html") as file:
#     website = file.read()
website_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=website_url)
website = response.content
soup = BeautifulSoup(website,'html.parser')
movies = [(movie.getText()).strip() for movie in soup.select('h3.title')]

with open("movies.txt", "w") as file:
    file.write(f"{'ID':<5} {'TITLE'}\n")
    file.write("-" * 50 + "\n")
    for i, movie in enumerate(movies, start=1):
        title = movie.strip().split(') ', 1)[-1]
        file.write(f"{i:<5} {title:<50}\n")