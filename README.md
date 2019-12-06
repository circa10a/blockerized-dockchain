# blockerized-dockchain

Create a blockchain in a docker container, because all problems are solvable with containers and blockchains.

![alt text](https://i.imgur.com/vRLEtBr.jpg)

## Usage

### Docker

```shell
docker run --rm --name blockerized-dockchain circa10a/blockerized-dockchain
```

### Kubernetes

```shell
kubectl apply -f https://raw.githubusercontent.com/circa10a/blockerized-dockchain/master/k8s-deployment.yaml
```

### Options

Opts are set via environment variables

| Environment Variable | Type   | Default    | Description                               |
|----------------------|--------|------------|-------------------------------------------|
| `WAIT_PERIOD`        | number | `1`        | Seconds between adding blocks             |
| `EXIT_COUNT`         | number | `Infinite` | How many blocks to create before exiting  |

### Sample config

```shell
docker run --rm -e EXIT_COUNT=20 -e WAIT_PERIOD=2 --name blockerized-dockchain circa10a/blockerized-dockchain
```

## Roadmap

- Machine Learning
- AI
- Cloud
- Serverless
- Big Data
- Quantum Computing
- Microkernel
- IOT
- Service Mesh
- Multiple [geese](https://golang.org/pkg/go/build/#hdr-Go_Path)
- [gorch](https://golang.org/pkg/go/build/#hdr-Go_Path)

## Credits

- Original name coined by [infidex](https://github.com/infidex)
- Original blockchain application by [Gerald Nash](https://medium.com/@aunyks)
- Photo by [morioh.com](https://morioh.com/p/b46e20454368)
