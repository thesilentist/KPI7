#network
docker network create server-client-network

#server volume
docker volume create servervol

#server build
docker build -t server .

#server run
docker run --name server --net server-client-network --rm --mount source=servervol,target=/usr/src/app/serverdata --env port=5000 server
