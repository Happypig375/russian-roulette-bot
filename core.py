from discord import app_commands, Embed, Interaction
from discord.ext.commands import Bot, Cog

from config import config


class Core(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print(f"Startup complete - logged in as {self.bot.user}")

    @app_commands.command()
    async def ping(self, interaction: Interaction):
        """Check the bot's latency."""
        await interaction.response.send_message(f"Pong! Latency is `{round(self.bot.latency * 1000)}ms`")

    @app_commands.command()
    async def invite(self, interaction: Interaction):
        """Get an invite link for the bot."""
        await interaction.response.send_message(f"Invite me to your server: {config.invite}")

    @app_commands.command()
    async def about(self, interaction: Interaction):
        """Show information about the bot."""
        with open('assets/markdown/about.md', 'r') as about_file:
            about = about_file.read()
        embed = Embed(title=config.name, description=about, color=config.color, url=config.url)
        await interaction.response.send_message(embed=embed)

    @app_commands.command()
    async def rules(self, interaction: Interaction):
        """Show the rules of the game."""
        with open('assets/markdown/rules.md', 'r') as rules_file:
            rules = rules_file.read()
        embed = Embed(title=f"{config.name} Rules", description=rules, color=config.color, url=config.url)
        await interaction.response.send_message(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Core(bot))
