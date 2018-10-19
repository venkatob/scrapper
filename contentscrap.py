import urllib2
wiki = "https://www.geeksforgeeks.org/"

#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(wiki)

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)

all_link=soup.find_all("img")
for i in all_link:
	print(i)