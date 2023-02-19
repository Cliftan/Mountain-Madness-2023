# terminal pip3 install requests
import requests
import numpy as np
from bs4 import BeautifulSoup

def scraper(searchTerm):
    file = open("badWords.txt",'r')

    response = requests.get("https://www.urbandictionary.com/"+searchTerm) 
    soup = BeautifulSoup(response.content, "html.parser")

    for i in soup.findAll('br'):
        i.replace_with('\n')

    results = soup.find(id = "ud-root")
    definition = results.find("div", class_ = "break-words meaning mb-4") 
    if definition == None:
        return 0
    definition = definition.text



    example = results.find("div", class_ = "break-words example italic mb-4")
    example = example.text
    
    #censor
    temp = definition.split( )
    temp2 = example.split()

    for i in file:
        definition = ""
        example = ""
        for j in range(len(temp)):
            if i.strip("\n,.").lower() in temp[j].lower():
                tempA = ""
                for q in range(len(temp[j])):
                    tempA += "*"
                temp[j] = tempA
            definition += temp[j]+" "
        for k in range(len(temp2)): 
            if i.strip("\n,.").lower() in temp2[k].lower():
                temp2A = ""
                for w in range(len(temp2[k])):
                    temp2A += "*"
                temp2[k] = temp2A
            example += temp2[k]+" "
        j = 0
        k = 0

    return definition,example
