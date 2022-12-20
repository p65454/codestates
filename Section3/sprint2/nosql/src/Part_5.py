"""
Part_6

NoSQL 데이터 입력하기 (csv-titanic)

클러스터 및 데이터베이스를 생성한 뒤에 titanic.csv 에 있는 탑승객 데이터 하나마다 문서로 저장합니다.

필요에 따라 추가로 코드를 작성합니다.

각 값의 데이터 타입은 아래와 같습니다. (필드명은 자유입니다).
아래에는 각 필드에 해당하는 데이터 타입입니다.
- Survived: int
- Pclass: int
- Name: str
- Sex: str
- Age: float
- Siblings/Spouses Aboard: int
- Parents/Children Aboard: int
- Fare: float

다 옮긴 뒤에 'passengers' 데이터베이스 정보를 아래 입력합니다.
해당 파트를 진행할 때는 titanic.csv 는 과제 레포에 있는 파일을 사용해야 합니다.
"""

import csv
import os
from pymongo import MongoClient

HOST = 'cluster0.jl2z6.mongodb.net'
USER = 'bsch0111'
PASSWORD = '12345'
DATABASE_NAME = 'myFirstDatabase'
COLLECTION_NAME = 'passengers'

MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

"""
위 코드는 힌트입니다. 자신에 맞는 HOST,USER, PASSWORD, DATABASE_NAME 을 입력하세요
! COLLECTION_NAME = 'openweather'
아래 pass 를 지우고 코드를 작성하세요
"""

CONNECTION = MongoClient(MONGO_URI)

def retrieve_data(file_path):

    data = []
    with open(file_path,'r') as csvfile:
        
        csv_reader = csv.DictReader(csvfile)
        
        for idx, row in enumerate(csv_reader):
            print(f"Reading Data {idx} : {row}")
            data.append({
                'Survived':int(row['Survived']),
                'Pclass':int(row['Pclass']),
                'Name':row['Name'],
                'Sex':row['Sex'],
                'Age':float(row['Age']),
                'Siblings/Spouses Aboard':int(row['Siblings/Spouses Aboard']),
                'Parents/Children Aboard':int(row['Parents/Children Aboard']),
                'Fare':float(row['Fare'])
            })
    return data

def get_collection(conn, db_name, coll_name):
    return conn[f"{ db_name }"][f"{coll_name}"]

def insert_data(collection, data):
    for i,d in enumerate(data) :
        try:
            print(f"inserting {d}")
            collection.insert_one(d)
        except Exception as e:
            print("Error occurred while inserting {d}")
            print(e)

def migrate_csv():
    filename = 'titanic.csv'
    file_path = os.path.join(os.getcwd(), filename)
    collection = get_collection(CONNECTION, DATABASE_NAME, COLLECTION_NAME)
    data = retrieve_data(file_path)

    insert_data(collection, data)
    print('Done')


