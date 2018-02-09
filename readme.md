It's simple telgram bot

connected to DialogFlow

To use you need
1 token for telegram
2 token for API Dialogflow

Change it in src/bot.py

base on https://habrahabr.ru/post/346606/


docker build -t mypybot .
docker run --rm -ti -d --name pybot mypybot

