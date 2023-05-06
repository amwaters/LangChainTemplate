# Sets debug support for the container (via docker-compose-debug.yaml)
ARG DEBUG=false
ARG STREAMLIT=false
ARG MOUNT=false


################################################################################
## Base image

FROM python:3-slim AS base-0

RUN apt-get update && apt-get upgrade -y 
RUN pip install --no-cache-dir --upgrade pip
RUN useradd --create-home --shell /bin/bash user

ENV PYTHON_ARGS=""
ENV PYTHON_ENTRYPOINT=/app/main.py


################################################################################
## Dependency installation

WORKDIR /tmp
COPY ./Source/requirements.txt .

RUN pip install \
      --no-cache-dir \
      --upgrade \
      --requirement requirements.txt \
&&  rm requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app/packages"


################################################################################
## Extension providing debug support

FROM base-0 AS debug-false
FROM base-0 AS debug-true

ENV DEBUG=true
ENV PYTHON_ARGS="$PYTHON_ARGS \
    -m debugpy \
    --listen 0.0.0.0:5678 \
    --wait-for-client \
    $PYTHON_ARGS \
"

RUN pip install --upgrade debugpy

EXPOSE 5678

FROM debug-$DEBUG AS base-1


################################################################################
## Extension providing streamlit support

FROM base-1 AS streamlit-false
FROM base-1 AS streamlit-true

RUN pip install --upgrade streamlit

ENV STREAMLIT=true
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501

ENV PYTHON_ARGS="$PYTHON_ARGS -m streamlit run"
ENV PYTHON_ENTRYPOINT="/app/Home.py"

EXPOSE 8501

FROM streamlit-$STREAMLIT AS base-2


################################################################################
## Extension providing mounted source for live development

FROM base-2 AS mount-true
FROM base-2 AS mount-false

WORKDIR /app
COPY Source/* .
RUN chmod a-w .

FROM mount-$MOUNT AS base-3


################################################################################
## Main application

FROM base-3
USER user
WORKDIR /home/user
ENV PYTHON_ARGS="$PYTHON_ARGS $PYTHON_ENTRYPOINT"
CMD [ "sh", "-c", "echo \"$PYTHON_ARGS\" | xargs python" ]
