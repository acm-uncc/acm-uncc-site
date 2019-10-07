from starlette.applications import Starlette
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app import data
from app.acm_calendar import get_events

app = Starlette()

templates = Jinja2Templates(directory='templates')
static = StaticFiles(directory='static')
app.mount('/static', static, name='static')


@app.route('/', methods=['get'])
async def index(request: Request):
    events = get_events(3)
    return templates.TemplateResponse('index.html', {
        'request': request,
        'event_list': events,
    })


@app.route('/mongo', methods=['get'])
async def mongo_index(request: Request):
    return templates.TemplateResponse('mongo.html', {
        'request': request,
        'times': data.times()
    })


@app.route('/mongo/add', methods=['post'])
async def mongo_insert(request: Request):
    data.add_time()
    return RedirectResponse('/mongo')
