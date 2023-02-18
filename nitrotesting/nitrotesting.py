import discord
from redbot.core import commands, Config

class nitrotestingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)  # use your own identifier here
        default_global = {"nitro_links": {}}
        self.config.register_global(**default_global)

    @commands.command()
    async def nitro(self, ctx, nitro_name: str):
        nitro_links = await self.config.nitro_links()
        if nitro_name not in nitro_links:
            await ctx.send(f"Invalid Nitro name '{nitro_name}'. Use !addnitro to add a new Nitro link.")
        else:
            await ctx.send(nitro_links[nitro_name]["url"])

    @commands.command()
    async def nitros(self, ctx):
        nitro_links = await self.config.nitro_links()
        if not nitro_links:
            await ctx.send("No Nitro links found. Use !addnitro to add a new Nitro link.")
        else:
            message = "Available Nitros:\n"
            for nitro_name, nitro_data in nitro_links.items():
                message += f"{nitro_name}: {nitro_data['url']}\n"
            await ctx.send(message)

    @commands.command()
    @commands.is_owner()
    async def addnitro(self, ctx, nitro_name: str, nitro_url: str):
        await self.config.nitro_links.set_raw(nitro_name, value={"url": nitro_url})
        await ctx.send(f"Added new Nitro link '{nitro_name}': {nitro_url}") 


def setup(bot):
    bot.add_cog(nitrotestingCog(bot))
