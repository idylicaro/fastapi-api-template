FROM python:3.10 as BASE

WORKDIR /code

COPY ./requirements ./alembic.ini /code/

RUN pip install --no-deps --require-hashes --no-cache-dir

COPY ./app /code/app

FROM BASE as EXECUTE

CMD ["python", "-m","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM BASE as TEST

RUN pip install pytest pytest-mock

CMD ["pytest"]
