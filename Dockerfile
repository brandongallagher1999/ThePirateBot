FROM python:latest

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "bot.py"]