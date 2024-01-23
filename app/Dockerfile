FROM python:3.10-alpine

WORKDIR /code

COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/app
WORKDIR /code/app

USER 1000

ENV OPENAI_API_KEY <PUT YOUR KEY HEAR>
ENV DATABASE_URI clickhouse+native://localhost/default

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



