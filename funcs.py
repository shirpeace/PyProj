# Shi's functions for Py practice
import random  ,json , math
import requests
from bs4 import BeautifulSoup
from collections import Counter
from datetime import datetime

from bokeh.plotting import figure, show, output_file

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
    size = x
    while size > 0 :
        print(' '*(x-size) + '* '*size)
        #print('* '*size + '\n')
        size -=1
    return
    
    
def readDict():
    #read from file and populate a dictionary of birthday dates        
    with open("info.json", "r") as f:
        stringDict = json.load(f)
    return stringDict


def dateAsString(date):
    return date.strftime("%d/%m/%Y")

def printDict(data):
    for d in data:
        print(d + ': ' + dateAsString(data[d]))

def bdaysProgram(bdays, action='6'):
    if action == '0' :
        action = input('Would you like to: \n1 - Check a date\n2 - Add/edit a date\n3 - See list of people\n4 - Count by month\n5 - Show months graph\n6 - What is today?\nX - Exit\n>')
    if action == '1' :
        choose = input('Who\'s birthday do you want to look up?\n>')
        if choose in bdays:
            print('{}\'s birthday is {}'.format(choose,bdays[choose]))
        else:
            print('Sorry, We don\'t know {}'.format(choose))
    elif action == '2' :
        newName = input('What\'s the person\'s name? ')
        newDate = input('And the birthday? (in \'dd/mm/yyyy\' format) ')
        if validDate(newDate) :
            # person exists in dict 
            if newName in bdays :
                editAction = input('This person is already in the list! Should we update the date?\nCurrently: {}\n Please Type: \'Y\'/\'N\'\n>'.format(bdays[newName]))
                if editAction in ['Y','y'] :
                    bdays[newName] = newDate
                    print('Change saved')
            # new person
            else : 
                bdays[newName] = newDate
                print('New birthday saved')
        else :
            print('Wrong date format!\n')
    elif action == '3' :
        print('We know this people\'s birthdays:')
        for n in bdays:
                print(n)
    elif action == '4' :
        monthList = datesCount(bdays)
        print(monthList)
    elif action == '5' :
        datesCountShow(bdays)
    elif action == '6' :
        WhatIsToday(bdays)
    elif action in ['X','x'] :
        saveDict(bdays)
        return
    else :
        print('Oops! You have to type 1/2/3/4/5/6/X\n')
    
    bdaysProgram(bdays,'0')
    return

def saveDict(data):
    with open("info.json", "w") as f:
        json.dump(data, f)
    return
    
def bdaysMain():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  Welcome to the Birthday Dictionary!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    bdays = readDict()
    bdaysProgram(bdays)

def datesCount(bdays):
    tempList = []
    num_to_string = {
        1: "January",
        2: "February",
        3: "March", 
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    for d in bdays.values():
        month = int(d.split("/")[1])
        tempList.append(num_to_string[month])
    return Counter(tempList)

def validDate(test_str):
    # initializing format
    format = "%d/%m/%Y" 
    # checking if format matches the date
    res = True
    # using try-except to check for truth value
    try:
        res = bool(datetime.strptime(test_str, format))
    except ValueError:
        res = False
    return res

def datesCountShow(bdays):
    tempList = []
    num_to_string = {
        1: "January",
        2: "February",
        3: "March", 
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    for d in bdays.values():
        month = int(d.split("/")[1])
        tempList.append(num_to_string[month])
    data = Counter(tempList)
    output_file("plot.html")
    x_categories = [str(i) for i in num_to_string.values()] #.values
    
    x = [str(i) for i in data.keys()]
    y = [str(i) for i in data.values()]
    
    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=0.5)
    show(p)

def WhatIsToday(bdays):
    tempList = []
    today = datetime.today()
    todayStr = dateAsString(today)
    
    for n in bdays:
        if bdays[n] == todayStr :
            tempList.append((n,bdays[n]))
    
    print('Celebrate Today:')
    print(tempList)
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

