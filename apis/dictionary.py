import  requests

app_id = '7627ca63'
app_key = '22789842857e1100789673510060b8cb'
language = 'en'
baseUrl = 'https://od-api.oxforddictionaries.com:443/api/v2'
# word_id = 'Ace'

def define(word_id):
    url = baseUrl + '/entries/'  + language + '/'  + word_id.lower()
    # url Normalized frequency
    # urlFR = baseUrl + '/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()

    r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

    if r.status_code != 200:
        return "Dictionary API Error: Please try again later"

    data = r.json()
    # res = data['results'][0]['lexicalEntries']
    # category = data['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']
    # entries = data['results'][0]['lexicalEntries'][0]['entries'][0]
    # ety = data['results'][0]['lexicalEntries'][0]['entries'][0]['etymologies']
    senses = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']

    ans = ""

    ans += "Results from: " + data['metadata']['provider'] + "\n"
    # ans += "Etymology\n"
    # for x in ety:
        # ans += x + "\n"
    ans += "\n"
    for x in senses:
        ans += "Definition: " + x['definitions'][0] + "\n"
        if 'domains' in x.keys():
            ans += "Domain: " + x['domains'][0]['text'] + "\n"
        if 'examples' in x.keys():
            ans += "Example: " + x['examples'][0]['text'] + "\n"
        ans += "\n"
    return ans

if __name__ == "__main__":
    word = input("Enter word: ")
    print(define(word))