import logging
import requests
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

logger = logging.getLogger(__name__)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    status_code = exc.status_code
    detail = exc.detail

    try:
        url = "http://external-service.com/notifications"
        payload = {"message": f"HTTP error {status_code}: {detail}"}
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.exception(f"Error sending notification: {e}")

    return {"error": {"status_code": status_code, "detail": detail}}
