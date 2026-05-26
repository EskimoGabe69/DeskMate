FROM python:3.13-slim

WORKDIR /src

RUN apt-get update && apt-get install -y \ 
  curl

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="$${PATH}:$${HOME}/.local/bin"

COPY requirements.txt .

RUN uv venv .venv && \
  .venv/bin/python install requirements.txt

COPY . .

CMD [".venv/bin/python", "main.py"]

