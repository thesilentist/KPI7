Enter running docker container:
```sh
sudo  docker exec -it server bash
```
Get into the server shell:
```sh
sudo docker run --name server --net server-client-network --rm --mount source=servervol,target=/usr/src/app/serverdata --env port=5000 -it server bash
```
Get into the client shell:
```sh
sudo docker run --name client --net server-client-network --rm --mount source=clientvol,target=/usr/src/app/clientdata -it client bash
```