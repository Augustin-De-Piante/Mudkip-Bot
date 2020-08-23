 
import discord
import asyncio
import aiohttp
import json
from discord.ext.commands import Bot
from random import randint
from discord.ext import commands
from platform import python_version
import os
import platform
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


BOT_PREFIX = ('YOUR_BOT_PREFIX_HERE')
OWNERS = [YOUR_DISCORD_ID_HERE]
BLACKLIST = []
client = Bot(command_prefix=BOT_PREFIX)





async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("with you!"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("with Doge_Stig!"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("YOUR_BOT_PREFIX_HEREhelp"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("with humans!"))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    client.loop.create_task(status_task())
    print('Logged in as ' + client.user.name)
    print("Discord.py API version:", discord.__version__)
    print("Python version:", platform.python_version())
    print("Running on:", platform.system(), platform.release(), "(" + os.name + ")")
    print('-------------------')

@client.command(name='info', pass_context=True)
async def info(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        e = discord.Embed(description='Used Krypons template', color=0xF4D4F4)
        e.set_author(name="Bot Informations")
        e.add_field(name="Owner:", value="doge_stig#9159", inline=True)
        e.add_field(name="Python Version:", value="{0}".format(python_version()), inline=True)
        e.add_field(name="Prefix:", value="$", inline=False)
        e.set_footer(text="Requested by {0}".format(context.message.author))
        await context.message.channel.send(embed=e)

@client.command(name='serverinfo', pass_context=True)
async def serverinfo(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        server = context.message.guild
        roles = [x.name for x in server.roles]
        role_length = len(roles)
        if role_length > 50:
            roles = roles[:50]
            roles.append('>>>> Displaying[50/%s] Roles' % len(roles))
        roles = ', '.join(roles)
        channelz = len(server.channels)
        time = str(server.created_at)
        time = time.split(' ')
        time = time[0]
        embed = discord.Embed(description='%s ' % (str(server)), title='**Server Name:**', color=0xF4D4F4)
        embed.set_thumbnail(url=server.icon_url)
        embed.add_field(name='__Owner__', value=str(server.owner) + '\n' + str(server.owner.id))
        embed.add_field(name='__Server ID__', value=str(server.id))
        embed.add_field(name='__Member Count__', value=str(server.member_count))
        embed.add_field(name='__Text/Voice Channels__', value=str(channelz))
        embed.add_field(name='__Roles (%s)__' % str(role_length), value=roles)
        embed.set_footer(text='Created at: %s' % time)
        await context.message.channel.send(embed=embed)

    
@client.command(name='ping', pass_context=True)
async def ping(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        embed = discord.Embed(color=0xF4D4F4)
        embed.set_footer(text='Pong request by {0}'.format(context.message.author))
        embed.add_field(name='Pong!', value=':ping_pong:',  inline=True)
        await context.message.channel.send(embed=embed)

@client.command(name='invite', pass_context=True)
async def invite(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        await context.message.channel.send('I sent you a private message!')
        await context.message.channel.send('Invite me by clicking here: https://discordapp.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot&permissions=8')


@client.command(name='server', pass_context=True)
async def server(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        await context.message.channel.send('I sent you a private message!')
        await context.message.channel.send('Join my discord server by clicking here: https://discord.gg/Vddcy76')

@client.command(name='poll', pass_context=True)
async def poll(context, *args):
    mesg = ' '.join(args)
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        await context.message.delete()
        embed = discord.Embed(title='We have a poll !', description='{0}'.format(mesg), color=0xF4D4F4)
        embed.set_footer(text='Poll created by: {0} • React to vote!'.format(context.message.author))
        embed_message = await context.message.channel.send(embed=embed)
        await embed_message.add_reaction('✅')
        await embed_message.add_reaction('❎')

@client.command(name='8ball', pass_context=True)
async def eight_ball(context, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.',
                   'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
                   'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
                   'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.',
                   'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
        embed = discord.Embed(title='**My Answer:** ', description='{0}'.format(answers[randint(0, len(answers))]), color=0xF4D4F4)
        embed.set_footer(text='Question asked by: {0} • Ask your own now!'.format(context.message.author))
        await context.message.channel.send(embed=embed)


@client.command(name='template', pass_context=True)
async def template(context, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title='**Command Template:** ',
            description="This was supposed to be secret... Nice detective work.\n\nThis is an easy template for me to make more commands",
            color=0xFFFFFF)
        
        embed.set_thumbnail(url = 'https://64.media.tumblr.com/bc67771ee387788a62fbf2bbc27f4acb/tumblr_n4nkl3cgd71r0m95co3_250.gif')
        embed.set_image (url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/-Insert_image_here-.svg/640px--Insert_image_here-.svg.png')
        embed.add_field(name = 'Blank Field', value = 'Field Value', inline=True)
        embed.add_field(name = 'Blank Field', value = 'Field Value', inline=True)
        embed.set_footer(text='Secret requested by: {0} • Calling the police!'.format(context.message.author))
        await context.message.channel.send(embed=embed)
        

@client.command(name='bincon', pass_context=True)
async def bincon(context, inputstringbin, *args):
    integerinputstringbin=int(inputstringbin)
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        binary=bin(int(inputstringbin.strip()))[2:]
        embed=discord.Embed(title='Decimal Converted to Binary',
                            description=f"Decimal Input: **{inputstringbin}** \n\n Binary Output: **{binary}**",
                            color=0xF4D4F4)
        embed.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/commons/5/58/BinaryData50.png')
        embed.set_image(url = 'https://programminghq.files.wordpress.com/2013/05/binary-code-big.jpg')
        await context.message.channel.send(embed=embed)    


@client.command(name='hexcon', pass_context=True)
async def hexcon(context, inputstringhex, *args):
    integerinputstringhex=int(inputstringhex)
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        hexa=hex(int(inputstringhex.strip()))[2:]
        embed=discord.Embed(title='Decimal Converted to Hex',
                            description=f"Decimal Input: **{inputstringhex}** \n\n Hexadecimal Output: **{hexa}**",
                            color=0xF4D4F4)
        embed.set_thumbnail(url = 'http://3.bp.blogspot.com/-2OIxuVu7SZs/UlwTxrHSq_I/AAAAAAAABfc/s_yCWsrvciY/s1600/htmlcolorcode.jpg')
        embed.set_image(url = 'https://www.lifewire.com/thmb/1DSrn9QZgHMDcRvaqSpsL4p-X5g=/1280x860/filters:fill(auto,1)/173580191-56a6f9b85f9b58b7d0e5cb75.jpg')
        await context.message.channel.send(embed=embed)


@client.command(name='sysbot', pass_context=True)
async def sysbot(context, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title='**SysBot FAQ:** ',
            description="This guide will define what a SysBot is, and how to use one. One does not currently exist on this server, but one day I hope it will. ~~donate lol~~\n\n",
            color=0xF4D4F4)
        
        embed.set_thumbnail(url = 'https://64.media.tumblr.com/bc67771ee387788a62fbf2bbc27f4acb/tumblr_n4nkl3cgd71r0m95co3_250.gif')
        embed.set_image (url = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/237/robot-face_1f916.png')
        embed.add_field(name = '**__Question:__** What is a sysbot anyways?', value = 'Answer: a SysBot is a hacked switch someone has generously set up to generate and distribute generated (genned) Pokémon via Link Trade.', inline=False)
        embed.add_field(name = '**__Question:__** Can I use these Pokémon?', value = 'Answer: Anything you can recieve via the bot has already passed Nintendo\'s legality checks and can be used online. __However__, it is incredibly risky to use them in such a fashion, especially with online competitive tournaments. Do so at your own risk, and using them to gain an unfair advantage over other players is highly ill-advised.', inline=False)
        embed.add_field(name = '**__Question:__** Legal? What does that mean?', value = 'Answer: Pokémon Legality can be broken down into 3 categories, Legitimate, Legal, and Illegal.\n\n**Legitimate:** Pokémon obtained on any normal playthrough of the game.\n\n**Legal:** Pokémon that **could** be obtained n any normal playthrough of the game.\n\n**Illegal:** Pokémon than **__CANNOT__** be obtained, whether it be impossible moves, abilities, or shininess.', inline=False)
        embed.add_field(name = '**__Question:__** So how do I gen my own Pokémon?', value = 'Answer: In a bot channel (again, none exist in this server yet, I dont own a hackable switch) send the command that usually is the word trade with a prefix, followed by a Showdown Format, or a .pk8 file', inline=False)
        embed.add_field(name = '**__Question:__** What happens after I send <prefix>trade to the bot channel?', value = 'Answer: The bot will add you to a queue, where you will be notified of your position in line. When it is your turn, the bot will DM you a Link Trade Code for your Sword/Shield game. Please have your internet connected and be on the screen to type in your code as soon as your turn approaches. If you are not on time, the bot will not be able to find you or it will cancel the trade on you.', inline=False)
        embed.add_field(name = '**__Question:__** What is Showdown format?', value = 'Answer: Showdown Format is obtained by using the team builder on https://play.pokemonshowdown.com/teambuilder. A properly formatted Pokémon will look like this:\n```Cinderace-Gmax (M) @ Expert Belt\nAbility: Libero\nShiny: Yes\nGigantamax: Yes\nEVs: 252 Atk / 4 SpD / 252 Spe\nJolly Nature\n- High Jump Kick\n- Pyro Ball\n- Zen Headbutt\n- Iron Head```', inline=False)
        embed.add_field(name = '**__Question:__** What is PKHeX?', value = 'Answer: PKHeX is a Windows only program that allows far greater customization for genned Pokémon. It can be found here: https://projectpokemon.org/home/files/file/1-pkhex/.', inline=False)
        embed.add_field(name = '**__Question:__** Can I get my own Trainer name and ID number on a genned Pokémon?', value = 'Answer: Yes, you can set OT, TID, and SID in PKHeX', inline=False)
        embed.add_field(name = '**__Question:__** What is SID and how can I find it?', value = 'Answer: SID is a Secret ID number, that is paired with your TID to make a Pokémon uniquely yours. You can find your SID by catching any wild Pokémon and trading it with a SysBot. The Bot will DM you the file of whatever you traded it, and your SID can be found using PKHeX.', inline=False)
        embed.add_field(name = '**__Question:__** What if I can\'t use PKHeX? (Mac/Chromebook users)', value = 'Answer: Look into a Virtual Machine, Bootcamp on Mac, or a Remote Desktop Service. Lots of educational institutions offer these resources especially if you are in university. If there is absolutely no way for you to obtain PKHeX, you may make 1 request per 24 hours in #pk8-requests.', inline=False)
        embed.set_footer(text='Guide requested by: {0} • Get your own now!'.format(context.message.author))
        await context.message.channel.send(embed=embed)       
       
        
@client.command(name='rerolling', pass_context=True)
async def rerolling(context, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title='**Rolling a New Pokemon in you Shiny Den:** ',
            description='**Step 1:**\nIf you haven\'t already, collect the Watts. Enter the lobby of your raid.\n\n**Step 2:**\nClick `Invite Others`.\n\n**Step 3:**\nPress the `Home` button on your Joy-Con.\n\n**Step 4:**\nSelect `Settings`, and scroll all the way to the bottom to find `System Settings`.\n\n**Step 5:**\nInside of `System Settings`, select `Date and Time`, then the bottom option to change your date.\n\n**Step 6:**\nAdvance the date one day forward, and pres `OK` to save your changes.\n\n **Step 7:**\nPress the `Home` button twice to re-enter your game.\n\n**Step 8:**\nPress `B` to stop looking for others, and then `A` to confirm you want to leave the lobby.\n\n**Step 9:**\nRepeat this process for a total  of 3 day skips. You are now on your shiny frame.\n\n**Step 10:**\nIf the Pokémon is the one you want, you may now host it. If you would like to change it, close your game **__without__** saving, and repeat from Step 1.',
            color=0xFFFFFF)
        
        embed.set_thumbnail(url = 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/whatsapp/186/sparkles_2728.png')
        embed.set_image (url = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8ab6bd4f-1408-4c7b-bdd7-4c007e69aead/ddawhhx-2e3803df-becd-4f79-acb0-d5a36e5feddb.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvOGFiNmJkNGYtMTQwOC00YzdiLWJkZDctNGMwMDdlNjlhZWFkXC9kZGF3aGh4LTJlMzgwM2RmLWJlY2QtNGY3OS1hY2IwLWQ1YTM2ZTVmZWRkYi5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.VPz1FJ8drlRavceV2-wAlItYRCHCtazVesRRkzTEZ8c')
        embed.set_footer(text='Guide requested by: {0} • Get your own now!'.format(context.message.author))
        await context.message.channel.send(embed=embed) 
 
 
@client.command(name='raid101', pass_context=True)
async def raid_101(context, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        embed = discord.Embed(
            title='**Joining a Shiny Raid:** ',
            description="**Step 1:**\nRead the host's rules.\n\n**Step 2:**\nAdd the host's Friend Code to your Switch Friend List.\n\n**Step 3:**\nOpen your game, and connect to the internet via Y-Comm.\n\n**Step 4:**\nPress Y to refresh your stamps, and when your host's stamp pops up, press A to join the raid. You will need to be fast!\n\n**Step 5:**\nGood luck!",
            color=0x0000FF)
        
        embed.set_thumbnail (url = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Flh4.ggpht.com%2F_oxFWKI8LhNE%2FSvhEVnLhJUI%2FAAAAAAAAA44%2F7GycIHt-oPU%2Fs1280%2FBeam%2520of%2520Light%2520shinning%2520down%2520(Pink%2520wallpaper).jpg&f=1&nofb=1')
        embed.set_image (url = 'https://cdn.bulbagarden.net/upload/thumb/6/69/Sword_Shield_Max_Raid_Battle_artwork.png/424px-Sword_Shield_Max_Raid_Battle_artwork.png')
        embed.add_field (name = '**__IMPORTANT__**', value = 'You *MUST* delete your host from your Friends List when you are finished raiding. This is a simple courtesy to fulfill, and makes hosting infinitely more enjoyable. Re-pay your host with this favor!', inline = True)
        embed.set_footer(text='Guide requested by: {0} • Get your own now!'.format(context.message.author))
        await context.message.channel.send(embed=embed)    
        
        
@client.command(pass_context=True)
async def bitcoin(context):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed = discord.Embed(title=':information_source: Info',
                              description='Bitcoin price is: $' + response['bpi']['USD']['rate'], color=0xF4D4F4)
        await context.message.channel.send(embed=embed)


@client.command(name='shutdown', pass_context=True)
async def shutdown(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.id in OWNERS:
            embed = discord.Embed(title='Shutdown!', description='Shutting down. Bye! :wave:', color=0xF4D4F4)
            await context.message.channel.send(embed=embed)
            await client.logout()
            await client.close()
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
                                  color=0xF4D4F4)
            await context.message.channel.send(embed=embed)


@client.command(name='say', pass_context=True)
async def echo(context, *, content):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.id in OWNERS:
            await context.message.delete()
            await context.message.channel.send(content)
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.', color=0xF4D4F4)
            await context.message.channel.send(embed=embed)

@client.command(name='embed', pass_context=True)
async def embed(context, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.id in OWNERS:
            mesg = ' '.join(args)
            embed = discord.Embed(description=mesg, color=0xF4D4F4)
            await context.message.channel.send(embed=embed)
            await context.message.delete()
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
                                  color=0xF4D4F4)
            await context.message.channel.send(embed=embed)


@client.command(name='kick', pass_context=True)
async def kick(context, member: discord.Member, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.kick_members:
            if member.guild_permissions.administrator:
                embed = discord.Embed(title='Error!', description='User has Admin permissions.', color=0xF4D4F4)
                await context.message.channel.send(embed=embed)
            else:
                mesg = ' '.join(args)
                embed = discord.Embed(title='User Kicked!', description='**{0}** was kicked by **{1}**!'.format(member,
                                                                                                                context.message.author),
                                      color=0xF4D4F4)
                embed.add_field(name='Reason:', value=mesg)
                await context.message.channel.send(embed=embed)
                await context.message.delete()
                await member.send('You where warned by **{0}**!  '.format(context.message.author) + 'Reason: {0}'.format(mesg))
                await member.kick()
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
                                  color=0xF4D4F4)
            await context.message.channel.send(embed=embed)

@client.command(name='nick', pass_context=True)
async def nick(context, member: discord.Member, *, name : str):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            if name.lower() == "!reset":
                name = None
            embed = discord.Embed(title='Changed Nickname!', description='**{0}** new nickname is **{1}**!'.format(member, name), color=0xF4D4F4)
            await context.message.channel.send(embed=embed)
            await context.message.delete()
            await member.edit(nick=name)
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.', color=0xF4D4F4)
            await context.message.channel.send(embed=embed)

@client.command(name='ban', pass_context=True)
async def ban(context, member: discord.Member, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            if member.guild_permissions.administrator:
                embed = discord.Embed(title='Error!', description='User has Admin permissions.', color=0xF4D4F4)
                await context.message.channel.send(embed=embed)
            else:
                mesg = ' '.join(args)
                embed = discord.Embed(title='User Banned!', description='**{0}** was banned by **{1}**!'.format(member,
                                                                                                                context.message.author),
                                      color=0xF4D4F4)
                embed.add_field(name='Reason:', value=mesg)
                await context.message.channel.send(embed=embed)
                await context.message.delete()
                await member.send('You were banned by **{0}**!'.format(
                    context.message.author) + 'Reason: {0}'.format(mesg))
                await member.ban()
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
                                  color=0xF4D4F4)
            await context.message.channel.send(embed=embed)


@client.command(name='unban', pass_context=True)
async def unban(context, user: discord.Member):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            embed = discord.Embed(title='User Unbanned!',
                                  description='**{0}** was unbanned by **{1}**!'.format(user, context.message.author),
                                  color=0xF4D4F4)
            await context.message.channel.send(embed=embed)
            await context.message.delete()
            await user.send('You were unbanned by **{0}**!  '.format(context.message.author) + 'Reason: Ban revoked')
            await user.unban()
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
                                  color=0xF4D4F4)
            await context.message.channel.send(embed=embed)


@client.command(name='warn', pass_context=True)
async def warn(context, member: discord.Member, *args):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            mesg = ' '.join(args)
            embed = discord.Embed(title='User Warned!',
                                  description='**{0}** was warned by **{1}**!'.format(member, context.message.author),
                                  color=0xF4D4F4)
            embed.add_field(name='Reason:', value=mesg)
            await context.message.channel.send(embed=embed)
            await context.message.delete()
            await member.send('You were warned by **{0}**!  '.format(
                context.message.author) + 'Reason: {0}'.format(mesg))
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
                                  color=0xF4D4F4)
            await context.message.channel.send(embed=embed)


@client.command(name='purge', pass_context=True)
async def purge(context, number):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.guild_permissions.administrator:
            number = int(number)
            await context.message.channel.purge(limit=number)
            embed = discord.Embed(title='Chat Cleared!',
                                  description='**{0}** cleared **{1}** messages!'.format(context.message.author,
                                                                                         number), color=0xF4D4F4)
            message = await context.message.channel.send(embed=embed)
            await asyncio.sleep(3)
            await message.delete()
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
                                  color=0xF4D4F4)
            await context.message.channel.send(embed=embed)

@client.command(name='blacklist', pass_context=True)
async def blacklist(context, mode : str, user : discord.User = None):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!',
                              description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        if context.message.author.id in OWNERS:
            if (mode.lower() == "add"):
                userID = user.id
                try:
                    BLACKLIST.append(userID)
                    embed = discord.Embed(title="User Blacklisted", description='**{0}** has been successfully added to the blacklist'.format(user.name), color=0xF4D4F4)
                    embed.set_footer(text='There are now {0} users in the blacklist'.format(len(BLACKLIST)))
                    await context.message.channel.send(embed=embed)
                except:
                    embed = discord.Embed(title=":x: Error!", description="An unknown error occurred when trying to add **{0}** to the blacklist.".format(user.name), color=0xFF0000)
                    await context.message.channel.send(embed=embed)
            elif (mode.lower() == "remove"):
                userID = user.id
                try:
                    BLACKLIST.remove(userID)
                    embed = discord.Embed(title="User Unblacklisted",
                                          description='**{0}** has been successfully removed from the blacklist'.format(
                                              user.name), color=0xF4D4F4)
                    embed.set_footer(text='There are now {0} users in the blacklist'.format(len(BLACKLIST)))
                    await context.message.channel.send(embed=embed)
                except:
                    embed = discord.Embed(title=":x: Error!",
                                          description="An unknown error occurred when trying to remove **{0}** from the blacklist.\nAre you sure the user is in the blacklist?".format(
                                              user.name), color=0xFF0000)
                    await context.message.channel.send(embed=embed)
            elif (mode.lower() == "list"):
                embed = discord.Embed(title="There are currently {0} blacklisted IDs".format(len(BLACKLIST)),
                                      description="{0}".format(BLACKLIST),
                                      color=0xF4D4F4)
                await context.message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title='Error!', description='You don\'t have the permission to use this command.',
                                  color=0xFF0000)
            await context.message.channel.send(embed=embed)

client.remove_command('help')

@client.command(name='help', description='Help HUD.', brief='HELPOOOO!!!', pass_context=True)
async def help(context):
    if context.message.author.id in BLACKLIST:
        embed = discord.Embed(title='You\'re blacklisted!', description='Ask the owner to remove from the list if it was unfair.', color=0xF4D4F4)
        await context.message.channel.send(embed=embed)
    else:
        # Note that commands made only for the owner of the bot are not listed here.
        embed = discord.Embed(title='Bot', description='List of commands are:', color=0xF4D4F4)
        embed.add_field(name='Invite - Invite the bot.', value='Usage: $invite', inline=False)
        embed.add_field(name='Server - Join my own server.', value='Usage: $server', inline=False)
        embed.add_field(name='Poll - Create a poll for your users.', value='Usage: $poll <idea>', inline=False)
        embed.add_field(name='8Ball - Answers to your questions.', value='Usage: $8ball <question>', inline=False)
        embed.add_field(name='Bitcoin - Shows the currency of the bitcoin.', value='Usage: $bitcoin', inline=False)
        embed.add_field(name='Info - Gives infos about the bot.', value='Usage: $info', inline=False)
        embed.add_field(name='Shutdown - Shutdowns the bot [OWNER].', value='Usage: $shutdown', inline=False)
        embed.add_field(name='Say - I send a message of your choice [OWNER].', value='Usage: $say <message>', inline=False)
        embed.add_field(name='Embed - I send a embed message of your choice [OWNER].', value='Usage: $embed <message>', inline=False)
        embed.add_field(name='Kick - Kick a user.', value='Usage: $kick <user> <reason>', inline=False)
        embed.add_field(name='Ban - Ban a user.', value='Usage: $ban <user> <reason>', inline=False)
        embed.add_field(name='Warn - Warn a user in private messages.', value='Usage: $warn <user> <reason>', inline=False)
        embed.add_field(name='Unban - Unban a user.', value='Usage: $unban <user>', inline=False)
        embed.add_field(name='Purge - Remove an amount of messages', value='Usage: $purge <number>', inline=False)
        embed.add_field(name='Raid101 - Details how to join Y-Comm Raids.', value='Usage: $raid101', inline=False)
        embed.add_field(name='SysBot - Guide to using a SysBot, in FAQ format.', value='Usage: $sysbot', inline=False)
        embed.add_field(name='Re-Rolling - Detailed instructions for re-rolling a shiny den.', value='Usage: $rerolling', inline=False)
        embed.add_field(name='Help - Gives this menu', value='Usage: $help', inline=False)
        await context.message.channel.send(embed=embed)

@client.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandOnCooldown):
        await context.message.delete()
        embed = discord.Embed(title="Error!", description='This command is on a %.2fs cooldown' % error.retry_after, color=0xF4D4F4)
        message = await context.message.channel.send(embed=embed)
        await asyncio.sleep(5)
        await message.delete()
    raise error

@blacklist.error
async def blacklist_error(context, error):
    embed = discord.Embed(title='**Command:** $blacklist', description='**Description::** Prevents a user from using the bot \n **Usage:** $blacklist [add/remove/list] [user] \n **Example:** $blacklist add @RandomUser', color=0xF4D4F4)
    await context.message.channel.send(embed=embed)

@ban.error
async def ban_error(context, error):
    embed = discord.Embed(title='**Command:** $ban', description='**Description:** Bans a member \n **Usage:** $ban [user] [reason] \n **Example:** $ban @RandomUser Get out!', color=0xF4D4F4)
    await context.message.channel.send(embed=embed)

@poll.error
async def poll_error(context, error):
    embed = discord.Embed(title='**Command:** $poll', description='**Description:** Create a pool to vote \n **Usage:** $poll [idea] \n **Example:** $poll Add new emojis!', color=0xF4D4F4)
    await context.message.channel.send(embed=embed)

@eight_ball.error
async def eight_ball_error(context, error):
    embed = discord.Embed(title='**Command:** $8ball', description='**Description:** Get an answer to all of your questions \n **Usage:** $8ball [question] \n **Example:** $8ball Is this bot cool?', color=0xF4D4F4)
    await context.message.channel.send(embed=embed)

@echo.error
async def say_error(context, error):
    embed = discord.Embed(title='**Command:** $say',
                          description='**Description:** I say what you say \n **Usage:** $say [message] \n **Example:** $say Hello!!',
                          color=0xF4D4F4)
    await context.message.channel.send(embed=embed)


@embed.error
async def embed_error(context, error):
    embed = discord.Embed(title='**Command:** $embed',
                          description='**Description:** I say what you say as embed message \n **Usage:** $embed [message] \n **Example:** $embed Hello!!',
                          color=0xF4D4F4)
    await context.message.channel.send(embed=embed)


@kick.error
async def kick_error(context, error):
    embed = discord.Embed(title='**Command:** $kick',
                          description='**Description:** Kicks a member \n **Usage:** $kick [user] [reason] \n **Example:** $kick @RandomUser Rejoin when you\'ll be smarter, like me!',
                          color=0xF4D4F4)
    await context.message.channel.send(embed=embed)


@unban.error
async def unban_error(context, error):
    embed = discord.Embed(title='**Command:** $unban',
                          description='**Description:** Unbans a member \n **Usage:** $unban [user] \n **Example:** $unban @RandomUser',
                          color=0xF4D4F4)
    await context.message.channel.send(embed=embed)

@warn.error
async def warn_error(context, error):
    embed = discord.Embed(title='**Command:** $warn',
                          description='**Description:** Warns a member \n **Usage:** $warn [user] [reason] \n **Example:** $warn @RandomUser Stop the caps, thanks!',
                          color=0xF4D4F4)
    await context.message.channel.send(embed=embed)


@purge.error
async def purge_error(context, error):
    embed = discord.Embed(title='**Command:** $purge',
                          description='**Description:** Delete a certain amount of messages \n **Usage:** $purge [numer of messages] \n **Example:** $purge 20',
                          color=0xF4D4F4)
    await context.message.channel.send(embed=embed)

client.run(TOKEN)

