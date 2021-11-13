import argparse
import os
import sys
import clipper
from deckGenerator import generateDeck,splitSubs
from clipper import clipSub

def generateCode(name):
    code=""
    for i in name:
        code+=str(ord(i))
    return int(code[:10])

my_parser = argparse.ArgumentParser(prog="Ankiniser", description='Create an anki deck with your favourite Series.')
my_parser.add_argument('mode',metavar='mode', type=str,help='Mode you want to execute this program(all,deck,clip)')
my_parser.add_argument('mediaPath',metavar='mediaPath', type=str,help='Path of the video you want to convert')
my_parser.add_argument('subPath',metavar='subPath', type=str,help='Path of the subtitles you want to convert(must be .srt)')
my_parser.add_argument('name',metavar='name', type=str,help='Name of the deck you want to create')

args = my_parser.parse_args()

mode = args.mode

mediaPath = args.mediaPath
subPath = args.subPath
name = args.name

subs = splitSubs(subPath)
code = generateCode(name)

if(mode=="all"):
    print("Generating clips and deck...")
    clipSub(mediaPath,subs)
    generateDeck(subs,name,code)

elif(mode=="deck"):
    print("Generating deck...")
    generateDeck(subs,name,code)

elif(mode=="clip"):
    print("Generating clips")
    clipSub(mediaPath,subs)

else:
    print("Error:Mode {mode} does not exist!!!")
