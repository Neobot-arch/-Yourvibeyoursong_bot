from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "musicbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        "Telegram Music Bot is running. Use /play <song name>"
    )

@app.on_message(filters.command("play"))
async def play(_, message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply_text("Usage: /play <song name>")
    await message.reply_text(f"Searching for: {query}")

app.run()
