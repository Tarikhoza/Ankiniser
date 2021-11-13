from langAPI import getDictionary
import genanki
import os
import clipper
from clipper import toSec
import math
def splitSubs(subs):
    s=[]
    with open(subs,'r') as f:
        lines=f.readlines()
        for i in range(len(lines)):
            try:
                l={'index':lines[i]}
                l['from'],l['to']=lines[i+1].split('-->')
                text=[]
                while True:
                    if(lines[i+2]!="\n"):
                        text.append(lines[i+2])
                        i+=1
                        continue
                    break
                l['text']=text
                s.append(l)
            except Exception:
                pass
    return s


def generateDeck(primarySubs,name,code):
    print("Generating deck...")
    my_model = genanki.Model(
      code,
      name,
      fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'MyMedia'},
        {'name':'Words'},
        ],
      templates=[
        {
          'name': 'Video',
          'qfmt': '<p style="font-size:2em">{{Question}}</p><br><video width=400 src={{MyMedia}} autoplay controls></video>',
          'afmt': '{{FrontSide}}<hr><div style="font-size:1.5em">{{Words}}</div>',
        },
      ])

    my_deck = genanki.Deck(
      int(code),
      name
      )
    print("Found",len(primarySubs),"lines.")
    for index,i in enumerate(primarySubs):

        print(index,"of",len(primarySubs),"finished",end="\r")
        quest=str(i["index"])+".\n".join(i["text"])
        answer=""
        videoName=str(index+1)+".mp4".replace(" ","")
        d=getDictionary(i["text"])
        dd=""
        for j in d:
            dd+=j["word"]+":"+j["definition"]+"<br><br>"
        my_note = genanki.Note(
          model=my_model,
          fields=[quest, answer,videoName,dd]
          )
        my_deck.add_note(my_note)
    my_package = genanki.Package(my_deck)
    my_package.media_files =map(lambda x: os.path.join("clips",x),os.listdir("clips"))
    my_package.write_to_file(f'{name}.apkg')
    print(f"Generating deck finished.\nDeck saved in {name}.apkg")

#GenerateDeck("01.jap.srt","Death Note","123311123")
