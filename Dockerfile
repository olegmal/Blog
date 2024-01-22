FROM python:3.11-rc-slim

RUN apt update && mkdir "/blog"

WORKDIR /blog

COPY ./src ./src
COPY ./commands ./commands
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt

CMD ["bash"]

