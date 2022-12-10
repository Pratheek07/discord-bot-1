import discord
import json 
import os
import requests
import random
from alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix='&')

client.remove_command('help')

@client.event
async def on_ready():
  print('Logged in as {0}'.format(client.user))


def getjoke():
  response = requests.get('https://v2.jokeapi.dev/joke/Any?type=single')
  json_data = json.loads(response.text)
  joke = json_data.get('joke')
  return joke

def getquote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -"+ json_data[0]['a']
  return quote

def gettask():
  response = requests.get('https://www.boredapi.com/api/activity')
  json_data = json.loads(response.text)
  act = json_data.get('activity')
  return act


@client.command()
async def help(ctx):
  helpEmbed = discord.Embed(title="HELP!.",description='Helper Sees All , Knows All. \n\n Prefix : &\n\n',color=discord.Color.gold())
  helpEmbed.add_field(name='Moderation',value="`help`,`delete (del,remove)`,`test`")
  helpEmbed.add_field(name='Misc.',value="`hello`,`joke`,`time`,`task`,`quote`")
  await ctx.send(embed=helpEmbed)

@client.command()
async def test(ctx, *, arg):
    await ctx.send(arg)

@client.command(aliases=['del','remove'])
async def delete(ctx,amt=1):
  await ctx.channel.purge(limit=amt+1)

@client.event 
async def on_message(message):
  hello_responses=['Hi there','Howdy','Greetings','Hey, What’s up?','What’s going on?','Hey! There he is','How’s everything?','How are things?','Good to see you','Great to see you','Nice to see you','What’s happening','How’s it going?','Hey, boo','How are you?','Nice to meet you!','Long time no see','What’s the good word?','What’s new?','Look who it is!','How have you been?','Nice to see you again.','Greetings and salutations!','How are you doing today?','What have you been up to?','How are you feeling today?','Look what the cat dragged in!']
  if message.content.startswith('&hello') or message.content.startswith('&Hello') or message.content.startswith('&hi') or message.content.startswith('&hey'):
    await message.channel.send(random.choice(hello_responses))

  if message.content.startswith('&joke') or message.content.startswith('&Joke'):
    await message.channel.send(getjoke())

  if message.content.startswith('&quote') or message.content.startswith('&inspire'):
    await message.channel.send(getquote())

  if message.content.startswith('&task') or message.content.startswith('&Task'):
    await message.channel.send(gettask())
  
  await client.process_commands(message)


  
keep_alive()
client.run(os.environ['TOKEN'])