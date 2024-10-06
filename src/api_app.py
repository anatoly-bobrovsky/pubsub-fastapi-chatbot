"""API App entry point."""

import uvicorn
from fastapi import FastAPI

from lifespan_events import lifespan
from websocket_chat import websocket_chat_router

app = FastAPI(
    title="Chatbot",
    description="Pub/Sub Chatbot",
    lifespan=lifespan,
)

app.include_router(websocket_chat_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
