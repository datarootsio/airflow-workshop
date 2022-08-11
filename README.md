# airflow-workshop

## How to setup

1. Github: https://github.com/datarootsio/airflow-workshop
2. VSCode and install the extension “remote-containers”
3. Clone the repo
4. Open it in VSCode
5. Open command pallet (cmd+shift+p on mac) and search for “remote-containers: rebuild and reopen” and press that

## Restart with clean env

WARNING!! THIS WILL DELETE ALL VOLUMES  
so if you have volumes with data that you need, be carefull.

1. close the vscode window opened in the dev container
2. make sure all containers are stopped `docker kill $(docker ps -aq)`
3. remove all containers `docker container rm $(docker ps -aq)`
4. remove all volumes `docker volume rm $(docker volume ls -q)`
5. Reopen vscode
6. Open command pallet (cmd+shift+p on mac) and search for “remote-containers: rebuild and reopen” and press that
