

DOCKER_TAG=$1

if [[ -z $DOCKER_TAG ]]
then
	echo "You should pass docker tag as an argument; ex: sh build_image.sh alpha"
	exit 1
fi

docker build . -t invanalabs/gremlin-proxy
docker tag invanalabs/gremlin-proxy invanalabs/gremlin-proxy:"$DOCKER_TAG"
docker tag invanalabs/gremlin-proxy invanalabs/gremlin-proxy:latest
docker push invanalabs/gremlin-proxy:"$DOCKER_TAG"
docker push invanalabs/gremlin-proxy:latest
