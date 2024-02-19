FROM Python:3.13.0a4-alpine3.19

RUN mkdir -p /home/app

COPY . /home/app

EXPOSE 8000

CMD ["python" , "/home/app/manage.py", "runserver"]