FROM python:latest

RUN python -m venv /opt/venv

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
EXPOSE 5000

COPY . .
CMD ["flask", "--app", "src/app", "--debug", "run", "--host=0.0.0.0"]