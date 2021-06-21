import random
import requests
from bs4 import BeautifulSoup
name = input('What is your name?')
number = str(random.randint(2, 6))
print('Hello ' + name + ', here is a random number: ' + number)


url = 'http://github.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

title = soup.title
print('This is GitHub title: ' + title.string)


ny_url = 'https://www.nytimes.com'
ny = requests.get(ny_url)
ny_html = ny.text
ny_soup = BeautifulSoup(ny_html, 'html.parser')
ny_titles = ny_soup.find_all('h3') 

# print('NY Times titles: ')
# for title in ny_titles :
  # print(title)
  # if title.find('span') != None :
    # print(title.find('span').text.strip())
  # else :
    # print(title.text.strip())
    
filename = input("File to save to: ")
with open(filename, 'w') as file:
    file.write('NY Times titles: \n')
    for title in ny_titles :
        if title.find('span') != None :
            file.write(title.find('span').text.strip() + '\n')
        else :
            file.write(title.text.strip() + '\n')