import discord
import random
from discord.ext import commands
from random import randint
from sql.jokes import sql_class

allowedChannels = [588354715625193473, 579538738988711958]


class jokes(commands.Cog, name='memery bullshit'):
    """
    Gregory is a dank memer :sunglasses:
    """
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return
        
        if "fuck" in message.content.lower():
            fBombs = message.content.lower().count("fuck")

            sql = sql_class()

            local_guild = message.guild
            sql.update_fuck_leaderboard(message.author.id, local_guild.id)
            
            if message.channel.id in allowedChannels:
                if fBombs == 1:
                    plural = "f-bomb"
                else:
                    plural = "f-bombs"
                await message.channel.send(f"**Hello!**\nI noticed you dropped **{fBombs} {plural}** in this comment. This might be necessary, but using nicer language makes the whole world a better place.\nMaybe you need to blow off some steam - in which case, go get a drink of water and come back later. This is just the internet and sometimes it can be helpful to cool down for a second.\n:hearts::hearts::hearts:")

    @commands.command(alias=["fLead", "fLeaderboard"])
    async def fuckLeaderboard(self, ctx):
        """
        Gets the leaderboard of fuck
        """ 
        sql = sql_class()

        local_guild = ctx.guild
        guild_name = local_guild.name
        
        leaderboard = sql.get_fuck_leaderboard(local_guild.id, 0, 10)

        msg = f'__F-bomb Leaderboard for **{guild_name}**:__'
        for record in leaderboard:
            msg = f"\n{msg} *{record[0]}*:\t{record[1]}"

        ctx.channel.send(msg)

    @commands.command(alias=['fuck', 'fuckCount'])
    async def getFuckCount(self, ctx, user:discord.Member=None):
        """
        Get's someone's fuck count
        """
        sql = sql_class()

        local_guild = ctx.guild

        if user == None:
            user = ctx.author

        user_ID = user.id
        guild_ID = local_guild.id

        fuckCount = sql.get_user_fuck(user_ID, guild_ID)[0]

        if fuckCount == 0:
            ctx.channel.send(f"Wow, {user.name} has **never** said the f-word! :sunglasses:")
        elif fuckCount < 100:
            ctx.channel.send(f"{user.name} has dropped **{fuckCount}** f-bombs on the server!")
        else:
            ctx.channel.send(f"Wow, {user.name} has dropped **{fuckCount}** f-bombs on the server!")








def setup(client):
    client.add_cog(jokes(client))