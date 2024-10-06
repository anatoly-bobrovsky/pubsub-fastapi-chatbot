"""Websocket chat router."""

from fastapi import APIRouter, WebSocket
from starlette.concurrency import run_until_first_complete

from .pub_sub import chat_ws_receiver, chat_ws_sender

websocket_chat_router = APIRouter()


@websocket_chat_router.websocket("/chatbot/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: str):
    """
    Handle websocket chat connections.

    Args:
        websocket (WebSocket): The WebSocket connection instance.
        chat_id (str): The identifier for the chat session.
    """
    await websocket.accept()

    await run_until_first_complete(
        (chat_ws_receiver, {"websocket": websocket, "chat_id": chat_id}),
        (chat_ws_sender, {"websocket": websocket, "chat_id": chat_id}),
    )
