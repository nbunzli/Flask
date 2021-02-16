Flask app deployed in a docker container.

Use the following commands to build and run the docker image.
```
docker build -t <TAG> .
docker run -p 5000:5000 -d <TAG>
```

App can then be accessed at port 5000 of the host machine.
```
curl http://localhost:5000/
curl http://localhost:5000/sum?a=2&b=5
```