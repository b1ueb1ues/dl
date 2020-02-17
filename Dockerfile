FROM python:3.7-alpine

RUN pip install Flask Flask-Cors requests

ENV PYTHONPATH=/

COPY . /
WORKDIR /app

ENTRYPOINT [ "flask" ]

CMD [ "run","--host","0.0.0.0" ]