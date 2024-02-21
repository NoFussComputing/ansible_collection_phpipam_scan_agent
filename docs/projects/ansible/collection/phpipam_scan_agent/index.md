---
title: phpIPAM Scan Agent
description: No Fuss Computings {php}IPAM Scan Agent for local and remote networks
date: 2024-02-20
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent
---

<span align="center">

![Project Status - Active](https://img.shields.io/badge/Project%20Status-Active-green?logo=gitlab&style=plastic)

[![Latest Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv3%2Fplugin%2Fansible%2Fcontent%2Fpublished%2Fcollections%2Findex%2Fnofusscomputing%2Fphp_scan_agent%2F&query=%24.highest_version.version&style=plastic&logo=ansible&logoColor=white&label=Latest%20Release&labelColor=black&color=cyan)](https://galaxy.ansible.com/ui/repo/published/nofusscomputing/ci_test_collection/)
![Downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv3%2Fplugin%2Fansible%2Fcontent%2Fpublished%2Fcollections%2Findex%2Fnofusscomputing%2Fphp_scan_agent%2F&query=%24.download_count&style=plastic&logo=ansible&logoColor=white&label=Downloads&labelColor=black&color=cyan)

[![Docker Image Version](https://img.shields.io/docker/v/nofusscomputing/phpipam-scan-agent?sort=semver&style=plastic&logo=docker&logoColor=0db7ed&color=0db7ed&label=Latest%20Release)](https://hub.docker.com/r/nofusscomputing/phpipam-scan-agent)
[![Docker Pulls](https://img.shields.io/docker/pulls/nofusscomputing/phpipam-scan-agent?style=plastic&logo=docker&logoColor=0db7ed&color=0db7ed)](https://hub.docker.com/r/nofusscomputing/phpipam-scan-agent)


</span>

A phpIPAM scan agent designed for both local and remote network scanning. This Ansible Collection contains all of the componets required to launch a scan agent that will report back to the phpIPAM server. This collection is also built into it's own docker container and is [available on Docker Hub](https://hub.docker.com/r/nofusscomputing/phpipam-scan-agent).

This collection has been broken down into two components, a server and a scanner. The scanner as the name implies will scan the networks assigned to it by phpIPAM and on completing a scan of a subnet, will post the results to the Server component which will process the results, and update the phpIPAM MySQL/MariaDB database directly.


## Installation

This collection is available on Ansible Galaxy and can be installed with `ansible-galaxy collection install nofusscomputing.phpipam_scan_agent`. When installing all of the required dependencies are installed.

Prefer to use our docker image? It's available on Docker Hub `docker pull nofusscomputing/phpipam-scan-agent:latest`.


## Features

Currenty this collection has the following features:

- Discover new hosts

- [**ToDo** Hosts check](https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent/-/issues/3)

- [**ToDo** Host Self-Update](https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent/-/issues/2)

- MAC Address updating*

    !!! info
        It's only possible to obtain a MAC Address if the scanner is on the same L2 network (Broadcast Domain). Within the docs you will find the different methods available to achieve this.

- [**ToDo** Remote Network Scanning](https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent/-/issues/1)

- [**ToDo** Resolve DNS names](https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent/-/issues/4)

