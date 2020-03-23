import requests
import json

site = "https://quotes.rest"

def getQuote():
    res = requests.get(site+"/qod")
    if res.status_code != 200:
        return "Error in connecting to quotes server! code: "+str(res.status_code)
    data = json.loads(res.text)
    return data['contents']['quotes'][0]['quote'] + "\n -" + data['contents']['quotes'][0]['author']

if __name__ == "__main__":
    print(getQuote())