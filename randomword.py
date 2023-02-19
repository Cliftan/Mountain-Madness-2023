import requests
import json 

def random():
    response = requests.get("https://api.urbandictionary.com/v0/random")
    return response.text

def randomWord():
    file = open("badWords.txt",'r')
    data = json.loads(random())
    firstdef = data["list"][0]
    definition = firstdef["definition"]
    word = firstdef["word"]
    example = firstdef["example"]

    word = word.replace("[", "").replace("]", "").lower()
    definition = definition.replace("[", "").replace("]", "").lower()
    example = example.replace("[", "").replace("]", "").lower()


    temp = definition.split( )
    temp2 = example.split()
    temp3 = word.split()

    for i in file:
        definition = ""
        example = ""
        word = ""
        for j in range(len(temp)):
            if temp[j] == i.strip("\n") or temp[j] == (i.strip("\n")+"."):
                temp[j] = "****"
            definition += temp[j]+" "
        for k in range(len(temp2)): 
            if temp2[k] == i.strip("\n") or temp2[k] == (i.strip("\n")+"."):
                temp2[k] = "****"
            example += temp2[k]+" "
        for l in range(len(temp3)):
            if temp3[l] == i.strip("\n") or temp3[l] == (i.strip("\n")+"."):
                temp3[l] = "****"
            word += temp3[l]
        j = 0
        k = 0
        l = 0

    return (word, definition, example)


