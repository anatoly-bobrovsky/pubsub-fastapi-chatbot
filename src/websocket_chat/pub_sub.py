"""PUB/SUB."""

from fastapi import WebSocket

from redis_broadcaster import broadcast

from .bot import get_response_from_bot


async def chat_ws_receiver(websocket: WebSocket, chat_id: str) -> None:
    """
    Receive messages from a WebSocket connection and broadcasts responses.

    This function listens for incoming text messages from a WebSocket connection,
    generates a response using the bot, and publishes the response to a broadcast
    channel.

    Args:
        websocket (WebSocket): The WebSocket connection to receive messages from.
        chat_id (str): The identifier of the chat channel for broadcasting messages.

    Returns:
        None
    """
    async for message in websocket.iter_text():
        response_message = get_response_from_bot(message)
        await broadcast.publish(channel=chat_id, message=response_message)


async def chat_ws_sender(websocket: WebSocket, chat_id: str) -> None:
    """
    Send messages from a broadcast channel to a WebSocket connection.

    This function subscribes to a broadcast channel and sends any received messages
    to the connected WebSocket client.

    Args:
        websocket (WebSocket): The WebSocket connection to send messages to.
        chat_id (str): The identifier of the chat channel to subscribe to.

    Returns:
        None
    """
    async with broadcast.subscribe(channel=chat_id) as subscriber:
        async for event in subscriber:
            await websocket.send_text(event.message)
