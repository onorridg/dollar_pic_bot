FROM python:3.9.17-alpine3.18
WORKDIR /bot
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "src/bot.py" ]