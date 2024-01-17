# syntax = docker/dockerfile:experimental
FROM python:3.11.1-slim-buster AS base
RUN groupadd -g 30000 -r app \
    && useradd -u 30000 -r -g app -s /usr/sbin/nologin app \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates=20200601~deb10u2 \
    curl=7.* \
    dumb-init=1.2.2-1.1 \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /home/app
RUN chown -R app:app /home/app
USER app

FROM base as poetry
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV PATH="/home/app/.local/bin:${PATH}" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VERSION=1.4.2
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY --chown=app:app pyproject.toml poetry.lock ./

FROM poetry AS prod-build
RUN poetry install -v --no-root --no-dev \
    && poetry run pip install --upgrade pip==23.3.1

FROM poetry AS dev-build
RUN poetry install -v --no-root \
    && poetry run pip install --upgrade pip==23.3.1

FROM base AS runtime
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=off \
    VIRTUAL_ENV="/home/app/.venv" \
    PATH="/home/app/.venv/bin:${PATH}"
COPY --chown=app:app parcelless/ parcelless/
ENTRYPOINT ["/usr/bin/dumb-init", "--"]

FROM runtime AS prod
COPY --chown=app:app --from=prod-build /home/app/.venv /home/app/.venv/
COPY --chown=app:app config/ config/
ENV ENV_FILE=config/prod/config.env
EXPOSE 8000
COPY --chown=app:app alembic.ini ./
CMD ["gunicorn", "--access-logfile", "-", "-k", "uvicorn.workers.UvicornWorker", "-w", "2", "-t", "60", "--graceful-timeout", "60", "parcelless:app"]

FROM runtime AS dev
COPY --chown=app:app --from=dev-build /home/app/.venv /home/app/.venv/
COPY --chown=app:app tests/ tests/
COPY --chown=app:app pyproject.toml ./
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "--reload", "parcelless:app"]
