PWD=$1
DOCS_AWS_BUCKET=$2
DOCS_PREFIX=$3
DOCS_AWS_DISTRIBUTION=$4
DOCKER_RUN="docker run --rm -i -v $1:/usr/src/app -w /usr/src/app skygeario/skygear-nodedev /bin/bash -l -c "
$DOCKER_RUN "rm -rfv esdoc"
$DOCKER_RUN "npm run doc"
VERSION=`$DOCKER_RUN "git describe --always"`
$DOCKER_RUN "aws s3 sync esdoc s3://$DOCS_AWS_BUCKET$DOCS_PREFIX/$VERSION --delete"
$DOCKER_RUN "aws cloudfront create-invalidation --distribution-id $DOCS_AWS_DISTRIBUTION --paths $DOCS_PREFIX/$VERSION/*"

