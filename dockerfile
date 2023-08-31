FROM python:3.9.16

RUN apt-get update && \
    apt-get install -y default-jdk && \
    pip install konlpy

WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py /app
COPY Blank_Fill /app/Blank_Fill
COPY Multiple_Choice /app/Multiple_Choice


EXPOSE 5050
CMD ["python", "server.py"]


