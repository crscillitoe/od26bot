from __future__ import annotations
import logging
import datetime
import discord
import asyncio
from discord import Client, Intents
from config import Config

discord.utils.setup_logging(level=logging.INFO, root=True)

class RaffleBot(Client):
    def __init__(self):
        intents = Intents.default()
        intents.members = True
        intents.message_content = True
        intents.guilds = True

        super().__init__(intents=intents)

    async def on_ready(self):
        logging.info(f"[Discord] Logged in as {self.user} (ID: {self.user.id})")


    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.user:
            return

        # balls channel id
        if message.channel.id == 1000931265979101337:
            # we don't care about case.
            if message.content.lower() != "balls":
                # Mad.
                # ball-of-shame
                ball_of_shame = self.get_channel(1050601840254926928)
                await message.author.timeout(datetime.timedelta(minutes=5))
                await ball_of_shame.send(f"{message.author.mention} you a bitch stop trying to be quirky")
                await message.delete()


client = RaffleBot()
async def main():
    async with client:
        await client.start(Config.CONFIG["Discord"]["Token"])


if __name__ == "__main__":
    asyncio.run(main())