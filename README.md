# Gremlin Server Proxy 

Proxy layer for Apache TinkerPop's Gremlin Server. 


[![Apache license](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/invanalabs/gremlin-proxy/blob/master/LICENSE) 
[![Docker pulls](https://img.shields.io/docker/pulls/invanalabs/gremlin-proxy)](https://hub.docker.com/r/invanalabs/gremlin-proxy)
[![Docs](https://img.shields.io/badge/docs-latest%20version-blue)](https://invana.io/docs.html)


## Installation


| Environment Variable        | default           | Example                            |
| --------------------------- |:-----------------:| ----------------------------------:|
| GREMLIN_HOST                | null              | http://127.0.0.1:8182, https://api.domain.io |
 
 
**Note** Currently only http hosts are acceptable.

##### Run from docker image
```shell script
docker run -p 9600:9600 -d --name gremlin-proxy invanalabs/gremlin-proxy
```
##### Build your own docker
```shell script
git clone git@github.com:invanalabs/gremlin-proxy.git
cd gremlin-proxy
docker build . -t gremlin-proxy 
docker run --name gremlin-proxy -d -p 9600:9600 -e GREMLIN_HOST="http://127.0.0.1:8182" gremlin-proxy 
```

## License 

Apache License 2.0

## Support

For any further queries or dedicated support, please feel free to get in touch with me at hi[at]invana.io.

