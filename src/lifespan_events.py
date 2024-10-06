"""Lifespan events."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from redis_broadcaster import broadcast


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage the lifespan of a FastAPI application.

    This function connects to a broadcast system at the start of the application
    and disconnects from it when the application shuts down.

    Args:
        app (FastAPI): The FastAPI application instance.

    Yields:
        None: This context manager does not yield any values.
    """
    await broadcast.connect()
    yield
    await broadcast.disconnect()
