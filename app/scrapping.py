# # from bs4 import BeautifulSoup
import requests
from flask import request
import json
import urllib3
# import ast
def scrape():
	

	# url = 'https://indreed.herokuapp.com/api/jobs?q=web+developer&limit=50'
	# # items=''
	# http = urllib3.PoolManager()
	# r = http.request('GET',url)
	# soup = BeautifulSoup(r.text,"html.parser")
	# all_product = soup.data

	url = 'https://indreed.herokuapp.com/api/jobs?q=web+developer&limit=50'
	# items=''
	r = requests.get(url)

	# print(r.text)
	# with open('data.txt','w+') as file:
	# 	file.write(r.text)

	# f= open('data.txt')
	
	# myfile = f.read()
	# a = ast.literal_eval(myfile)
	
	return json.loads(r.text)
# r = requests.get(url)
# s=""

# for i in r:
# 	s=s+str(i)

# print(s)


# f = open('E:/data.text')
# myfile = f.read()
# a = ast.literal_eval(myfile)
# b=[]
# for i in a:
# 	if i["title"].lower()=="Associate WEb Developer".lower():
# 		b.append(i)
# print([x["title"] for x in b if x["title"]=="Associate Web Developer"])



# url = 'https://indreed.herokuapp.com/api/jobs?q=web+developer&limit=50'
	# items=''
# http = urllib3.PoolManager()
# r = http.request('GET',url)
# for i in r.data:
# 	print(i)
# 	print('***********')


# url = 'https://indreed.herokuapp.com/api/jobs?q=web+developer&limit=50'
# 	# items=''
# r = requests.get(url)
# # print(r.text)
# with open('data.txt','w+') as file:
# 	file.write(r.text)

# f= open('data.txt')
# c = f.read()

# print(c)


# str=[{'name':'shubham', 'age':None},{'name':'nitin','age':20}]
# # lst =ast.literal_eval(str)

# for i in str:
# 	print(i.values())










