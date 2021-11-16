from moviepy.editor import *
import os
import shutil

#convert time to seconds
def toSec(time):
    #00:00:01,290  hours:minutes:seconds
    time=time.replace(",",".").replace(" ","")
    hours,mins,sec=time.split(":")
    if(hours[0]=="0"):
        hours=hours[1:]
    if(mins[0]=="0"):
        mins=mins[1:]
    if(sec[0]=="0"):
        sec=sec[1:]
    sec=float(sec)+(float(mins)*60)
    sec+=(float(hours)*60*60)
    return sec


def clip(video,times):
    if("clips" in os.listdir()):
        shutil.rmtree("clips")
        print("Removed old clips")
    os.mkdir("clips")
    print(f"Clipping {video}...")
    print(len(times),"clips to clip...")
    for index,time in enumerate(times):
        print("Clipping",index+1, "of", len(times),"...",end="\r")
        clip =VideoFileClip(video)
        clip = clip.subclip(time[0],time[1]+0.5)
        clip.write_videofile(f"clips/{index+1}.mp4",logger=None)
    print("Clipping video finished!!!")
    print("Clips saved in clips folder")

def clipSub(video,subs):
    times=[]
    for i in subs:
        times.append((toSec(i["from"]),toSec(i["to"])))
    clip(video,times)

