
FROM python:3.13-slim

WORKDIR /src

RUN apt-get update && \
    apt-get install -y -qq \
    libsdl2-dev \
    python3-xlib \
    libx11-dev \
    libxrandr-dev \
    libxkbcommon-x11-0 \      
    libxcb-cursor0 \
    libxcb-xinerama0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-util1 \
    libxcb-xfixes0 \
    libxcb-shape0 \ 
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

ENV QT_QPA_PLATFORM=xcb

COPY requirements.txt .

RUN python -m venv .venv && \
  .venv/bin/pip install --upgrade pip && \
  .venv/bin/pip install -r requirements.txt

COPY src .

CMD [".venv/bin/python", "main.py"]

