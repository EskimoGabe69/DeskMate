FROM python:3.13-slim

WORKDIR /src

RUN apt-get update && apt-get install -y \ 
  libsdl2-dev \
  python3-xlib \
  libx11-dev \
  libxrandr-dev \
  libxcb-cursor-dev \
  libxcb-cursor0 \
  qt6-base-dev \
  -qq libglu1-mesa-dev libx11-xcb-dev '^libxcb*' \
  && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN python -m venv .venv && \
  .venv/bin/pip install --upgrade pip && \
  .venv/bin/pip install -r requirements.txt

COPY src .

CMD [".venv/bin/python", "main.py"]
