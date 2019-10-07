FROM python:3.7-alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install pipenv cython

WORKDIR /app
ADD . /app
RUN pipenv install

CMD pipenv run uvicorn app.acm:app --host 0.0.0.0 --port $PORT --proxy-headers
