FROM python:3.12-alpine

ADD main.py .

RUN pip install numpy pandas pygsheets requests python-dotenv pytz

CMD [ "python", "./main.py"]


