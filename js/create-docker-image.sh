DOCKER_ORG_NAME="skygeario"
DOCKER_IMAGE="skygear-nodedev"
DOCKER_TAG="latest"

IMAGE_NAME=$DOCKER_ORG_NAME/$DOCKER_IMAGE:$DOCKER_TAG
DIR=`dirname $0`/docker-images/nodedev
docker build -t $IMAGE_NAME $DIR
