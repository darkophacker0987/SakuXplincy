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

@Client.on_message(command(["help"]) & filters.group & ~filters.edited)
async def helper(ok, message: Message):
    await message.reply_text(
        f"""💞 Hello! Following are the commands available for **{bn}** - __A Group Voice Chat Music Player__.
The commands I currently support are:

🔥 **Users Commands :**
⚜️ /play - **[ Groups Only ]** > __Plays the replied audio file or YouTube video through link.__
⚜️ /song - **[ Groups & DM ]** > __Uploads the searched song in the chat.__



🔰 **Admin & Sudo Users Commands :**
⚜️ /pause - **[Groups Only ]** > __Pause Voice Chat Music.__
⚜️ /resume - **[Groups Only ]** > __Resume Voice Chat Music.__
⚜️ /skip - **[Groups Only ]** > __Skips the current Music Playing In Voice Chat.__
⚜️ /stop - **[Groups Only ]** > __Clears The Queue as well as ends Voice Chat Music.__""")

        
