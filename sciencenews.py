from bs4 import BeautifulSoup
import requests
import sys
from tabulate import tabulate
from datetime import date

url=''
baseUrl = 'https://www.sciencenews.org/topic/'
options = ['neuroscience' ,'plants', 'animals', 'earth', 'space' , 'humans', 'life' ,'genetics', 'agriculture', 'microbes', 'climate', 'computing', 'artificial-intelligence', 'psychology', 'enviroment']


try:
	if len(sys.argv)<2:
		print('Note: Run the script as python3 newsfeed.py earth')
		print(options)
	elif sys.argv[1] not in options:
		print('Note: Run the script as python3 newsfeed.py earth')
		print(options)
	else:
		print('\033[1m')
		print('ScienceNews')
		print(date.today())
		url = baseUrl + sys.argv[1]
		print(url)
		webpage = requests.get(url)
		soup = BeautifulSoup(webpage.content, 'lxml')

		temp = []
		finalList = []

		headings = soup.select('h3 a', href=True)
		c=0
		for heading in headings[15:28]:
			c+=1
			temp = [c,heading.text.strip(),heading['href'].strip()]
			finalList.append(temp)
		print(tabulate(finalList,tablefmt='rst'))
		print('Himanshu Soni, 2021')
except NameError:
		print('Something went wrong, try again')
