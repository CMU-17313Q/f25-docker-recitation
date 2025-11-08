# f25-docker-recitation

## 1. Running the app locally
In the root directory, run:

```terminal
pip install -r requirements.txt
```
to install requirements.

```terminal
uvicorn app.main:app --host 0.0.0.0 --port 8080
```
to locally run the app.

## 2. Build the docker image
Make sure your have `Dockerfile`
```terminal
docker build -t myimage .
```

## 3. Local or remote containerization (and deployment)
### Local
You can containerize locally two ways. Using `docker run` or using the `docker-compose.yml` file.
```terminal
docker run -d --name mycontainer -p 8080:8080 myimage 
```

OR

```terminal
docker-compose up -d
```
## 4. Stretch Challenge 
### Remote
Try to run your code remotely by running the docker container in a [codespace](https://docs.github.com/en/codespaces/quickstart)
