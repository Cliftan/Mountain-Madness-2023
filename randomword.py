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
        for l in range(len(temp3)):
            if i.strip("\n,.").lower() in temp2[k].lower():
                temp2A = ""
                for w in range(len(temp2[k])):
                    temp2A += "*"
                temp2[k] = temp2A
            word += temp2[k]+" "     

        j = 0
        k = 0
        l = 0

    return (word, definition, example)

