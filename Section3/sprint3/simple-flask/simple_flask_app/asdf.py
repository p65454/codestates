import csv

with open('users.csv') as csvfile:
        #userlist = {[csv.reader(csvfile)]}
        user_csv = csv.reader(csvfile)
        userlist = {'users': [row[0] for row in user_csv][1:]}
print(userlist)