"""Bot."""


def get_response_from_bot(user_message: str) -> str:
    """
    Generate a response from the bot based on the user's message.

    Args:
        user_message (str): The message received from the user.

    Returns:
        str: A formatted response from the bot.
    """
    return f"BOT: {user_message}"
