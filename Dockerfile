FROM python:3.12

WORKDIR /usr/app

COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
CMD [ "fastapi","dev", "app.py" ]

