from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from RAJAmusic67 import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b61227af05544deb76a34.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐕1 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://files.catbox.moe/3uokvf.jpg")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://files.catbox.moe/8gai3w.jpg")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐕2 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/itzshukla/STRANGER-MUSIC/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://files.catbox.moe/8gai3w.jpg")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b61227af05544deb76a34.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐕1 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://files.catbox.moe/8gai3w.jpg")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://files.catbox.moe/8gai3w.jpg")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐕2 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/itzshukla/STRANGER-MUSIC/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://files.catbox.moe/8gai3w.jpg")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b61227af05544deb76a34.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐕1 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://files.catbox.moe/8gai3w.jpg")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐂ʜᴀᴛ 𝐁ᴏᴛ 𝐑ᴇᴘᴏ  🗡️", url=f"https://files.catbox.moe/8gai3w.jpg")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐕2 𝐌ᴜsɪᴄ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/itzshukla/STRANGER-MUSIC/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐒ᴘᴀᴍ  𝐑ᴇᴘᴏ 🗡️", url=f"https://files.catbox.moe/8gai3w.jpg")
                 ]
            ]
        ),
    )
