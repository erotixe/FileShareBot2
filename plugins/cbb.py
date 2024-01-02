#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>\n○  ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={5191566338}'>Killua </a>\n○  ʟᴀɴɢᴜᴀɢᴇ : <code>Eng Sub & Dub</code>\n○  Main Channel : <a href=https://t.me/Animes_Alliance>Anime Alliance</a>\n○  Support Group : <a href=https://t.me/Alliance_Weebs>Anime Chats</a>\n</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
