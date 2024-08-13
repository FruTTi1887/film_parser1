from bs4 import BeautifulSoup
import requests
import random


def links_parcer(url, temp_url):
    movie_links = []
    temp_url = url
    for i in range(1, 6):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            if link['href'].startswith('/movie/'):
                movie_link = link['href']
                movie_link = 'https://movielib.ru' + movie_link
                if movie_link in movie_links:
                    continue
                movie_links.append(movie_link)
        for link in movie_links:
            if 'reviews' in link:
                movie_links.remove(link)
        url = temp_url + str(i)
    random_film = movie_links[random.randint(0, len(movie_links)-1)]
    return(random_film)

def film_info(url):
    janr_list = ['Детектив', 'Ужасы', 'Триллер', 'Боевик', 'Драма', 'Криминал', 'Фэнтези', 
                 'Романтика', 'Анимация', 'Комедия', 'Приключения', 'Семейный', 'Мелодрама', 'Аниме', 'Фантастика', 'Биография']
    
    count = 0
    title_name = ''
    genre = '' 
    hrono = ''
    rank = ''
    country = ''
    soderjanie = ''

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title_names = soup.find_all('h1', class_='embossed movie-title')
    for movie_name in title_names:
        title_name = movie_name.text

    janrs = soup.find_all('a', href=True)
    for janr in janrs:
        if janr.text in janr_list:
            genre = genre + janr.text + ' '


    hronomitraj = soup.find_all('td')
    for hronomit in hronomitraj:
        if 'мин.' in hronomit.text:
            hrono = hronomit.text


    ranks = soup.find_all('span', class_='average')
    for rank in ranks:
        rank = rank.text


    movie_countrys = soup.find_all('td')
    for movie_country in movie_countrys:
        country = movie_country.text
        if count == 1:
            break
        if 'Страна' in movie_country.text:
            count += 1


    movie_soderjanie = soup.find_all('p', class_='intrigue description summary')
    for movie_soderjan in movie_soderjanie:
        soderjanie = movie_soderjan.text

    output = 'Название фильма: ' + title_name + '\n' + 'Жанры: ' + genre[138:] + '\n' + 'Хронометраж: ' + hrono + '\n' + 'Оценка: ' + rank + '\n' + 'Страна: ' + country + '\n' + 'Содержание: ' + soderjanie + '\n' + 'Ссылка на фильм: ' + url
    return(output)


def movie_photo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie_photo = soup.find_all('img', itemprop="image")
    for photos in movie_photo:
        photo = str(photos)
        photo = photo.split('src="')
        photo_link = photo[1].split('"')[0]
    return(photo_link)
