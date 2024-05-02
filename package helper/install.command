#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Check for Python 3.9.6 or higher
required_ver="3.9.6"
if [[ $(python3 --version) > $required_ver ]]; then
    echo "${GREEN}Check Passed: Python 3.9.6 or higher is installed.${NC}"
else
    echo "${RED}Please install Python 3.9.6 (recommended) or higher.${NC}"
    exit 1
fi

cd "$(dirname "$BASH_SOURCE")" || {
    echo "${RED}Error getting script directory${NC}" >&2
    exit 1
}

python3 -m pip install -r ./dist/requirements.txt
echo -e "${GREEN}Photo Nexus Installed Successful!${NC}"
