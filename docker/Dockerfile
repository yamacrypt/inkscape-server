FROM python:3.8-slim as base
 
WORKDIR /usr/src/fastapi_sample
 
COPY docker/Pipfile .
RUN pip install pipenv
RUN apt update
RUN apt install -y software-properties-common 
RUN add-apt-repository -y ppa:inkscape.dev/stable
RUN apt -y install inkscape


# 開発用
FROM base as dev
RUN pipenv install --dev
