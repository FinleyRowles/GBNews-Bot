import discord
from discord import app_commands
from discord.app_commands import Choice
import feedparser
import requests
from bs4 import BeautifulSoup
import json
import datetime

#Get Bot token
with open('token.txt', 'r') as tokenTxt:
    token = tokenTxt.read().strip()
tokenTxt.close()

#Configure Bot's Intents and Command Tree
client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

# On Start
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Britain's News Channel"))
    try:
        synced = await tree.sync()
        print(f"synced {len(synced)} commands of expected 3")
    except Exception as e:
        print(e)
    print('Bot is ready.')


#Latest command - Grabs latest News article from specified catagory and creates an embedded message for it
@tree.command(name="latest", description="Gets the latest news directly from GB News.")
@app_commands.choices(topic=[
    Choice(name='News', value="https://www.gbnews.com/feeds/news.rss"),
    Choice(name='Politics', value="https://www.gbnews.com/feeds/politics.rss"),
    Choice(name='Sport', value="https://www.gbnews.com/feeds/sport.rss"),
    Choice(name='Weather', value="https://www.gbnews.com/feeds/weather.rss"),
    Choice(name='Money', value="https://www.gbnews.com/feeds/money.rss"),
    Choice(name='Celebrity', value="https://www.gbnews.com/feeds/Celebrity.rss"),
    Choice(name='Royal', value="https://www.gbnews.com/feeds/Royal.rss"),
    Choice(name='Membership', value="https://www.gbnews.com/feeds/Membership.rss"),
])
async def latest(interaction: discord.Interaction, topic: Choice[str]):
    #Get latest entry on rss feed
    News = feedparser.parse((topic.value))
    entry = News.entries[0]
    response = requests.get(entry.link)
    
    #Scrape json of the news article for information
    soup = BeautifulSoup(response.content, 'html.parser')
    res = soup.find('script')
    json_object = json.loads(res.contents[0])

    og_data = {}
    for tag in soup.find_all('meta', property=lambda name: name):
        property_name = tag['property'].replace('og:', '')
        og_data[property_name] = tag['content']

    #Create a Discord embed for the article
    embed = discord.Embed(title=(entry.title), url=(entry.link), color=15548997, description=(og_data['description']))
    media = (entry.media_content)
    first = media[0]
    url = first["url"]
    embed.set_image(url=url)
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1571994202854100994/vYcqAgBG_400x400.jpg")

    #If the article is Members only, Indicate this in the Embed
    if "Membership" in (json_object['keywords']):
        embed.set_author(name=("Membership: " + og_data['article:section']))
    else:
        embed.set_author(name=(og_data['article:section']))

    #Include the time and date of publication
    time = datetime.datetime.fromisoformat((og_data['article:published_time']))
    embed.timestamp = time

    #Include the Author information where possible along with their photo (Not avalable on videos)
    try:
        embed.set_footer(text=("By "+(json_object['author'])['name']), icon_url=(((json_object['author'])['image'])['url']))
    except:
        embed.set_footer(text="Video")

    #Send created embed as a reply to the users command
    await interaction.response.send_message(embed=embed)

#Cammand for playing GB News "radio" in a users voice channel
@tree.command(name="radio", description="Starts playback of GB News Live Radio in your curent voice channel.")
async def latest(interaction: discord.Interaction):
    # Get the voice channel of the user
    if interaction.user.voice and interaction.user.voice.channel:
        channel = interaction.user.voice.channel
        # Connect to the voice channel
        voice_channel = await channel.connect()
        # Play the live radio
        voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source="https://listen-gbnews.sharp-stream.com/gbnews.mp3?=&&___cb=405128176981545"))
        await interaction.response.send_message("Playing GB News Radio in " + str(interaction.user.voice.channel))
    else:
        await interaction.response.send_message("You must be in a voice channel to use the /radio command!", ephemeral=True)

#Automatically disconnect from VC if nobody is present
@client.event
async def on_voice_state_update(member, before, after):
    if not member.bot:
        if before.channel is not None:
            if len(before.channel.members) == 1 and before.channel.members[0].bot:
                if before.channel.guild.voice_client is not None:
                    await before.channel.guild.voice_client.disconnect()

#Command to maually disonnect the bot from the voice channel
@tree.command(name="disconnect", description="Stops playback of GB News Radio in the current voice channel and disconnects the bot.")
async def disconnect(interaction: discord.Interaction):
    # Check if the bot is in a voice channel
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("Disconnected from the voice channel.")
    else:
        await interaction.response.send_message("The bot is not connected to a voice channel.", ephemeral=True)


client.run(token)
