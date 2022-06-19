# flask app

## Run flask app locally

```sh
cd flaskapp
flask app
```

## Build & Push

```sh
docker build -t pirafrank/flaskapp:1.0.1 -f flaskapp/Dockerfile flaskapp
docker push pirafrank/flaskapp:1.0.1

docker build -t pirafrank/flaskapp:1.0.2 -f flaskapp/Dockerfile-green flaskapp
docker push pirafrank/flaskapp:1.0.2

docker build -t pirafrank/flaskapp:bad -f flaskapp/Dockerfile-bad flaskapp
docker push pirafrank/flaskapp:bad
```

### Run image locally

```sh
docker run --rm -d -p 5000:5000 pirafrank/flaskapp:1.0.1
```

### Deploy on K8s

```sh
kubectl kustomize | kubectl apply -f -
```

### Get rollouts

```sh
kubectl argo rollouts get rollout flaskapp-rollout -w
```
