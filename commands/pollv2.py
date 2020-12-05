import datetime
import discord
from discord.ext import commands
from converter.datetimeCalc import datetimeCal
from sql.pollv2 import sql_class



class poll(commands.Cog):
    '''
    super fancy shmancy poll command
    '''
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        """
        <RawReactionActionEvent 
        message_id=784823361476886540 
        user_id=771011111242956820 
        channel_id=784752699152269323 
        guild_id=784750381694713908 
        emoji=<PartialEmoji 
            animated=False 
            name='🇦' 
            id=None
            > 
        event_type='REACTION_ADD' 
        member=<Member 
            id=771011111242956820 
            name='Gregory' 
            discriminator='8659' 
            bot=True 
            nick=None 
            guild=<
                Guild id=784750381694713908
                name='gregory test server' 
                shard_id=None 
                chunked=True 
                member_count=7
                >
            >
        >
        """
        


    @commands.command(aliases=['poll2electricboogaloo','poll'])
    async def poll2(self, ctx, time: datetimeCal, *, args):
        """
        .poll2 7d2h {who do you want to vote lol?} [arg1] [arg2]
        """
        # fomatting of arguments in message
        args = args.split('[')
        name = args.pop(0)[1:]
        name = name[:name.find('}')]
        
        args = [arg[:arg.find(']')] for arg in args] # thanks ritz for this line

        if len(args) > 20:
            await ctx.send(f"bad {ctx.author.name}! thats too much polling >:(")
            return
        
        pollsigns = ["🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹","🇺","🇻","🇼","🇽","🇾","🇿"]

        # format
        description = ''
        for count in range(len(args)):
            description += pollsigns[count] + ' ' + args[count] + '\n\n'

        embed = discord.Embed(title=name,color=discord.Color.green(),description=description)

        # send poll
        message = await ctx.send(embed=embed)

        #add reactions
        for count in range(len(args)):
            await message.add_reaction(pollsigns[count])

        sql = sql_class()
        
        sql.add_poll(str(message.id), str(message.channel.id), str(message.author.guild.id), name, time, pollsigns, args)

    @commands.command()
    async def test(self, ctx, time: datetimeCal, name, *args):
        message = await ctx.send(name)
        print(message)
        pass


def setup(client):
    client.add_cog(poll(client))