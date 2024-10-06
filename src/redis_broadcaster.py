"""Redis broadcaster."""

from broadcaster import Broadcast

DB_URI = "redis://redis:6379"
broadcast = Broadcast(DB_URI)
