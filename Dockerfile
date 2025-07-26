FROM python:3.11

# set work directory
WORKDIR /usr/srv

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/srv
RUN useradd -rm -d /code -s /bin/bash -g root -G sudo -u 1001 ubuntu

# copy requirements file
COPY ./requirements.txt /usr/srv/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install --no-cache-dir pytest
RUN pip install --no-cache-dir pytest pytest-cov
RUN pip install --no-cache-dir pytest pytest-asyncio pytest-cov httpx
RUN pip install --no-cache-dir httpx pytest-asyncio

USER ubuntu

EXPOSE 8000

CMD bash -c 'uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload'