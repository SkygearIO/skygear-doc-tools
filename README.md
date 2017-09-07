# skygear-doc-tools
skygear-doc-tools is an utility to generate and upload documentation.

## Installation
`sudo pip install git+https://github.com/SkygearIO/skygear-doc-tools.git@master`

## Usage
### Create Docker Image (Android & JS) Only
- js `create-docker-image --platform js`
- Android  `create-docker-image --platform android`
### Generating Documentation
- js `generate-js-doc --pwd $PWD --docker`
- Android `generate-android-doc --pwd $PWD --src-dir ./chat/src/main/java --package io.skygear.plugins.chat --dst-dir ./javadoc --docker`
- iOS `generate-ios-doc --pwd $PWD`
### Publish Documentation to S3 (Make sure awscli is installed)
`publish-doc --platform ios --pwd $PWD  --doc-dir $PWD/jazzy_docs --bucket $BUCKET --prefix $PREFIX --version $VERSION --distribution-id $DISTRIBUTION_ID`
