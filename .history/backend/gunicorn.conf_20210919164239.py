
2
3
4
5
6
7
8
9
10
11
12
13
 
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