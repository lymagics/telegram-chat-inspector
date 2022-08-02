from requests import delete
from .filters import EnglishCensorFilter, RussianCensorFilter
from .utils import delete_message, send_message

ecf = EnglishCensorFilter()
rcf = RussianCensorFilter()


def message_handler(update, context):
    """Telegram bot message handler."""
    text = censored = str(update.message.text)
    
    if not ecf.is_clean(censored):
        censored = ecf.censor(censored)    
    if not rcf.is_clean(censored):
        censored = rcf.censor(censored)
        
    if text != censored:
        from_user = update.message.from_user
        author = f"@{from_user.username}" if from_user.username else str(from_user.first_name)
        
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        
        delete_message(context, chat_id, message_id)
        send_message(context, chat_id, author, censored)
