#import libraries
import urllib2  
from bs4 import BeautifulSoup  
import re
a = [0,1,2]
str = []
str1 = []
# specify the url
quote_page = 'http://www.espncricinfo.com/indian-premier-league-2015/engine/series/791129.html'  

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)  

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser') 

# Take out the <div> of name and get its value
name_box = soup.find_all('h2')

for i in a:
	name = name_box[i].text.strip()
	#print(name) 
for link in soup.find_all('a',href = re.compile('^/indian-premier-league-2015/engine/match/8297')):
    #print(link.get('href'))
    str.append(link.get('href'))  
#print 'http://www.espncricinfo.com' + str[0]  

for j in range (0,len(str)):  #for each team vs team
	quote_page1 = 'http://www.espncricinfo.com' + str[i] 
	page1 = urllib2.urlopen(quote_page1)
	soup1 = BeautifulSoup(page1,'html.parser')
	name1_box = soup.find_all('td',attrs={'class': 'playerName'})
	for link1 in soup.find_all()
	for k in range (0,len(name_box)):
		str1.append(link.get())
	str1.append()
	#name1_box = soup.find_all('a',href = re.compile('^/indian-premier-league-2015/content/player/'))
	print(name1_box[0])


	'''
	for k in a:
		name1 = name1_box[i].text.strip()
		print(name1) #playername
	'''
	
