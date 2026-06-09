from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "musicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def alive(_, message):
    await message.reply_text("Bot Online ✅")

app.run()
