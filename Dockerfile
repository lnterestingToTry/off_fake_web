# FROM python:3.10-slim

# #WORKDIR /app

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN pip install --upgrade pip
# RUN pip install virtualenv

# RUN virtualenv venv
# RUN /bin/bash -c "source venv/bin/activate"

# COPY ./requirements.txt .
# RUN pip install -r requirements.txt



# #WORKDIR /app/source

# COPY ./source/ ./app/source/
# #COPY ./source/database/ ./app/source/database/



# #WORKDIR /app


# COPY ./source/main.py ./app/source/
# #COPY ./env/api/init.sh ./app
# #RUN /bin/bash -c "/app/init.sh"
# #ENTRYPOINT ["/app/entrypoint.sh"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

FROM python:3.10-slim

#WORKDIR /app/source

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./source /app/source

# Указываем Flask, какой файл запускать
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN ls

COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]