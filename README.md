# Gremlin Server Proxy 

Proxy layer for Apache TinkerPop's Gremlin Server to enable Cross Origin Resource Sharing (CORS). 
To support their authentication abilities from web browsers enabling CORS. 

[![Apache license](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/invanalabs/gremlin-proxy/blob/master/LICENSE) 
[![Docker pulls](https://img.shields.io/docker/pulls/invanalabs/gremlin-proxy)](https://hub.docker.com/r/invanalabs/gremlin-proxy)
[![Docs](https://img.shields.io/badge/docs-latest%20version-blue)](https://invana.io/docs.html)

Please refer [documentation](https://invana.io/docs/gremlin-proxy/01-get-started) to get started.


![Overview Diagram](./diagram.png "Overview Diagram")


This project let's you connect to your favorite Gremlin Server using connection 
strings from the web browsers. This service doesn't add any layer of security, 
it just avoids the CORS issue. They layer would forward the `Content-Type` and `Authorization`
headers to your gremlin server.

**Note:** This may not be the best implementation for production use. 




## License 

Apache License 2.0

## Support

For any further queries or dedicated support, please feel free to get in touch with me at hi[at]invana.io.

