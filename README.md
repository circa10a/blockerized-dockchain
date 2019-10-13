# blockerized-dockchain

Because all problems are solvable with containers and blockchains

![alt text](https://i.imgur.com/vRLEtBr.jpg)

## Usage

```shell
docker run --rm --name blockerized-dockchain circa10a/blockerized-dockchain
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
- Big Data
- Quantum Computing
- IOT
