# Gremlin Server Proxy 

Proxy layer for Apache TinkerPop's Gremlin Server. 


[![Apache license](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/invanalabs/gremlin-server-proxy/blob/master/LICENSE) 
[![Build Status](https://travis-ci.org/invanalabs/gremlin-server-proxy.svg?branch=master)](https://travis-ci.org/invanalabs/gremlin-server-proxy)
[![Docker pulls](https://img.shields.io/docker/pulls/invanalabs/gremlin-server-proxy)](https://hub.docker.com/r/invanalabs/gremlin-server-proxy)
[![Docs](https://img.shields.io/badge/docs-latest%20version-blue)](https://invana.io/docs.html)


## 1. Installation


| Environment Variable        | default           | Example                            |
| --------------------------- |:-----------------:| ----------------------------------:|
| GREMLIN_HOST                | null              | http://127.0.0.1:8182, https://api.domain.io |
 
 
**Note** Currently only http hosts are acceptable.

##### 1.1 Run from docker image
```shell script
docker run -p 9600:9600 -d --name gremlin-server-proxy invanalabs/gremlin-server-proxy
```
##### 1.2 Build your own docker
```shell script
git clone git@github.com:invanalabs/gremlin-server-proxy.git
cd gremlin-server-proxy
docker build . -t gremlin-server-proxy 
docker run --name gremlin-server-proxy -d -p 9600:9600 -e GREMLIN_HOST="http://127.0.0.1:8182" gremlin-server-proxy 
```

## 2. License 

Apache License 2.0

## 3. Support

For any further queries or dedicated support, please feel free to get in touch with me at hi[at]invana.io.

