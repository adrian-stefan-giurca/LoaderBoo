FROM python:3.14

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN apt upgrade && apt update -y && apt install ffmpeg -y

CMD ["fastapi", "run", "app/main.py", "--port", "8000", "--host", "0.0.0.0"]