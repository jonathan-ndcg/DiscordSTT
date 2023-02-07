# DiscordSST

A Discord bot to transcribe conversations in a voice channel into a text channel.

https://user-images.githubusercontent.com/124545488/216897225-edf331ac-fb11-4c45-a5d3-3ae76973960a.mp4

## Built With

* Python
* [Pycord](https://github.com/Pycord-Development/pycord)
* [SpeechRecognition](https://github.com/Uberi/speech_recognition)

## Installation

1. Clone the repo and cd into the directory:

```sh
git clone https://github.com/jonathan-ndcg/DiscordSTT.git
cd DiscordSTT
```

2. Install dependencies:

```sh
pip install -r requirements.txt
```

3. Create a `.env` file in the root and enter your Discord bot token:

```dosini
TOKEN=
```

## Usage

1. Type the below command to run the bot: 

```sh
python src/bot.py
```

2. On Discord you must be in a voice channel. You can enter in a text channel the commands `/start` and `/stop`.
