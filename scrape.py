# terminal pip3 install requests
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.urbandictionary.com/")

soup = BeautifulSoup(response.content, "html.parser")

for i in soup.findAll('br'):
    i.replace_with('\n')

results = soup.find(id = "ud-root")
definition = results.find("div", class_ = "break-words meaning mb-4")
if definition == None:
    print("no definition found for this term")
    exit()

print(definition.text)

example = results.find("div", class_ = "break-words example italic mb-4")
print(example.text)
