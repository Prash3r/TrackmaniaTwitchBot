#!/bin/bash
set -o nounset
set -o errexit
set -o xtrace
set -o pipefail

# get me that sweet repo
DIR="/app/.git/"

if [ -d "$DIR" ]; then
  ## if .git folder exists just go for git pull origin master (credentials in .git/config or remote settings)
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
  git config credential.helper '!f() { sleep 1; echo "username=${GIT_USER}"; echo "password=${GIT_PASSWORD}"; }; f'
  git add remote origin https://github.com/Prash3r/TrackmaniaTwitchBot
  cat /app/.git/config
  git config --get user.name
  git pull origin universal_docker
fi

# we got the current state of the bot inside the container

# now reinstall requirements - they could have been changed with the new commit
pip3 install -r requirements.txt

# now run the bot
python3 run.py
# when this fails or gracefully terminates the container should terminate as well (needs testing)