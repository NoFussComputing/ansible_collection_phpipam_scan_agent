## 0.3.0 (2024-02-25)

### Feat

- **server**: DNS Reverse Lookup for IP Address'
- **server**: Convert scanned time within scan report to UTC

### Fix

- **ci**: http user_agent version set during version bump
- **server**: Time of last access for scan agent to use 'now'

## 0.2.0 (2024-02-24)

### Feat

- **server**: Update the time of last access for scan agent
- **scanner**: Add scanner timezone to scan report
- **scanner**: don't include PTR DNS records as hostname
- **scanner**: for ssl cert validation when uploading to server
- **scanner**: if an auth token has been set, fail non-https communication with server
- **scanner**: Set user http user agent to <name>/<version>
- **server**: scanner identity confirmation
- **server**: update subnet discovery date/time
- **server**: move config of variables to vars file
- **agent**: move config of variables to vars file
- **server**: if hostname in scan report, update the database
- **agent**: if hostname present in nmap scan report, add to report for server
- **agent**: showsubnet address in logs when conducting subnet actions
- **server**: show ip address in logs when updating an ip address
- **api_call**: before returning check if cached file exists

### Fix

- **server**: use correct sql syntax to insert ipaddress
- **agent**: only attempt to scan subnet if subnets were returned
- **agent**: cater for api call that returns nothing
- **docker**: ensure correct variable used to install package
- **build**: ensure the correct tags and architectures are published

### Refactor

- **server**: don't process scan results in parallel
- **api_call**: use var name that makes more sense

## 0.1.1 (2024-02-21)

### Fix

- **ci**: use correct collection name

## 0.1.0 (2024-02-21)

### Feat

- **docker**: adjust scanner job to run every 5 mins

### Fix

- **ci**: ensure docker publish uses correct tag
- **ci**: ensure correct github sync repo is used
- **ci**: ensure docker build and publish occurs
- Don't process results if scan report is empty
