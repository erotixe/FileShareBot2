import os

import speedtest
import wget
from pyrogram import filters
from pyrogram.types import Message

from bot import Bot
from config import ADMINS


@Bot.on_message(filters.command("speedtest") & filters.user(ADMINS))
async def run_speedtest(client: Bot, message: Message):
    m = await message.reply_text("⚡️ Running Server Speedtest")
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = await m.edit("⚡️ Running Download Speedtest..")
        test.download()
        m = await m.edit("⚡️ Running Upload Speedtest...")
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        await m.edit(e)
        return
    m = await m.edit("🔄 Sharing Speedtest Results")
    path = wget.download(result["share"])

    output = f"""💡 <b>SpeedTest Results</b>   
<u><b>Client:<b></u>
<b>ISP:</b> {result['client']['isp']}
<b>Country:</b> {result['client']['country']} 
<u><b>Server:</b></u>
<b>Name:</b> {result['server']['name']}
<b>Country:</b> {result['server']['country']}, {result['server']['cc']}
<b>Sponsor:</b> {result['server']['sponsor']}
⚡️ <b>Ping:</b> {result['ping']}"""
    msg = await client.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()
