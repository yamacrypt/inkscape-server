
version: '3.9'
services:
  fastapi-sample:
    build:
      target: dev
    volumes:
      - ./backend:/usr/src/fastapi_sample/backend
    ports:
      - 8080:8080
    environment:
      - PORT=8080