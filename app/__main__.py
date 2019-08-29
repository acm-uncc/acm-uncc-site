import uvicorn
import os

host = '0.0.0.0'
port = os.environ.get('PORT', 8000)

uvicorn.run('app.acm:app', host=host, port=int(port))
