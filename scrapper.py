#imports
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

#Get the
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

movie_container_div = html_soup.find_all('div', class_ = 'lister-item mode-advanced')

# Lists to store the scraped data in
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

for container in movie_container_div:
    if container.find('div', class_ = 'ratings-metascore') is not None:

        #Get the name
        name = container.h3.a.text
        names.append(name)

        # The year
        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)

        # The IMDB rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        # The Metascore
        m_score = container.find('span', class_='metascore').text
        metascores.append(int(m_score))

        # The number of votes
        vote = container.find('span', attrs={'name': 'nv'})['data-value']
        votes.append(int(vote))


test_df = pd.DataFrame({'movie': names,
                       'year': years,
                       'imdb': imdb_ratings,
                       'metascore': metascores,
                       'votes': votes})
print(test_df)

