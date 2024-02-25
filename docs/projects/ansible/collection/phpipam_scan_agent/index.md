---
title: phpIPAM Scan Agent
description: No Fuss Computings {php}IPAM Scan Agent for local and remote networks
date: 2024-02-20
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent
---

<span style="text-align: center;">

![Project Status - Active](https://img.shields.io/badge/Project%20Status-Active-green?logo=gitlab&style=plastic)


![branch release version](https://img.shields.io/badge/dynamic/yaml?color=ff782e&logo=gitlab&style=plastic&label=Stable%20Release&query=%24.commitizen.version&url=https%3A//gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent%2F-%2Fraw%2Fmaster%2F.cz.yaml) 
![branch release version](https://img.shields.io/badge/dynamic/yaml?color=ff782e&logo=gitlab&style=plastic&label=Dev%20Release&query=%24.commitizen.version&url=https%3A//gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent%2F-%2Fraw%2Fdevelopment%2F.cz.yaml)


[![Downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv3%2Fplugin%2Fansible%2Fcontent%2Fpublished%2Fcollections%2Findex%2Fnofusscomputing%2Fphpipam_scan_agent%2F&query=%24.download_count&style=plastic&logo=ansible&logoColor=white&label=Galaxy%20Downloads&labelColor=black&color=cyan)](https://galaxy.ansible.com/ui/repo/published/nofusscomputing/phpipam_scan_agent/)
[![Docker Pulls](https://img.shields.io/docker/pulls/nofusscomputing/phpipam-scan-agent?style=plastic&logo=docker&logoColor=0db7ed&color=0db7ed)](https://hub.docker.com/r/nofusscomputing/phpipam-scan-agent)


</span>

A phpIPAM scan agent designed for both local and remote network scanning. This Ansible Collection contains all of the componets required to launch a scan agent that will report back to the phpIPAM server. This collection is also built into it's own docker container and is [available on Docker Hub](https://hub.docker.com/r/nofusscomputing/phpipam-scan-agent).

This collection has been broken down into two components, a [server](server.md) and a [scanner](scanner.md). The scanner as the name implies will scan the networks assigned to it by phpIPAM and on completing a scan of a subnet, will post the results to the Server component which will process the results, and update the phpIPAM MySQL/MariaDB database directly.


## Installation

This collection is available on Ansible Galaxy and can be installed with `ansible-galaxy collection install nofusscomputing.phpipam_scan_agent`. When installing all of the required dependencies are installed.

Prefer to use our [docker](docker.md) image? It's available on Docker Hub `docker pull nofusscomputing/phpipam-scan-agent:latest`.

There is no timezone support within phpIPAM. Due to this it's recommended that you setup phpIPAM, the database and the scanner component to use UTC (GMT +00:00) timezone or that all components be setup to use the same timezone.


## Features

The following features are available or planned to be implmented:

- Discover new hosts

- [**ToDo** Execute scan from remote host](https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent/-/issues/7)

- [**ToDo** Hosts check](https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent/-/issues/3)

- [**ToDo** Host Self-Update](https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent/-/issues/2)

- MAC Address updating*

    !!! info
        It's only possible to obtain a MAC Address if the scanner is on the same L2 network (Broadcast Domain). Within the docs you will find the different methods available to achieve this.

- Remote Network Scanning

- [Resolve DNS names](index.md#Resolve-dns-names)

- [Timezone Normalization](server.md#timezone-normalization)


## phpIPAM Features

This section describes the phpIPAM settings and what they each do for the scanner/server component. Regardless of any setting detailed below, unless otherwise specified. If the scan agent is not assigned to the subnet, the subnet will not be scanned.


### Discover new hosts

- Location `Subnet -> Discover new hosts`

When this setting is enabled, the scanner will scan the entire subnet that has been assigned to it. Every host that is found is updated in phpIPAM.

!!! note
    the work in [Hosts check](https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent/-/issues/3), will adjust this behaviour to only add hosts that dont exist.


 - Location `Subnet -> Discover new hosts [Last discovery time]` 

This is displayed within the subnet interface next to the `Discover new hosts` field. Whenever a scan report is received by the server this filed is updated to reflect the last scan time.


### Resolve DNS names

- Location `Subnet -> Resolve DNS names`

When this setting is enabled, DNS resolution for the hostname for any IP found will be conducted. If you have setup nameservers (`Administration -> Nameservers`) and assigned them to the subnet, they will be used for name resolution. If no nameservers are configured for the subnet, the host's nameservers where the scanner is running from will be used. BY default within phpIPAM, DNS Resolution is turned off for a subnet and as such the scanner will not resolve IP address DNS names.

!!! info
    The FQDN for an IP that is retured is not used as the hostname. **Only** the first octet. i.e. if the reverse DNS lookup returns a FQDN of `my_hostname.domainname.tld`, the hostname for the IP address will be set to `my_hostname`


### Scan Agent

- Location `Administration -> Scan agents [Last access]`

This is displayed within the Scan Agent table in column `Last access`. When ever the scanner checks in, the time of the checkin is used to update the field.

- Location `Subnet -> Scan agent [Last Check]`

This is displayed within the subnet interface next to `Scan agent` field. When ever the scanner checks in, the time of the checkin is used to update the field.


## Development Notes

Contributions to this project are welcome. Below you will find some useful commands for use during development.

``` bash
# To build the container. ensure the changes are commited and push to you feature branch
docker build . --tag scan-agent:dev --build-arg  COLLECTION_BRANCH=<your feature branch name> --build-arg COLLECTION_COMMIT=$(git log -n1 --format=format:"%H")


# Launch your build container
docker run \
    -d \
    -v "./scan_agent.yaml:/etc/phpipam/scan_agent.yaml" \
    -v "./scan_server.yaml:/etc/phpipam/scan_server.yaml" \
    -e "ANSIBLE_LOG_PATH=/var/log/ansible.log" \
    -p "5000:5000" \
    --name scan-agent \
    scan-agent:dev;

# remove launched dev container
docker rm --force scan-agent

```

Our docker build file has been designed so that during development it will pull from the repository branch as specified to find the collection to install. if you fail to specify your feature branch, the collection will not install the work you have been doing.
