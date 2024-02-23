## 0.2.0-a2 (2024-02-23)

### Feat

- **server**: update subnet discovery date/time
- **server**: move config of variables to vars file
- **agent**: move config of variables to vars file

### Refactor

- **server**: don't process scan results in parallel

## 0.2.0-a1 (2024-02-22)

### Feat

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

### Refactor

- **api_call**: use var name that makes more sense

## 0.1.2-a1 (2024-02-21)

### Fix

- **build**: ensure the correct tags and architectures are published

## 0.1.1 (2024-02-21)

### Fix

- **ci**: use correct collection name

## 0.1.0 (2024-02-21)

### Feat

- **docker**: adjust scanner job to run every 5 mins
- **docs**: add initial doc layout and CI jobs

### Fix

- **ci**: ensure docker publish uses correct tag
- **ci**: ensure correct github sync repo is used
- **ci**: ensure docker build and publish occurs
- Don't process results if scan report is empty
- **docs**: correct nav link
