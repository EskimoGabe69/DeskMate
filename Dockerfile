FROM python:3.13-slim

WORKDIR /src

RUN apt-get update && \
    apt-get install -y -qq \
    libsdl2-dev \
    python3-xlib \
    libx11-dev \
    libxrandr-dev \
    libxcb-cursor-dev \
    libxcb-cursor0 \
    qt6-base-dev \
    qt6-declarative-dev \
    qt6-multimedia-dev \
    qt6-webengine-dev \
    qt6-svg-dev \
    qt6-tools-dev \
    qtbase5-dev \
    qt5-qmake \
    libxcb-xinerama0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-render-util0 \
    libxcb-util1 \
    xvfb \
    libglu1-mesa-dev \
    libx11-xcb-dev \
    'libxcb.*' \
    && rm -rf /var/lib/apt/lists/*

ENV QT_QPA_PLATFORM=xcb

COPY requirements.txt .

RUN python -m venv .venv && \
  .venv/bin/pip install --upgrade pip && \
  .venv/bin/pip install -r requirements.txt

COPY src .

CMD [".venv/bin/python", "main.py"]
