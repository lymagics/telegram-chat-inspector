from requests import delete
from .filters import FilterProvider, EnglishCensorFilter, RussianCensorFilter, \
    UkrainianCensorFilter
from .utils import delete_message, send_message

provider = FilterProvider()
provider.register_filters(
    EnglishCensorFilter,
    RussianCensorFilter,
    UkrainianCensorFilter
)


def message_handler(update, context):
    """Telegram bot message handler."""
    text = str(update.message.text)
    censored = provider.censore(text)
        
    if text != censored:
        from_user = update.message.from_user
        author = f"@{from_user.username}" if from_user.username else str(from_user.first_name)
        
        chat_id = update.message.chat_id
        message_id = update.message.message_id
        
        delete_message(context, chat_id, message_id)
        send_message(context, chat_id, author, censored)
