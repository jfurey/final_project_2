from bs4 import BeautifulSoup
import requests
import csv


def web_scrape(age_selected):
    '''
    Method to conduct web scrape of pet adoption site, extract name, breed, and age of available dogs, and output results to CSV file.
    '''
    url = 'https://bestfriends.org/adopt/adopt-our-sanctuary/dogs'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('div', class_='animal-item-view views-row')

    #Output results of web scrape to a CSV file
    with open('dogs.csv', 'w', newline='') as f:
        content = csv.writer(f)
        header = ['Name', 'Breed', 'Age']
        content.writerow(header)
            
        for list in lists:
            name = list.find('span', class_='animalName').text
            breed = list.find('span', class_='animalBreed').text
            age = list.find('span', class_='animalAge').text
                
            info = [name, breed, age]
            content.writerow(info)

    #Create list containing all data from CSV file
    with open('dogs.csv', 'r') as f:
        csvreader = csv.reader(f)
        rows = []
        for row in csvreader:
            rows.append(row)
    
    #Iterate through list to find results that match age group selected by user; create new list of all matches
    age = age_selected
    output_list = []
    
    if age == 0:
        for row in rows:
            if row[2] == 'Baby':
                output_list.append(row)

    elif age == 1:
        for row in rows:
            if row[2] == 'Young':
                output_list.append(row)
                            
    elif age == 2:
        for row in rows:
            if row[2] == 'Adult':
                output_list.append(row)
                    
    else:
        for row in rows:
            if row[2] == 'Senior':
                output_list.append(row)
    
    #Iterate through list of matches to output final results to a CSV file
    with open('results.csv', 'w', newline='') as f:
        content = csv.writer(f)
        header = ['Name', 'Breed', 'Age']
        content.writerow(header)
            
        for list in output_list:
            content.writerow(list)