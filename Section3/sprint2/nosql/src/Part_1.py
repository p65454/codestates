"""
Part_1

NoSQL 데이터 입력하기 (Openweather API)

Openweather 에서 받아올 수 있는 JSON 데이터가 작성되어 있습니다.
MongoDB 에 Openeather 데이터를 입력하세요

하단의 pass 라는 코드를 지우고 문제를 풀어주세요

pytest 로만 통과할 수 없습니다. `python src/Part_1.py`로 MongoDB 에 데이터를 입력하세요
# 클라우드 데이터베이스는 테스트에 시간이 걸릴 수 있습니다. 기다려주세요.
"""
openweather = {
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  }
  
"""
MONGODB SETUP
"""

dont_touch = openweather.copy()

from pymongo import MongoClient

HOST = 'cluster0.jl2z6.mongodb.net'
USER = 'bsch0111'
PASSWORD = '12345'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'openweather'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

"""
위 코드는 힌트입니다. 자신에 맞는 HOST,USER, PASSWORD, DATABASE_NAME 을 입력하세요
! COLLECTION_NAME = 'openweather'
아래 pass 를 지우고 코드를 작성하세요

- 데이터베이스와 연결한 뒤 Collection 이라는 테이블과 연결하는 작업이 가장 오래걸리실 겁니다.
"""

client = MongoClient(MONGO_URI)
collection =client[DATABASE_NAME][COLLECTION_NAME]
collection.insert_one(openweather)