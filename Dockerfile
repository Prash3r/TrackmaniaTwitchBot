# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /app

COPY requirements.txt run.py ./
COPY run.sh run.sh ./
RUN pip3 install -r requirements.txt

#COPY TTBot /app/TTBot

#CMD [ "python3", "run.py"]
#CMD ["/bin/bash" "-c" "\"./run.sh\""]
CMD ["/bin/bash", "run.sh"]
# clone repo if no .git folder otherwise pull, then reinstall requirements - they may have changed, then run bot