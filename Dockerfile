FROM python:3.8-alpine

WORKDIR /usr/src/app

RUN apk add --no-cache \
        build-base \
        linux-headers \
        libffi-dev

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod +x /usr/src/app/entrypoint.sh

CMD ["/usr/src/app/entrypoint.sh"]
