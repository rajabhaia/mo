import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from RAJAmusic67 import LOGGER, app, userbot
from RAJAmusic67.core.call import SHUKLA
from RAJAmusic67.misc import sudo
from RAJAmusic67.plugins import ALL_MODULES
from RAJAmusic67.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝗔𝗕𝗘 𝗟𝗢𝗗𝗘 𝗦𝗧𝗥𝗜𝗡𝗚 𝗧𝗘𝗥𝗔 𝗕𝗔𝗣 𝗗𝗔𝗟𝗘 𝗚𝗔 𝗞𝗬𝗔 😑")
        
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("RAJAmusic67.plugins" + all_module)
    LOGGER("RAJAmusic67.plugins").info("𝗔𝗕𝗘 𝗥𝗔𝗡𝗗𝗜 𝗞𝗘 𝗕𝗔𝗖𝗛𝗘 𝗥𝗘𝗣𝗢 𝗘𝗗𝗜𝗧 𝗞𝗔𝗥 𝗟𝗜𝗔  👿 ...")
    await userbot.start()
    await SHUKLA.start()
    await SHUKLA.decorators()
    LOGGER("RAJAmusic67").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝐌𝐀𝐃𝐄 𝐁𝐘 𝐓𝐄𝐀𝐌 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑♨️\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("RAJAmusic67").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝐌𝐀𝐃𝐄 𝐁𝐘 𝐓𝐄𝐀𝐌 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑♨️\n╚═════ஜ۩۞۩ஜ════╝")
    

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
