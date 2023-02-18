# terminal pip3 install requests
import requests

#endpoint url, delineates what data we are interacting with
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":"wat"}

headers = {
	"X-RapidAPI-Key": "921e591a9emsh1d05878404e0f88p13def1jsna7e4f4ef1e76",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}
def define(term):
    querystring = {"term": term}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

term = input("What term would you like to define? ")
definition = define(term)

if definition["list"]:
    print(f"Definition of {term}: {definition['list'][0]['definition']}")
else:
    print(f"No definition found for {term}")