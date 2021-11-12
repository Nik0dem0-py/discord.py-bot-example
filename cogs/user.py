import discord
from discord.ext import commands
from discord.ext.commands import bot

class User(commands.Cog):
    """
    User information
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog "Avatar" has been loaded')
    
    @commands.command(name="avatar", descritpion="Shows following member's profile picture", aliases=["av"])
    async def _avatar(self, ctx, member : commands.MemberConverter):
        """Shows following member's profile picture"""
        embed = discord.Embed(title = f"{member.name}'s profile picture", colour = discord.Colour.blue())
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(name="userinfo", descritpion="Shows information about the following member", aliases=['user'])
    async def info(self, ctx, member : commands.MemberConverter):
        """Shows information about the following member"""
       
        embed = discord.Embed(
            title=f"About {member.name}", 
            description = f"ID: `{member.id}`\n Name: `{member.name}#{member.discriminator}` \n Avatar URL: [click!]({member.avatar_url})", 
            colour = discord.Colour.blue())
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(User(bot))