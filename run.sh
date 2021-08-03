#!/bin/bash

# WARNING: this file run.sh is preinjected into the docker container as running.sh.
# WARNING: If you need changes in run.sh/running.sh you need to update the docker container.
# WARNING: this includes building, uploading to dockerhub and force updating on the host.

set -o nounset
set -o errexit
set -o xtrace
set -o pipefail

# get me that sweet repo
DIR="/app/.git/"

if [ -d "$DIR" ]; then
  ## if .git folder exists just go for git pull origin master (credentials in .git/config or remote settings)
  # on my current hosting this folder is NOT persistent so this if statement is never true and this bracket was never tested.
  echo "The folder ${DIR} exists -> just git pull origin master"
  git pull origin master
else
  ## if it doesnt then go for git clone (credentials need to be provided (via .env?) if repo still private)
  echo "The folder ${DIR} does not exist -> git clone"
  cd /
  
  # option 1: preferred when no credentials are needed to pull/clone
  #rm -rf /app
  #git clone https://github.com/Prash3r/TrackmaniaTwitchBot app
  cd /app

  # option 2: git init, then add remote origin and inject credentials from environment
  git init
  git config credential.helper '!f() { sleep 1; echo "username=${GIT_USERNAME}"; echo "password=${GIT_PASSWORD}"; }; f'
  #git config 
  git remote add origin "https://${GIT_USERNAME}@github.com/Prash3r/TrackmaniaTwitchBot"
  git remote -v
  cat /app/.git/config
  echo "${GIT_USERNAME}"
  echo "${GIT_PASSWORD}"
  #git config --get user.name
  rm requirements.txt
  git pull origin master
fi

# we got the current state of the bot inside the container

# now reinstall requirements - they could have been changed with the new commit
pip3 install -r requirements.txt

# now run the bot
python3 run.py
# when this fails or gracefully terminates the container should terminate as well (needs testing)