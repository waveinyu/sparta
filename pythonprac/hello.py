import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sis7sux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# headers : 헤더에서 콜을 날리지만 마치 우리가 브라우저에 콜을 날린 것처럼 보이게 함
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

# print(movies) # 리스트 형태로 출력
# 리스트니까 for문을 돌리자!

for movie in movies:
    a = movie.select_one('td.title > div > a')

    if a is not None:
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text
        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
        db.moives.insert_one(doc)
