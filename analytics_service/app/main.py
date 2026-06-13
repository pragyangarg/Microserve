from fastapi import FastAPI

from app.logger import logger

app = FastAPI()

events = []


@app.post("/track")
def track_event(
    event: dict
):
    logger.info(
    f"EVENT RECORDED: {event}"
    )
    events.append(event)

    return {
        "message": "event recorded"
    }


@app.get("/events")
def get_events():

    return events