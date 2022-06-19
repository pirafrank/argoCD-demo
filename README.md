# flask app

## Build

```sh
cd flaskapp
docker build -t flaskapp:1.0.0 -f Dockerfile .
```

## Run locally

```sh
cd flaskapp
docker run --rm -d -p 5000:5000 flaskapp:1.0.0
```

