from __future__ import annotations

from datetime import datetime, timezone

from loguru import logger
from pydantic import BaseModel, Field
from syft_event import SyftEvents


class PingRequest(BaseModel):
    """Request to send a ping."""

    msg: str = Field(description="Ping request string")
    ts: datetime = Field(description="Timestamp of the ping request.")


class PongResponse(BaseModel):
    """Response to a ping request."""

    msg: str = Field(description="Ping response string")
    ts: datetime = Field(description="Timestamp of the pong response.")


box = SyftEvents("pingpong")


@box.on_request("/ping")
def ping_handler(ping: PingRequest) -> PongResponse:
    """Handle a ping request and return a pong response."""
    logger.info(f"Got ping request - {ping}")
    return PongResponse(
        msg=f"Pong from {box.client.email}",
        ts=datetime.now(timezone.utc),
    )


if __name__ == "__main__":
    try:
        box.run_forever()
    except Exception as e:
        print(e)
