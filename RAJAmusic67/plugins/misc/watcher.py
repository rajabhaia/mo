from pyrogram import filters
from pyrogram.types import Message

from RAJAmusic67 import app
from RAJAmusic67.core.call import SHUKLA

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await SHUKLA.stop_stream_force(message.chat.id)
