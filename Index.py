from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
async def start(update: Update, context):
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(f'Halo {user_first_name}!')
async def help_command(update: Update, context):
    await update.message.reply_text('Daftar perintah /start dan /help.')
async def handle_message(update: Update, context):
    text = update.message.text
    response = f"Anda mengirim pesan: {text}"
    await update.message.reply_text(response)
async def kata_hari_ini(update: Update, context):
    text = update.message.text
    response = f""
    await update.message.reply_text(response)
def main():
    TOKEN = "TOKEN"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("kata2", kata_hari_ini))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
if __name__ == '__main__':
    main()
