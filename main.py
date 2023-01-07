import functions_framework
import os
import telegram
from telegram import Update
from telegram.ext import Updater,Dispatcher, CommandHandler, MessageHandler, Filters, CallbackContext

# Define a function for the /start command
def start(update: Update, context: CallbackContext) -> None:
   # Get chat_id from update
   chat_id = update.message.chat.id
   text = update.message.text
   # Send message to chat_id
   bot.sendMessage(chat_id=chat_id, text=text)


   
# Get TOKEN from environment variable
TOKEN = os.environ.get('TOKEN')
# Create bot instance
bot = telegram.Bot(token=TOKEN)

@functions_framework.http
def main(request):
   # Check if request is POST
   if request.method == 'POST':
      # Create a dispatcher instance
      dp = Dispatcher(bot, None,workers=0)
      # Get update from request
      update = Update.de_json(request.get_json(force=True), bot)
      # Add handlers
      dp.add_handler(CommandHandler('start', start))
      dp.process_update(update) 
      return {'ok':TOKEN}

   
   return f'TOKEN: {TOKEN}!'