
import requests
import os
from newspaper import Article
from blogpost import make_post
url = "https://news.bitcoin.com/what-uk-bitcoin-investors-should-know-as-tax-deadline-approaches/"


def article_content(url):
    content = dict()
    article = Article(url, language='en')
    article.download()
    article.parse()
    print(article.title)
    content['title'] = article.title
    print(article.text)
    content['body'] = article.text
    print(article.top_image)
    # For Image We Will Save Our Image Path In To Our Dictionary
    # Lets Download And Save The Image

    # Using Requests To Download And Save The Image File In Our Local Directory
    resp = requests.get(article.top_image)
    with open('1.jpg', 'wb') as imagefile:
        imagefile.write(resp.content)
    content['image'] = '1.jpg'
    return content


make_post(article_content(url))
