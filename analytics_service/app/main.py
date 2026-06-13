from fastapi import FastAPI

app = FastAPI()

events = []


@app.post("/track")
def track_event(
    event: dict
):

    events.append(event)

    return {
        "message": "event recorded"
    }


@app.get("/events")
def get_events():

    return events