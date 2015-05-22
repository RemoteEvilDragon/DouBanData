import requests
from bs4 import BeautifulSoup
import sqlite3

global db_path = 'data/crawl.db'
url = 'https://www.douban.com/accounts/login'

s = requests.Session()

soup = BeautifulSoup(s.get(url).content)

data_ = None

if soup.find('div',{'class':'item item-captcha'}) is not None:#detect crack verifyCode.
	data_ = {'captcha-solution':'pic',
	'captcha-id':'',
	'source':'index_nav',
	'form_mail':'uuqqii@163.com',
	'form_password':'12300000',
	'remember':'on'}
	print'need_verify'
else:
    data_ = {'source':'index_nav',
    'form_mail':'uuqqii@163.com',
    'form_password':'12300000',
    'remember':'on'}
    print 'no_need'


soup = s.post(url,data=data_).content
#日记

global conn = open_db()
global c = conn.cursor()

global id_ = soup.find



def open_db():
	conn = sqlite3.connect(db_path)
	c = conn.cursor()
	c.execute('CREATE TABLE books(id text,book text)')
	c.execute('CREATE TABLE movies(id text,movie text)')
	c.execute('CREATE TABLE music(id text,music text)')
	c.execute('CREATE TABLE notes(id text,title text,content text)')
	return conn

c.commit()
conn.close()


