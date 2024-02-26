---
title: phpIPAM Scan Agent Docker Container
description: No Fuss Computings {php}IPAM Scan Agent Docker Container
date: 2024-02-21
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent
---

The Scan Agent Docker container has the Ansible collection installed which when launched will by default, start a Scan Server and scanner. The components running inside the container can be customised to suit different use cases.

The Container has been setup to use supervisord, with the server and cron setup as the two available services. Due to the simplicity of supervisord, the container does have a healthcheck, that on failure means one or both of the services have failed.


## Usage

Launching the docker container can be done with

``` bash

docker run \
    -d \
    -p "5000:5000" \
    -v "./scan_agent.yaml:/etc/phpipam/scan_agent.yaml" \
    -v "./scan_server.yaml:/etc/phpipam/scan_server.yaml" \
    -v "./my-custom-ca.crt:/usr/local/share/ca-certificates/my-custom-ca.crt:ro"
    --name scan-agent \
    nofusscomputing/phpipam-scan-agent:latest;

```

Variables must still be set for the running container, please review the [Scanner](scanner.md) or [Server](server.md) documentation as appropriate.


### Logs

When viewing the container logs `docker logs <container name>`, what you will see is the Server component logs. This is by design. If however you are also running the scanner component, as is the default. To view those logs you will need to ensure that when launching the container that you specify environmental variable `ANSIBLE_LOG_PATH=/var/log/ansible.log`. This tells the scanner component to log to file at path `/var/log/ansible.log`.

During the build of the container environmental variable `ANSIBLE_FORCE_COLOR='true'` is set, this enables the playbooks to be in colour when viewing the container logs. If this is not desired, set the variable to `ANSIBLE_FORCE_COLOR='false'` when launching the container.


### Custom CA Certificate

When the container starts or restarts a script runs that updates the containers trusted CA certificates. Details for mounting a/an certificate(s) is detailed below.


### Volumes

To configure the components, the following files will need to be mounted within the container:

- Custom CA certificate at path `/usr/local/share/ca-certificates/`. you can mount a single `crt` file or multiple if you use a sub-directory at this path.

- scanner config file at path `/etc/phpipam/scan_agent.yaml`, see [scanner docs](scanner.md#variables) for details.

- server config at path `/etc/phpipam/scan_server.yaml`, see [server docs](server.md#variables) for details.

If you wish to customize the cronjob for the scan component within the container, mount a new cron file to path `/etc/cron.d/scanner`. The default cron file is as follows:

``` yaml title="/etc/cron.d/scanner" linenums="1"

--8<-- "includes/etc/cron.d/scanner"

```
