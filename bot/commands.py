def start_command(update, context):
    """Telegram bot start command.
    
    enter /start to use it
    """
    update.message.reply_text("Hello! I'm here to keep this room tolerant!")
    
    
def help_command(update, context):
    """Telegram bot start command.
    
    enter /help to use it
    """
    update.message.reply_text("I will enforce tolerance in this chat. Try not to use swear words and respect each other.")
    