FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

RUN pip install apache-airflow==2.3.3 psycopg2-binary black mypy flake8 pytest