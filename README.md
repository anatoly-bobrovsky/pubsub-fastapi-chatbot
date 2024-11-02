# Pub/Sub Chatbot Using FastAPI and Broadcaster

## Overview

This repository provides a template for a chatbot backend built with `FastAPI`, using `WebSocket` communication and a `Pub/Sub` architecture. The project is designed for scalability and flexibility, leveraging `Redis` as the message broker. The setup allows seamless two-way communication for chat applications, making it suitable for various deployment environments.

## Features

- **WebSocket Communication**: Real-time interaction through WebSocket endpoints.
- **Pub/Sub Architecture**: Manages user sessions and messages using the `broadcaster` library with `Redis PUB/SUB` for efficient, isolated message handling.
- **Dockerized Deployment**: Simplified deployment using `docker-compose` for setting up both `FastAPI` and `Redis` services.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.
- [Postman](https://www.postman.com/) or any WebSocket client for testing.

### Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/anatoly-bobrovsky/pubsub-fastapi-chatbot.git
   cd pubsub-fastapi-chatbot
   ```

2. **Build Docker Images**:
   ```bash
   docker compose build chatbot
   ```

3. **Create External Volume for Redis**:
   ```bash
   docker volume create redis-data
   ```

4. **Run Services**:
   ```bash
   docker compose up
   ```

### Usage

1. Open `Postman`, create a new WebSocket connection with the URL `ws://localhost:8000/chatbot/{chat_id}` (e.g., `ws://localhost:8000/chatbot/1`).
2. Connect and send messages to test interaction with the bot. The bot echoes received messages with a "BOT:" prefix.

## Project Structure

- **`src/redis_broadcaster.py`**: Configures `Redis` for message broadcasting.
- **`src/api_app.py`**: Initializes `FastAPI` app with WebSocket support.
- **`src/websocket_chat/`**: Contains WebSocket routing and Pub/Sub logic.
- **`Dockerfile`**: Builds a lightweight container for the chatbot service.
- **`docker-compose.yaml`**: Manages multi-container deployment of the chatbot and Redis.
