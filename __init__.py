from .nitro import NitroTesting


def setup(bot):
    bot.add_cog(NitroTesting(bot))