from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6061907199:AAH8ciYkbkAKW0hfu28XMPUZPkVKkvo2HGo'
BOT_USERNAME: Final = '@sghistorybot'

# Commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thank you for using this bot. This bot is made by @sghistorybot. To use this bot, just send me a message and I will reply you with the history of Bulgaria!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a historian bot prease send me a message and I will reply you with some history fact of Bulgaria!')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom comand!')

# Responses

def handle_response(text: str) -> str:
    prossed: str = text.lower()
    if 'hello' in prossed:
        return 'Hi!'
    if 'How are you?' in prossed:
        return 'I am fine, thank you!'
    if 'Who are you?' in prossed:
        return 'I am a historian bot!'
    if 'What is your name?' in prossed:
        return 'My name is @sghistorybot!'
    if 'What is your purpose?' in prossed:
        return 'My purpose is to tell you some history facts about Bulgaria!'
    if 'When Bulgaria was founded?' in prossed:
        return '681 A.C.'
    if 'What is the name of the  first capital?' in prossed:
        return 'The first capital of Bulgaria is Pliska!'
    if 'What is the the name of first Tzar of Bulgaria?' in prossed:
        return 'Tzar Simeon I!'
    if 'What is the name of the last Tzar of Bulgaria?' in prossed:
        return 'Tzar Boris III!'
    if 'When was liberation of Bulgaria?' in prossed:
        return '03 03 1879 after San Stefano peace treaty!'
    if 'Who is first bulgarian historian?' in prossed:
        return 'Paisiy Hilendarski!'
    # to be continued...
    if 'I love Bulgaria!' in prossed:
        return 'Please Subscribe!'
    
    return 'I do not understand you!'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip
            responce: str = handle_response(new_text)
        else:
            return    
    else:
        responce: str = handle_response(text)
    
    print('Bot:' , responce)
    await update.message.reply_text(responce)
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot ...')
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Errors
    app.add_error_handler(error)
    
    # Poll the bot
    print('Bot is polling...')
    app.run_polling(poll_interval=0.5, timeout=10)
    
    
        
