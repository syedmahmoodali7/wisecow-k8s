FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/games:${PATH}"

RUN apt-get update && apt-get install -y \
    fortune cowsay netcat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY wisecow.sh .

RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix wisecow.sh
RUN chmod +x wisecow.sh

EXPOSE 4499

CMD ["./wisecow.sh"]