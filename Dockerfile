FROM python:3.13-slim

WORKDIR /src

RUN apt-get update && apt-get install -y -qq --no-install-recommends \
  git \
  libxcb-cursor0 \
  libx11-xcb1 \
  libxcb-icccm4 \
  libxcb-image0 \
  libxcb-keysyms1 \
  libxcb-render-util0 \
  libxcb-render0 \
  libxcb-shape0 \
  libxcb-xfixes0 \
  libxcb-xinerama0 \
  libxcb-xkb1 \
  libxcb1 \
  libxrender1 \
  libxkbcommon-x11-0 \
  libxkbcommon0 \
  x11-xkb-utils \
  libfontconfig1 \
  libfreetype6 \
  libgl1 \
  libglx0 \
  libglvnd0 \
  libglapi-mesa \
  libegl1 \
  libgles2 \
  libglib2.0-0 \
  dbus \
  libdbus-1-3 \
  && rm -rf /var/lib/apt/lists/*

ENV QT_QPA_PLATFORM=xcb

COPY requirements.txt .

RUN python -m venv .venv && \
  .venv/bin/pip install --upgrade pip && \
  .venv/bin/pip install -r requirements.txt

COPY src .

CMD [".venv/bin/python", "main.py"]

