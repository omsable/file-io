FROM          jfloff/alpine-python

RUN           pip install requests
ADD           app.py /app.py

ENTRYPOINT   ["python", "/app.py"]
