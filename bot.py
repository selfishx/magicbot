# < (c) 2021 @Godmrunal >

import logging

from os import remove

import requests

from decouple import config

from telethon import Button, TelegramClient, events

logging.basicConfig(

    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO

)

bot = TelegramClient(None, api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e").start(

    bot_token=config("BOT_TOKEN")

)


logging.info("Starting bot...")


@bot.on(

    events.NewMessage(

        incoming=True, func=lambda e: not e.is_private))

async def mrunal(event):

    await event.delete()

    return

                

logging.info("\n\nBot has started.\n(c) @Godmrunal")

bot.run_until_disconnected()
