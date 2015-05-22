def finder(class):
	def __init__():
		print 'init_finder'

	def find_note(soup,c):
		notes= soup.find('div',{'id':'note'})
		for n in notes.div.find_all('div'):
			try:
				title = n.div.a.string
				note = n.find('div',{'class':'note'}).string
				c.execute("INSERT INTO notes VALUES (self.id_,title,note)")
			except:
				pass

	def find_music(soup):
		notes= soup.find('div',{'id':'note'})
		for n in notes.div.find_all('div'):
			try:
				title = n.div.a.string
				note = n.find('div',{'class':'note'}).string
				c.execute("INSERT INTO notes VALUES (id_,title,note)")
			except:
				pass

	def find_books(soup):
		notes= soup.find('div',{'id':'note'})
		for n in notes.div.find_all('div'):
			try:
				title = n.div.a.string
				note = n.find('div',{'class':'note'}).string
				c.execute("INSERT INTO notes VALUES (id_,title,note)")
			except:
				pass

	def find_movies(soup):
		for m in soup.find('div',{'id':'movie'}).find_all('div'):
			for mo in m.url.find_all('li'):
				title = mo.a.title
				self.c.execute("INSERT INTO movies VALUES (self.id_,title)")