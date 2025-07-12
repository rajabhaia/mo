from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from RAJAmusic67 import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
        InlineKeyboardButton(
            text="▪️ᴍᴏʀᴇ▪️", callback_data="help_callback hb13"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="▪️ ᴧᴅᴍɪɴ ▪️",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="▪️ ᴧᴜᴛʜ ▪️",
                    callback_data="help_callback hb2",
                ),
            
            ],
            [
                InlineKeyboardButton(
                    text="▪️ ʙʟᴏᴄᴋ ▪️",
                    callback_data="help_callback hb3",
                ),
                InlineKeyboardButton(
                    text="▪️ ɢ-ᴄᴧsᴛ ▪️",
                    callback_data="help_callback hb4",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="▪️ ɢ-ʙᴧɴ ▪️",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="▪️ ʟʏʀɪᴄs ▪️",
                    callback_data="help_callback hb5",
                ),
            ],
                        
            [
                InlineKeyboardButton(
                    text="▪️ ᴘʟᴀʏʟɪsᴛs ▪️",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="▪️ ᴠᴏɪᴄᴇ-ᴄʜᴀᴛ ▪️",
                    callback_data="help_callback hb10",
                ),
            ],
            [
                            InlineKeyboardButton(text="👿DEMON👿", url=f"https://t.me/DEMONPAPATHUMAHRA"),
                            InlineKeyboardButton(text="😎RAJA BHAI😎", url=f"https://t.me/RAJARAJ909"),
            ],
            [
           
                InlineKeyboardButton(
                    text="▪️ ᴘʟᴀʏ ▪️",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="▪️ sᴜᴅᴏ ▪️",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="▪️ sᴛᴀʀᴛ ▪️",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="▪️ ️ᴍᴏʀᴇ ▪️", callback_data="help_callback hb14"
                )

            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="▪️ ʜᴇʟᴘ ▪️",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
    
    
    
