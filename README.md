# Ankiniser
A Python3.8 script to convert your favorite TV series into an Anki deck.
## How to install?
Download the script with git or download it manualy.

git clone https://github.com/Tarikhoza/Ankiniser

After downloading the script you have to install the requirements.
Install them with the following command in the root of project:

pip install -r requirements.txt

## How to run it?
You run the script with the command:

python Ankiniser.py all {VideoFilePath} {SubtitleFilePath} {NameOfTheDeck}

The subtitles you are using should be in the target language you are learning.

Before you run this script please check if the subtitles fit the video you are trying to convert.

After the script has finished you have to copy the clips from the clips folder into the media.collection folder from your Anki user.

For now this script works only for japanese series, but it won't be that hard to make it work for other languages.
For this you would only have to change the langAPI.py file.
