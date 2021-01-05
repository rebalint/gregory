import pathlib

from discord.ext import commands
allowedChannels = [588354715625193473, 579538738988711958]


class fun(commands.Cog, name='fun'):
    """
    Gregory is a dank memer :sunglasses:
    """
    def __init__(self, client):
        self.client = client
        self.category = pathlib.Path(__file__).parent.absolute().name[4:]
        self.uwu_conversions = {}
        self.populate_uwu()

    def populate_uwu(self):
        self.uwu_conversions['the'] = 'da'
        self.uwu_conversions['The'] = 'Da'

        self.uwu_conversions['you'] = 'u'
        self.uwu_conversions['You'] = 'U'

        self.uwu_conversions['are'] = 'ish'
        self.uwu_conversions['Are'] = 'Ash'

        self.uwu_conversions['is'] = 'ish'
        self.uwu_conversions['Is'] = 'Ish'

        self.uwu_conversions['r'] = 'w'
        self.uwu_conversions['R'] = 'W'

        self.uwu_conversions['l'] = 'w'
        self.uwu_conversions['L'] = 'W'

    @commands.command(aliases=['uwu', 'uwuify', 'owo', 'owoify', 'owoifier'])
    async def uwuifier(self, ctx, *, message):
        """
        uwus your messages :3
        """
        for key, value in self.uwu_conversions.items():
            message = message.replace(key, value)
        await ctx.send(message)


def setup(client):
    client.add_cog(fun(client))
