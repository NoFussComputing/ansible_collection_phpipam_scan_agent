---
title: phpIPAM Scan Server
description: No Fuss Computings {php}IPAM Scan Agent Server component
date: 2024-02-20
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent
---

The Scan Agent Server component is intended to act as the go between for the Scanner component and phpIPAM.


## Usage

After installing the collection, running the server is as simple as running the following command:

``` bash

ansible-rulebook -r nofusscomputing.phpipam_scan_agent.agent_receive

```


### Variables

The variables described below, if optional the value specified here is the default value. The variables are to be set in a variables file at path `/etc/phpipam/scan_server.yaml`

``` yaml

nofusscomputing_phpipam_scan_server:

  # phpIPAM MariaDB/MySQL Variables
  mysql_host:         # Mandatory, String. IP/DNS of host to connect.
  mysql_port: 3306    # Optional, Integer. port to use for connection.
  mysql_user:         # Mandatory, String. User to authenticate with.
  mysql_password:     # Mandatory, String. Password for the user to connect with.


  # Server Component Variables
  http_port: 5000     # Optional, Integer. The port for the Server component to listen for connections.
  auth_token:         # Optional, String. Token used to authentication Agents.

```


## Workflow

The Server componet has the following workflow:

1. Receive the Scanner component report.

1. check if the Scanner Code is in the DB

    - _if no results found, no further processing occurs_

1. Confirm the subnet scanned is assigned to the scanner

    - _if no results found, no further processing occurs_

1. Update the phpIPAM MariaDB/MySQL database directly


## Remote network Scannning

Remote network scanning is possible with the Scan-Agent. The server must be setup and have connectivity to the phpIPAM MariaDB/MySQL database. Currently the server does not perform secure communication. As such you are strongly encouraged to setup the server component behind a reverse proxy that conducts the TLS termination.

The [scan](scanner.md#remote-network-scannning) and server component must be setup with the same `auth_token`. It is this token that provides a means to ensure that what the server is receiving, is from an authorized client.

!!! danger "Security"
    Failing to secure the server component communication with TLS will allow anyone with direct access to the line of communication to view the `auth_token`. Anyone who has the `auth_token` will be able to upload data to the server.
