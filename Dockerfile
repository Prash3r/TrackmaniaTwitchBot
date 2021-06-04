# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /app

COPY requirements.txt run.py ./
RUN pip3 install -r requirements.txt

COPY TTBot /app/TTBot

CMD [ "python3", "run.py"]
#CMD ["/bin/bash" "-c" "\"./run.sh\""]
