# airflow-workshop

## How to setup

1. Clone this repo: https://github.com/datarootsio/airflow-workshop
2. Open VSCode and install the extension “Dev containers"
4. Open this repo
5. Open command pallete (cmd+shift+p on mac) and search for “Dev-containers: rebuild and reopen” and press that
6. Wait a few minutes for all containers to start
7. Access the Airflow UI at http://localhost:8080. User: `airflow`, password: `airflow`
8. Start writing DAGs

## Restart with clean env

WARNING!! THIS WILL DELETE ALL VOLUMES  
You will lose dagruns, dataset events, XCOM, .. etc!

1. close the vscode window opened in the dev container
2. make sure all containers are stopped `docker kill $(docker ps -aq)`
3. remove all containers `docker container rm $(docker ps -aq)`
4. remove all volumes `docker volume rm $(docker volume ls -q)`
5. Reopen vscode
6. Open command pallet (cmd+shift+p on mac) and search for “remote-containers: rebuild and reopen” and press that
