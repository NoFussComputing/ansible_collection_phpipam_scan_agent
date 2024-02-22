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

The variables described below, if optional the value specified here is the default value. All variables that are used by the server component are environmental variables that must be set before execution. Ansbible variable name is enclused in `[]`

``` bash
# phpIPAM Scan Agent Settings
SCANNER_TOKEN=         # Mandatory, String client api token to connect to phpIPAM API [client_token]
SCANNER_NAME=          # Mandatory, String. The scanner name as set in phpIPAM interface [client_name]
SCANNER_CODE=          # Mandatory, String. Scan Agent Code as set in phpIPAM interface [scanagent_code]

# phpIPAM MariaDB/MySQL Variables
MYSQL_HOST=            # Mandatory, String. IP/DNS of host to connect. [nfc_c_mysql_host]
MYSQL_PORT=3306        # Optional, Integer. port to use for connection. [nfc_c_mysql_port]
MYSQL_USER=            # Mandatory, String. User to authenticate with. [nfc_c_mysql_user]
MYSQL_PASSWORD=        # Mandatory, String. Password for the user to connect with. [nfc_c_mysql_password]


# Server Component Variables
HTTP_PORT=5000         # Optional, Integer. The port for the Server component to listen for connections.

```


#### phpIPAM Interface variable Mapping

These images are of the phpIPAM interface that show in green text the variable name that would be set as detailed above.

![phpIPAM API](images/phpipam_api.png)

phpIPAM API Settings

----

![phpIPAM Scan Agent](images/phpipam_scan_agent_details.png)

phpIPAM Scan Agent Settings


# Workflow

The Server componet has the following workflow:

1. Receive the Scanner component report.

1. check if the Scanner Code is in the DB

    - _if no results found, no further processing occurs_

1. Confirm the subnet scanned is assigned to the scanner

    - _if no results found, no further processing occurs_

1. Update the phpIPAM MariaDB/MySQL database directly
