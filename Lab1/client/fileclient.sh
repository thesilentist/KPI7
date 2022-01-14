#client volume
docker volume create clientvol

#client build
docker build -t client .

#client run
docker run --name client --net server-client-network --rm --mount source=clientvol,target=/usr/src/app/clientdata --env ip=server --env port=5000 client