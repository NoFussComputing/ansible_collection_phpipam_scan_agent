---
title: phpIPAM Scan Agent Docker Container
description: No Fuss Computings {php}IPAM Scan Agent Docker Container
date: 2024-02-21
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent
---

The Scan Agent Docker container has the Ansible collection installed which when launched will by default, start a Scan Server and scanner. The components running inside the container can be customised to suit different use cases.


## Usage

Launching the docker container can be done with

``` bash

docker run \
    -d \
    -e "API_URL=<your value here>" \
    -e "MYSQL_HOST=<your value here>" \
    -e "MYSQL_USER=<your value here>" \
    -e "MYSQL_PASSWORD=<your value here>" \
    -e "SCANNER_TOKEN=<your value here>" \
    -e "SCANNER_NAME=<your value here>" \
    -e "SCANNER_CODE=<your value here>" \
    -p "5000:5000" \
    --name scan-agent \
    scan-agent:dev;

```

### Logs

when viewing the container logs `docker logs <container name>`, what you will see is the Server component logs. This is by design. If however you are also running the scanner component, as is the default. To view those logs you will need to ensure that when launching the container that you specify environmental variable `ANSIBLE_LOG_PATH=/var/log/ansible.log`. This tells the scanner component to log to file at path `/var/log/ansible.log`.

