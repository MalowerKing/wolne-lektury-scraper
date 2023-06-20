import requests
from bs4 import BeautifulSoup as bs

#scraping data from Wolne Lektury and writing it into .txt file
def dataScraping (page):
 
    cookies = {'session' : 'gv9UhDuKBbyztZae8fdU0NQHngaMr2F0cCZrpAjCLITvF1n7A2VPJuwG2AtNK49J'}
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
        "Accept-Encoding" : "gzip, deflate, br",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "DNT" : "1",
        "Connection" : "Close",
        "Upgrade-Insecure-Requests" : "1"
    }
    page = requests.get('https://wolnelektury.pl/katalog/lektury/?page={page}'.format(page=page),
                           headers=headers,
                           cookies= cookies
                           ).text
    html = bs(page, 'lxml')
    bookContainer = html.find_all('article', attrs= {'class' : 'l-books__item book-container-activator'})
    with open('wolne_lektury_tytuly.txt','a', encoding="utf-8") as output:
        for book in bookContainer:                         
            title = book.find('h2').text
            author = book.find('h3').text
            output.write(title+ ', '+ author)
    

for i in range (1,25):
    dataScraping(i)