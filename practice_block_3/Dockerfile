FROM python:3.12-slim

WORKDIR /app

RUN pip install fastmcp==4.0.4

COPY *.py ./

CMD ["python", "weather_app.py"]
