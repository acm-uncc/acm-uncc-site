from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from .acm_calendar import get_events

app = FastAPI()

templates = Jinja2Templates(directory='templates')
static = StaticFiles(directory='static')
app.mount('/static', static, name='static')


@app.get('/')
async def index(request: Request):
    events = get_events(3)
    return templates.TemplateResponse('index.html', {
        'request': request,
        'event_list': events
    })
