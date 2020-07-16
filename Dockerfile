FROM python:latest

COPY . .

RUN pip install -r requirements.txt

EXPOSE 80
EXPOSE 443

#ENTRYPOINT ["python", "bot.py"]