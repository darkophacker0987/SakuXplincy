import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c247284e8ddc50f01a314.png",
        caption=f"""**Hey Dear, I'm ﮩ٨ـﮩﮩ٨ـSaku♡Plincyﮩ٨ـﮩﮩ٨ـ bot🔥. I'm a Private bot for Moi master's Princess. So, don't add me in any group...search another bot🔥For cmds /help**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♥️Owner♥️", url=f"https://t.me/Officiallycute")
               ],
                [
                    InlineKeyboardButton(
                        "🔥Channel🔥", url=f"https://t.me/teamUltronX")
               ], 
                [
                    InlineKeyboardButton(
                        "🔱Developer🔱", url=f"https://t.me/TheUltronX")
               ],
                [
                    InlineKeyboardButton(
                        "💝Support💝", url=f"https://t.me/TeamUltronX")
                ]
                
           ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/c247284e8ddc50f01a314.png",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 Repo 💞", url=f"https://github.com/teamUltronX")
                ]
            ]
        ),
    )
