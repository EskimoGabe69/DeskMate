FROM python:3.13-slim

WORKDIR /src

RUN apt-get update && apt-get install -y \ 
  libsdl2-dev \
  && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN python -m venv .venv && \
  .venv/bin/pip install --upgrade pip && \
  .venv/bin/pip install -r requirements.txt

COPY src .

CMD [".venv/bin/python", "main.py"]
