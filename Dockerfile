FROM python:3.13-slim

WORKDIR /src

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY requirements.txt .

RUN uv venv .venv && \
    .venv/bin/python install requirements.txt

COPY . .

CMD [".venv/bin/python", "main.py"]

