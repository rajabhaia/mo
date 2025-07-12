import time
import random
import asyncio # For adding delays between messages
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from RAJAmusic67 import app
from RAJAmusic67.misc import _boot_
from RAJAmusic67.plugins.sudo.sudoers import sudoers_list
from RAJAmusic67.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from RAJAmusic67.utils.decorators.language import LanguageStart
from RAJAmusic67.utils.formatters import get_readable_time
from RAJAmusic67.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

# List of image URLs for random selection
YUMI_PICS = [
    "https://telegra.ph/file/3ed81ef4e352a691fb0b4.jpg",
    "https://telegra.ph/file/3134ed3b57eb051b8c363.jpg",
    "https://telegra.ph/file/6ca0813b719b6ade1c250.jpg",
    "https://telegra.ph/file/5a2cbb9deb62ba4b122e4.jpg",
    "https://telegra.ph/file/cb09d52a9555883eb0f61.jpg"
]

# Placeholder for animated sticker file IDs.
# IMPORTANT: Replace these with actual file IDs of animated stickers you want to use.
# You can get sticker file IDs by sending a sticker to a bot like @StickerFileIdBot
ANIMATED_STICKERS = [
    "CAACAgIAAxkBAAEF_CFlrQhL9oY7Wd-b8jP_e2Xg-94AAgYAAzHh2hKx07o_9rW_zDQE", # Example sticker ID (replace with yours)
    "CAACAgIAAxkBAAEF_CFlrQhL9oY7Wd-b8jP_e2Xg-94AAgYAAzHh2hKx07o_9rW_zDQE", # Add more sticker IDs here
    "CAACAgIAAxkBAAEF_CFlrQhL9oY7Wd-b8jP_e2Xg-94AAgYAAzHh2hKx07o_9rW_zDQE", # Make sure they are actual animated stickers
]


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    """
    Handles the /start command in private chats.
    Includes animated sticker, dynamic messages, and special greetings.
    """
    await add_served_user(message.from_user.id)

    # --- START: Loading Animation ---
    baby = await message.reply_text(f"sᴛᴧʀᴛɪηɢ.❤️‍🔥")
    await asyncio.sleep(0.3)
    await baby.edit_text(f"sᴛᴧʀᴛɪηɢ..❤️‍🔥")
    await asyncio.sleep(0.3)
    await baby.edit_text(f"sᴛᴧʀᴛɪηɢ...❤️‍🔥")
    await asyncio.sleep(0.3)
    await baby.edit_text(f"sᴛᴧʀᴛɪηɢ....❤️‍🔥")
    await asyncio.sleep(0.3)
    await baby.edit_text(f"sᴛᴧʀᴛɪηɢ.....❤️‍🔥")
    await asyncio.sleep(0.5) # A bit longer pause before next action
    await baby.delete() # Delete the loading message after animation
    # --- END: Loading Animation ---

    # Send a random animated sticker for a stylish start
    if ANIMATED_STICKERS:
        await message.reply_sticker(random.choice(ANIMATED_STICKERS))
        await asyncio.sleep(1.5) # Small delay for effect

    # Dynamic welcome messages
    await message.reply_text(
        f"👋 **Hey there, {message.from_user.mention}!**\n"
        f"I'm {app.mention}, your ultimate music companion. ✨"
    )
    await asyncio.sleep(1)

    # Incorporate the special RAJA BHAI message
    await message.reply_text(
        "**RAJA BHAI Special Message:**\n"
        "😎𝗣𝗔𝗛𝗟𝗘 𓆩 𝗥𝗔𝗝𝗔 𝗕𝗛𝗔𝗜 𓆪 𝗞𝗢 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗝𝗔𝗞𝗘 😆😆\n\n"
        "Let's make some noise with your favorite tunes!"
    )
    await asyncio.sleep(1)


    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_photo(
                photo=config.START_IMG_URL,
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        # Final message with photo and inline keyboard
        out = private_panel(_)
        await message.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    """
    Handles the /start command in group chats.
    """
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    """
    Handles new chat members, including bot's own addition to a group.
    Includes animated sticker and dynamic welcome messages for the bot.
    """
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                # Send a random animated sticker when bot joins
                if ANIMATED_STICKERS:
                    await message.reply_sticker(random.choice(ANIMATED_STICKERS))
                    await asyncio.sleep(1.5) # Small delay for effect

                # Dynamic welcome messages for the bot itself
                await message.reply_text(
                    f"🎉 **Hello everyone!**\n"
                    f"I'm {app.mention}, ready to rock this group with amazing music! 🎶"
                )
                await asyncio.sleep(1)

                # Incorporate the special RAJA BHAI message
                await message.reply_text(
                    "**RAJA BHAI Special Message:**\n"
                    "😎𝗣𝗔𝗛𝗟𝗘 𓆩𓆩 𝗥𝗔𝗝𝗔 𝗕𝗛𝗔𝗜 𓆪𓆪 𝗞𝗢 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗝𝗔𝗞𝗘 😆😆\n\n"
                    "Let the music begin!"
                )
                await asyncio.sleep(1)

                out = start_panel(_)
                await message.reply_photo(
                    random.choice(YUMI_PICS),
                    caption=_["start_3"].format(
                        message.from_user.first_name, # This will be the user who added the bot
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
