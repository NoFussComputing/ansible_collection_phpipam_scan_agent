---
title: phpIPAM Scanner
description: No Fuss Computings {php}IPAM Scan Agent scenner component
date: 2024-02-20
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent
---

The Scan Agent Scanner component is intended to scan networks that are assigned to it by the phpIPAM server. It can be installed and ran from any host that is capable of running python.


## Usage

After installing the collection, running the agent is as simple as running the following command:

``` bash

ansible-playbook nofusscomputing.phpipam_scan_agent.agent \
  --extra-vars "api_url=<your value here>" \
  --extra-vars "client_token=<your value here>" \
  --extra-vars "client_name=<your value here>" \
  --extra-vars "scanagent_code=<your value here>"

```

_See below for the variable details_


### Variables

The variables described below, if optional the value specified here is the default value. Any variable that can be set via environmental variables have the variable name enclosed in `[]`

``` yaml

client_token: ""                       # Mandatory, String client api token to connect to phpIPAM API [SCANNER_TOKEN]
client_name: ""                        # Mandatory, String. The scanner name as set in phpIPAM interface [SCANNER_NAME]
scanagent_code: ""                     # Mandatory, String. Scan Agent Code as set in phpIPAM interface [SCANNER_CODE]


nfc_c_http_port: 5000                  # Optional, Integer. http port to connect to the server. [HTTP_PORT]
nfc_c_http_server: http://127.0.0.1    # Optional, Integer. url with protocol of the Scan Server to connect to. [HTTP_URL]


api_url: http://127.0.0.1              # Optional, String. url with protocol of the phpIPAM API to connect to. [API_URL]


nfc_c_cache_expire_time: 1800          # Optional, Integer. Time in seconds to expire the phpIPAM cache.
nfc_c_epoch_time_offset: 0             # optional, int. Value in seconds to offset the time

```

!!! tip
    You can specify environmental variable `ANSIBLE_LOG_PATH=/var/log/ansible.log`, which will tell the scanner component to log to a file at path `/var/log/ansible.log`


## Workflow

The scanner component has the following workflow:

1. Expire cache, if cache expiry has elapsed.

1. Fetch from the phpIPAM API, the subnets assigned to it. _results are cached_

1. Fetch ALL address' from phpIPAM API, that are assosiated with agent subnets. _results are cached_

1. For each network:

    1. conduct Scan of network.

        !!! info
            The following details are included in the scan report:
    
            - IP Address
    
            - MAC Address* _Only if the scanner is on the same L2 network (Broadcast Domain)_

    1. Re-format nmap scan report to format Server component recognizes.

    1. upload scan report to configured Server.

1. workflow complete.
