FROM ubuntu:latest
LABEL authors="amex"

ENTRYPOINT ["top", "-b"]