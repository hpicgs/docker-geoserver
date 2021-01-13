#!/bin/sh

MAJOR=2
MINOR=18
BUGFIX=1


# Build Geoserver
echo "Building GeoServer ${MAJOR}.${MINOR}.${BUGFIX} "


docker build --build-arg GS_VERSION=${MAJOR}.${MINOR}.${BUGFIX} -t hpicgs/ejpgeoserver:${MAJOR}.${MINOR}.${BUGFIX} .
#docker-registry.hpi3d.de/ejp/ejpgeoserver-docker:${MAJOR}.${MINOR}.${BUGFIX} .

# Build Arguments - To change the defaults when building the image
#need to specify a different value.

#--build-arg WAR_URL=http://downloads.sourceforge.net/project/geoserver/GeoServer/<GS_VERSION>/geoserver-<GS_VERSION>-war.zip
#--build-arg INITIAL_MEMORY=2G
#--build-arg MAXIMUM_MEMORY=8G




