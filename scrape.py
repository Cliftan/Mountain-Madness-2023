# terminal pip3 install requests
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.urbandictionary.com/rizz")

soup = BeautifulSoup(response.content, "html.parser")

for i in soup.findAll('br'):
    i.replace_with('\n')
    
results = soup.find(id = "ud-root")
definition = results.find("div", class_ = "break-words meaning mb-4")
print(definition.text)

example = results.find("div", class_ = "break-words example italic mb-4")
print(example.text)




# url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"




# querystring = {"term":"wat"}

# headers = {
# 	"X-RapidAPI-Key": "921e591a9emsh1d05878404e0f88p13def1jsna7e4f4ef1e76",
# 	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)