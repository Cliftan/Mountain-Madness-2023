# terminal pip3 install requests
import requests
from bs4 import BeautifulSoup

def scraper(searchTerm):
    response = requests.get("https://www.urbandictionary.com/"+searchTerm)

    soup = BeautifulSoup(response.content, "html.parser")

    for i in soup.findAll('br'):
        i.replace_with('\n')

    results = soup.find(id = "ud-root")
    definition = results.find("div", class_ = "break-words meaning mb-4")
    definition = definition.text
    if definition == None:
        print("no definition found for this term")
        exit()

    example = results.find("div", class_ = "break-words example italic mb-4")
    example = example.text
    
    finalResult = (definition + "\n" + example)
    return finalResult


