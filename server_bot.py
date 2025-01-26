from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from transformers import pipeline


pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hello! I am your AI assistant. How can I help you?")

async def process(update: Update, context: CallbackContext) -> None:
    """Process the user message."""
    user_message = update.message.text
   
    response = pipe(user_message, max_length=50)[0]['generated_text']
    await update.message.reply_text(response)

def main() -> None:
    """Start the bot."""
    API_TOKEN = "7702609674:AAGzLzBd70oesz63e6aY_jsrx1KJ-hqo4E0"
    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process))

    application.run_polling()

if __name__ == '__main__':
    main()