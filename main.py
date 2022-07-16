import tweepy
import discord

API_KEY = 'xxxxx'
API_SECRET_KET = 'xxxxx'

ACCESS_TOKEN = 'xxxxx'
ACCESS_TOKEN_SECRET = 'xxxxx'

tclient = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET_KET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

dclient = discord.Client()

@dclient.event
async def on_ready():
    print('logged in')

async def check_tweet(msg):
    global tclient
    tclient.create_tweet(text=f'{msg.content.replace("!tweet ", "")}')

    await msg.channel.send(f'{msg.author.mention} successfully tweeted *"{msg.content.replace("!tweet ", "")}"*.')

@dclient.event
async def on_message(msg: discord.Message):
    global tclient

    if msg.author == dclient.user:
        return
    
    if msg.content.startswith('!tweet '):

        if ('https://' in str(msg.content) or 'http://' in str(msg.content)):
            return

        if len(msg.content) - 6 > 200:
            await msg.channel.send('that message is too long')
        else:
            try:
                await check_tweet(msg)
            except Exception as e:
                print(e)
                tclient = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET_KET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
                await check_tweet(msg)

dclient.run('xxxxx')
