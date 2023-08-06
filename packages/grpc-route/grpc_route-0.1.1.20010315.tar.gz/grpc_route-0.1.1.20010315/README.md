# grpc_route

## Installation
```shell
 pip install grpc_route
```
## Usage
server run:
```

from grpc_route.server import Router

app = Router()


@app.route("index")
def test(n):
    # n / 0
    print("-> to index: ", n)
    return "server back ->"


if __name__ == "__main__":
    app.run_forever("0.0.0.0", port=5656)
```
   
client run:
```
from grpc_route.client import RouteClient
from grpc_route import AddrConf

addr1 = AddrConf("127.0.0.1", 5656)
app = RouteClient(addr1)
app.connect()


@app.register(handler="index", to_addr=addr1)
def run_index(n):
    pass
```