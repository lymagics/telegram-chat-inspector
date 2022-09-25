def start_command(update, context):
    """Telegram bot start command. Enter /start to use it."""
    update.message.reply_text("Hello! I'm here to keep this room tolerant! I require admin permission to work.")
    
    
def help_command(update, context):
    """Telegram bot help command. Enter /help to use it."""
    update.message.reply_text("I will enforce tolerance in this chat. Try not to use swear words and respect each other. I require admin permission to work.")


def updates_command(update, context):
    """Telegram bot updates command. Enter /new to use it."""
    new = """What's new?
- added Ukrainian language swear words censor.
last update: 26.09.2022
    """
    update.message.reply_text(new)
    