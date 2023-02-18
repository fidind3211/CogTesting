from .nitrotesting import nitrotestingCog


def setup(bot):
    bot.add_cog(nitrotestingCog(bot))
