# Ankiniser
A Python3 script to convert your favorite TV series into an Anki deck.
## How to install?
Download the script with git or download it manualy.

git clone https://github.com/Tarikhoza/Ankiniser

After downloading the script you have to install the requirements.
Install them with the following command in the root of project:
pip install -r requirements.txt
## How to run it?
You run the script with the command:

python Ankiniser.py all {VideoFilePath} {Subtitle file path} {Name of the deck}

Before you run this script please check if the subtitles fit the video you are trying to convert.

After the script has finished you have to copy the clips into the media.collection folder of your Anki user.

For now this program works only for japanese series, but it wont be that to implement it for other languages.
For this you would only have to change the LanguageAPI.py file.
