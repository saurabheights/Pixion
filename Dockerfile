FROM python:3.12 AS prod

#https://github.com/johnthagen/python-blueprint/blob/main/Dockerfile
ENV POETRY_VERSION=1.8.5

# By default, pip caches copies of downloaded packages from PyPI. These are not useful within
# a Docker image, so disable this to reduce the size of images.
ENV PIP_NO_CACHE_DIR=1
# Set ENV variables that make Python more friendly to running inside a container.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry installation path to PATH.
ENV PATH="/root/.local/bin:${PATH}"
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Prevent poetry from adding a new virtual environment and use docker env.
# Use of VIRTUAL_ENV and PATH allows poetry to fix and reuse venv.
ENV VIRTUAL_ENV=/venv
RUN python -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

RUN poetry install --no-interaction --only main --no-root


FROM prod AS dev

RUN poetry install --no-interaction --with dev