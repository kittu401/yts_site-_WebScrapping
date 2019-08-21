File_size = []
Resolutoin = []
Languageb=[]
Rating = []
Subtitles = []
Frame_rate = []
Run_time = []
Peers = []

Torrent_link = []
Title_n=[]
IMDB_link =[]
image_link=[]
Genre_g = []


scr_one =[]
scr_two=[]
scr_three = []

from PIL import Image
import requests
import os
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("E:\Tester\selenium\chromedriver.exe")

driver.maximize_window()
driver.get("https://yts.tl/rss//0/all/all/0")  # ---->>> PLease change RSS url Here its enough no need to change anythin
driver.implicitly_wait(12)
content = driver.page_source
formatted = bs(content,features='lxml')
# code for torent link

torrent = formatted.findAll('enclosure')
for i in torrent:
    torrent_link = 'https://yts.tl/'+(i['url'])
    Torrent_link.append(torrent_link)

    # block ends

movie_link = formatted.findAll('guid')

for i in movie_link:
    url = "https://yts.tl/"+str(i.text)

    driver.get(url)
    time.sleep(3)
    content2 = driver.page_source
    format = bs(content2,features='lxml')

    # Code for Movie Title
    Title = format.find('h1', attrs={'itemprop': 'name'}).text

    '''included replace method because while creating folder it wont accept characters 
        like \ / : ? " < > | to remove these from title '''


    Title = Title.replace(':', " ")
    Title_n.append(Title)
    # movie title ends

    # Code block for imdb link
    imdb_link = format.find('a', href=True, attrs={'title': 'IMDb Rating'})
    IMDB_link.append(imdb_link['href'])
    # code ends

    # block for Image url
    image = format.find('img',attrs={'itemprop':'image'})
    if 'alt' in image.attrs:
        image_link.append(image.attrs['src'])

        #image url block ends

    # Code clock for Genre
    type  = format.find('div',attrs={'id':'movie-info'})
    genre = 0
    for i in type.findAll('h2'):
        genre = i
    Genre_g.append(genre.text)
    # Block Ends
    list = []
    # code block for file size
    if "#1080p" in url:

        size = format.find('div', attrs={'class': 'tech-spec-info col-xs-20 hidden-tech-info'})
        # File_size = format.find('span',attrs ={'title':'File Size'})
        for details in size.findAll('div', attrs={'class': 'tech-spec-element col-xs-20 col-sm-10 col-md-5'}):
            list.append(details.text)

        File_size.append(list[0])
        Resolutoin.append(list[1])
        Languageb.append(list[2])
        Rating.append(list[3])
        Subtitles.append(list[4])
        Frame_rate.append(list[5])
        Run_time.append(list[6])
        Peers.append(list[7])
    elif "#720p" in url:

        size = format.find('div', attrs={'class': 'tech-spec-info col-xs-20'})
        # File_size = format.find('span',attrs ={'title':'File Size'})
        for details in size.findAll('div', attrs={'class': 'tech-spec-element col-xs-20 col-sm-10 col-md-5'}):
            list.append(details.text)

        File_size.append(list[0])
        Resolutoin.append(list[1])
        Languageb.append(list[2])
        Rating.append(list[3])
        Subtitles.append(list[4])
        Frame_rate.append(list[5])
        Run_time.append(list[6])
        Peers.append(list[7])

    # Code block for screenshot images

    for size in format.findAll('a',attrs={'class':'screenshot-group imghov cboxElement'}):
    # File_size = format.find('span',attrs ={'title':'File Size'})
    # for details in size.findAll('div', attrs={'class': 'tech-spec-element col-xs-20 col-sm-10 col-md-5'}):

        image = size.find('img')
        if 'alt' in image.attrs:
            list.append(image.attrs['src'])

    scr_one.append(list[0])
    scr_two.append(list[1])
    scr_three.append(list[2])

    # code block ends

    n = 0
    for i in image_link:
        for j in Title_n:
            path = "E:\Python\python work space\webScraping\\freelancer\\" + j  # change Path name according to your's
            x = os.path.exists(path)
            if x is True:
                os.chdir(path)
                url = str(i)
                img = Image.open(requests.get(url, stream=True).raw)
                img.save(j + ".jpg")
                os.chdir("E:\Python\python work space\webScraping\\freelancer")
                n = n + 1
            elif x is False:
                os.mkdir(path)
                os.chdir(path)
                url = str(i)
                img = Image.open(requests.get(url, stream=True).raw)
                img.save(j + ".jpg")
                os.chdir("E:\Python\python work space\webScraping\\freelancer")
                n = n + 1





''' df = pd.DataFrame({'Title':Title_n,'Image':image_link,'IMDB Link':IMDB_link,
                   'Torrent':Torrent_link,'Genre':Genre_g,'Rating':Rating,
                   'File_size':File_size,'Resolution':Resolutoin,'Run_time':Run_time,
                    'Language':Languageb,'Frame-rate':Frame_rate,'img_one':scr_one,
                   'img_two':scr_two,'img_three':scr_three})

df.to_csv('Movie_details.csv', index=False, encoding='utf-8')'''