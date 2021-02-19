Flask app deployed in a docker container. The app doesn't really do much in this project - there is a test endpoint and an endpoint which can add two numbers. The motivation was to try to "dockerize" a flask app, which it turns out is really easy. This repo can serve as a template/starting point for a docker flask app.

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
