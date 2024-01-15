# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """

<b>Press "Start"</b>
Subscribe☑️ to the channel and select the Series you want to watch📲
"""

    close = [
        [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
            InlineKeyboardButton("Cʟᴏsᴇ", callback_data="close")
        ],
    ]

    ABOUT = """
Hello , Thanks for using me :D

♥️ Developed by Unkown entity (≧▽≦)
"""
