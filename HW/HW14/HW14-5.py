from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})


@app.post("/create-user", response_class=HTMLResponse)
async def create_user(request: Request, username: str, email: str, password: str, password_confirmation: str):
    if len(password) < 8 or len(password_confirmation) < 8:
        return templates.TemplateResponse("create_user.html", {"request": request,
                                                               "error_message1": "Password must be at least 8 characters."})

    if password != password_confirmation:
        return templates.TemplateResponse("create_user.html", {"request": request,
                                                               "error_message2": "Passwords do not match."})

    return templates.TemplateResponse("user_created.html", {"request": request, "username": username, "email": email})
