import requests
import bs4
url="https://ichi.moe/cl/qr/?q={}&r=htr"
def getGloss(sentence):
    req=requests.get(url.format(sentence))
    soup=bs4.BeautifulSoup(req.text,"html.parser")
    return soup.find(class_="gloss-all")



def getDictionary(sentence):
    gloss=getGloss(sentence)
    try:
        meaningContainers=gloss.find_all(class_="gloss-content")
        meanings=[]
        for i in meaningContainers:
            container=i.find(class_="alternatives")
            if type(container)!=type(None):
                word=container.find("dt")
                defi=container.find("dd")
                meanings.append({
                        "word":word.text.replace("  ",""),
                        "definition":defi.text.replace("  ","")
                        }
                    )
    except Exception:
        return []

    return meanings
