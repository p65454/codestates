"""
Part_2 

NoSQL 데이터 입력하기 (Github API - User octokit repos)

Github API 를 이용해서 octokit 이란 사용자의 정보를 받아왔습니다.
아래 변수는 유지한 채로 Github API - User octokit 데이터를 MongoDB 에 입력하세요

pytest 로만 통과할 수 없습니다. `python src/Part_2.py`로 MongoDB 에 데이터를 입력하세요
# 클라우드 데이터베이스는 테스트에 시간이 걸릴 수 있습니다. 기다려주세요.
# 해당 테스트는 완료 후, 이 데이터를 RDB 에 저장한다면 NoSQL 이 빠를지 한번 생각해보세요
"""

import time
import copy
import requests

octokit = ''
dont_touch= []
response = requests.get("https://api.github.com/users/octokit/repos")
# 주의할 점 : github API 는 호출이 너무 많이 발생하면 자체적으로 제한을 걸 수 있습니다.
# 한번의 API 호출 후 1초 sleep 시간을 지정합니다.
time.sleep(1)

if response.status_code == 200:
    octokit = response.json()
    dont_touch = copy.deepcopy(octokit)

"""
MONGODB SETUP
"""
from pymongo import MongoClient

HOST = 'cluster0.jl2z6.mongodb.net'
USER = 'bsch0111'
PASSWORD = '12345'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'octokit_repos'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

"""
위 코드는 힌트입니다. 자신에 맞는 HOST,USER, PASSWORD, DATABASE_NAME 을 입력하세요
! COLLECTION_NAME = 'octokit_repos'
아래 pass 를 지우고 코드를 작성하세요

- 데이터베이스와 연결한 뒤 Collection 이라는 테이블과 연결하는 작업이 가장 오래걸리실 겁니다.
"""

client = MongoClient(MONGO_URI)
collection =client[DATABASE_NAME][COLLECTION_NAME]
collection.insert_many(octokit)