#!/bin/sh

sed -E "/http_agent: nfc-phpipam-scan-agent/s/\/(.+)/\/$(cz version --project)/g" -i playbooks/tasks/scan_subnet.yaml;

git add playbooks/tasks/scan_subnet.yaml;

git status;

sed -E "/http_agent: nfc-phpipam-scan-agent/s/\/(.+)/\/$(cz version --project)/g" -i playbooks/tasks/api_call.yaml;

git add playbooks/tasks/api_call.yaml;

git status;
