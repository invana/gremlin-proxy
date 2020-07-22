# Gremlin Server Proxy 

Proxy layer for Apache TinkerPop's Gremlin Server to support their 
authentication abilities from web browsers by solving Cross-origin resource sharing (CORS) issue.

This project let's you connect to your favorite Gremlin Server using connection 
strings from the web browsers. 

[![Apache license](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/invanalabs/gremlin-proxy/blob/master/LICENSE) 
[![Docker pulls](https://img.shields.io/docker/pulls/invanalabs/gremlin-proxy)](https://hub.docker.com/r/invanalabs/gremlin-proxy)
[![Docs](https://img.shields.io/badge/docs-latest%20version-blue)](https://invana.io/docs.html)



## Installation


| Environment Variable        | default           | Example                            |
|:--------------------------- |:-----------------:| ----------------------------------:|
| GREMLIN_HOST                | null              | eg: http://127.0.0.1:8182, https://api.domain.io |
 
**Note** only http hosts are acceptable.

##### Install on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/invanalabs/graph-explorer/tree/master)


##### Run from docker image
```shell script
docker run -p 9600:9600 -e GREMLIN_HOST=http://192.168.0.10:8182 -d --name gremlin-proxy invanalabs/gremlin-proxy 
```

## How to use 


where `awesome-proxy-domain.local` is where this proxy is hosted.

**Note:** This project only handlers CORs issue, You are expected to use your own
 Authentication method on your gremlin server side.



You my extend this to log your

- Log User Events - Query history



## License 

Apache License 2.0

## Support

For any further queries or dedicated support, please feel free to get in touch with me at hi[at]invana.io.

