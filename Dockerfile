# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY run.sh ./running.sh
# its dirty i know but this allows me to pull the repo in place wehre running.sh already exists and is executed

#COPY TTBot /app/TTBot

#CMD [ "python3", "run.py"]
#CMD ["/bin/bash" "-c" "\"./run.sh\""]
CMD ["/bin/bash", "running.sh"]
# clone repo if no .git folder otherwise pull, then reinstall requirements - they may have changed, then run bot