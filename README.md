## Containers

Build and publish images compatible with `linux/amd64` and `linux/arm64` architectures.

- **postgis 3.3** (code from https://github.com/postgis/docker-postgis)
    - Base: `postgres:${POSTGRES_VERSION}-bullseye`
    - Images:
        - `ghcr.io/vincentsarago/postgis:13-3.3`
        - `ghcr.io/vincentsarago/postgis:14-3.3`
        - `ghcr.io/vincentsarago/postgis:15-3.3`

    - old images:
        - `ghcr.io/vincentsarago/postgis:13-3.2`
        - `ghcr.io/vincentsarago/postgis:14-3.2`
        - `ghcr.io/vincentsarago/postgis:13-3.1`
        - `ghcr.io/vincentsarago/postgis:14-3.1`

- **uvicorn/gunicorn** (code from https://github.com/tiangolo/uvicorn-gunicorn-docker)
    - Base: `bitnami/python:${PYTHON_VERSION}` (~600MB)
    - Images:
        - `ghcr.io/vincentsarago/uvicorn-gunicorn:3.8`
        - `ghcr.io/vincentsarago/uvicorn-gunicorn:3.9`
        - `ghcr.io/vincentsarago/uvicorn-gunicorn:3.10`
        - `ghcr.io/vincentsarago/uvicorn-gunicorn:3.11`
        - `ghcr.io/vincentsarago/uvicorn-gunicorn:3.12`

- **hypercorn**
    - Base: `bitnami/python:${PYTHON_VERSION}` (~600MB)
    - Images:
        - `ghcr.io/vincentsarago/hypercorn:3.8`
        - `ghcr.io/vincentsarago/hypercorn:3.9`
        - `ghcr.io/vincentsarago/hypercorn:3.10`
        - `ghcr.io/vincentsarago/hypercorn:3.11`
        - `ghcr.io/vincentsarago/hypercorn:3.12`

### Motivation

With the new Mac OS M1, docker images have to be specifically built for `arm64` architecture to fully work as expected. While maintainers and contributors of the original repositories work to make those available (e.g. PR still in review) I found myself blocked which is why I decided to published both `postgis` and `uvicorn-gunicorn` docker images compatible with `linux/amd64` and `linux/arm64` architectures here.
