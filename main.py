from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import RedirectResponse, FileResponse
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from jinja2 import FileSystemLoader, Environment

env = Environment(loader=FileSystemLoader("static/templates"), enable_async=True)

title = "AnyBlog"

app = FastAPI(title=title, description="fast blog system at zero cost")
app.add_middleware(GZipMiddleware, minimum_size=1024)
app.mount("/static", StaticFiles(directory="./static"), "static")

templates = Jinja2Templates("./static/templates")
TemplateResponse = templates.TemplateResponse


@app.get("/")
def home_page():
    return RedirectResponse("/index.html")


@app.get("/index.html")
def index_page(request: Request):
    context = {
        "request": request,
        "title": title
    }
    return TemplateResponse("static_images.html", context)
