# terminal pip3 install requests
import requests

# endpoint url for urban dictionary api
url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

# default query params for api key and host name
headers = {
    "X-RapidAPI-Key": "921e591a9emsh1d05878404e0f88p13def1jsna7e4f4ef1e76",
    "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
}

# requests the definition of the term and returns a json response from the API
def define(word):
    querystring = {"term": word}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

# response.json() for a given "term" input is a list of all definitions, from most to least upvotes
# format of each list is: {definition} {permalink} {example} {author} {word} {thumbs_up} {thumbs_down} {sound_urls}
# eg. {definition['list']} returns all definitions for term
# eg. {definition['list'][0]} returns the top definition
# eg. {definition['list'][0]['author']} returns the author for the top definition

# accept input term for function definition
# term = input("What term would you like to define?\n")
# get a term from the user

def defineWord(term):
    definition = define(term)

    # if definition exists as a list:
    if definition["list"]:
        theDef = definition['list'][0]['definition'].replace("[", "").replace("]", "").lower()
        theExmpl = definition['list'][0]['example'].replace("[", "").replace("]", "").lower()
    else:
        error = 0
        return error

    # check and censor for bad words
    badWordsTxt = open("badWords.txt")
    badWords = badWordsTxt.read().split("\n")  # create a list of bad words we wish to censor

    for word in badWords:
        theDef = theDef.replace(word, "*" * len(word))
        theExmpl = theExmpl.replace(word, "*" * len(word))

    response = f"\nThe definition of '{term}':\n{theDef}\n\nFor example:\n{theExmpl}"

    return theDef, theExmpl
