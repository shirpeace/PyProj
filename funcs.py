# Shi's functions for Py practice
import random
import requests
from bs4 import BeautifulSoup

def hello():
    name = input('What is your name?')
    number = str(random.randint(2, 6))
    print('Hello ' + name + ', \nHere is a random number: ' + number)
    return


def pageTitle(url):
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html, 'html.parser')
    title = soup.title
    print('This is GitHub title: ' + title.string)
    return

def NYTtitles():
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
    print('file ' + filename + ' saved')
    return

    # read list of names from files
    # count how many times each name repeats
    # save to dictionary and print it
def listFromFile():
    names = {} #init a dictionary
    filename = input("File to read: ")
    with open(filename, 'r') as f:
        # contents = f.read()
        # print(contents)
        for name in f:
            # extract & strip the element 
            #name = name.strip() #for names file
            name = extractCategory(name)
            if name in names:
                names[name] +=1
            else :
                names[name] = 1
    print (names)
    return
    
    
def extractCategory(line):
    spl = line.rsplit('/', 1) #beware of special char
    spli = spl[0].rsplit('/', 1)
    return spli[1]
    
    
def piramid(x):
    #print a piramid of stars, x wide
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    