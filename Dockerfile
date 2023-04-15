# Sets debug support for the container (via docker-compose-debug.yaml)
ARG DEBUG=false


################################################################################
## Base image

FROM python:3-slim AS base_debug-false

RUN apt-get update && apt-get upgrade -y 
RUN pip install --no-cache-dir --upgrade pip
RUN useradd --create-home --shell /bin/bash user

CMD [ "python", "/app/main.py" ]


################################################################################
## Extension providing debug support

FROM base_debug-false as base_debug-true

RUN pip install --upgrade debugpy

EXPOSE 5678

CMD [ \
    "python", \
    "-m", "debugpy", \
    "--listen", "0.0.0.0:5678", \
    "--wait-for-client", \
    "/app/main.py" ]


################################################################################
## Main application

FROM base_debug-$DEBUG

COPY ./Source/requirements.txt .

RUN pip install \
    --no-cache-dir \
    --upgrade \
    -r requirements.txt

WORKDIR /app
COPY Source/* .

ENV PYTHONPATH "${PYTHONPATH}:/app/packages"

USER user
WORKDIR /home/user
