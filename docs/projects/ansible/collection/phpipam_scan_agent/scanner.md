---
title: phpIPAM Scanner
description: No Fuss Computings {php}IPAM Scan Agent scenner component
date: 2024-02-20
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible/collections/phpipam_scan_agent
---

The Scan Agent Scanner component is intended to scan networks that are assigned to it by the phpIPAM server. It can be installed and ran from any host that is capable of running python. The scan agent only requires that there be `nmap` installed as this is the package that conducts the network scanning.


## Usage

Ensure that the `namp` package is installed, install and configure the collection. Running the agent is as simple as running the following command:

``` bash

ansible-playbook nofusscomputing.phpipam_scan_agent.agent

```

_See below for the variable details_


### phpIPAM API

The scanner component requires API access to phpIPAM. THe API user that is used, must only be given read only access to the API.


### Variables

Variables for the scanner are set in a variables file at path `/etc/phpipam/scan_agent.yaml`. The variables described below, if optional the value specified here is the default value.

``` yaml
nofusscomputing_phpipam_scan_agent:

  api_url:                           # Mandatory, String. url with protocol of the phpIPAM API to connect to.

  http_port: 5000                    # Optional, Integer. http port to connect to the server.
  http_server: http://127.0.0.1      # Optional, Integer. url with protocol of the Scan Server to connect to.
  auth_token:                        # Optional, String. The Scan-Agent server authentication token.

  cache_expire_time: 1800            # Optional, Integer. Time in seconds to expire the phpIPAM cache.
  epoch_time_offset: 0               # optional, int. Value in seconds to offset the time

# phpIPAM Scan Agent Settings
  client_token:                      # Mandatory, String client api token to connect to phpIPAM API
  client_name:                       # Mandatory, String. The scanner name as set in phpIPAM interface
  scanagent_code:                    # Mandatory, String. Scan Agent Code as set in phpIPAM interface


```

!!! tip
    You can specify environmental variable `ANSIBLE_LOG_PATH=/var/log/ansible.log`, which will tell the scanner component to log to a file at path `/var/log/ansible.log`


#### phpIPAM Interface variable Mapping

These images are of the phpIPAM interface that show in green text the variable name that would be set as detailed above.

![phpIPAM API](images/phpipam_api.png)
phpIPAM API Settings

----

![phpIPAM Scan Agent](images/phpipam_scan_agent_details.png)
phpIPAM Scan Agent Settings


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


## Remote network Scannning

Once the [server component](server.md#remote-network-scannning) has been setup, the client can be installed/used from any network. Even a network that is isolated from the server. Only caveat is that the client can communicate with the server. To ensure that the client can connect to the server set the `auth_token` to match that of the server.

There is no true confirmation of the servers identity outside of confirming the TLS Certificate is trusted. Due to this fact, you're advised to use your own CA to sign the server components TLS Certificate. By doing this only you can issue a certificate to the server component. All that is required is to ensure that [your CA certificate](docker.md#custom-ca-certificate) is within the [trusted certificates](../../../itil/runbooks/linux/custom_ca.md) of the machine that is running the agent.

!!! danger "Security"
    Failing to secure the server component communication with TLS will allow anyone with direct access to the line of communication to view the `auth_token`. Anyone who has the `auth_token` will be able to upload data to the server.

    In an attempt to mitigate this, the scanner will fail to communicate with the server if you have set an `auth_token` and attempt non-TLS communication with the server.
