docker stop energyvars
docker rm energyvars
docker build --no-cache -t energyvars .
docker run -d --name energyvars -p 83:80 energyvars:latest