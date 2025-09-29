import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, ChatMemberHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")  # We'll set this on Render

WELCOME_MESSAGE = (
    "👋 Welcome to AspireX, {name}!\n"
    "Please make sure you read through the rules topic, and also the Beginners Guide topic "
    "where you can find a bunch of videos that will help you get set up as well as our basics Ebook 'aspire.'"
)

async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.chat_member.new_chat_members:
        name = member.full_name
        chat_id = update.chat_member.chat.id

        await context.bot.send_message(
            chat_id=chat_id,
            text=WELCOME_MESSAGE.format(name=name)
        )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatMemberHandler(new_member, ChatMemberHandler.CHAT_MEMBER))
    app.run_polling()
