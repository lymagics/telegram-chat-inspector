def delete_message(context, chat_id, message_id):
    """Delete message from chat."""
    context.bot.deleteMessage(chat_id=chat_id,
                                  message_id=message_id) 


def send_message(context, chat_id, author, text):
    """Send message to chat."""
    msg = f"{author} said: {text}"
    context.bot.send_message(chat_id=chat_id, text=msg)
