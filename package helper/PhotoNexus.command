GREEN='\033[0;32m'
NC='\033[0m'

cd "$(dirname "$BASH_SOURCE")" || {
    echo "${RED}Error getting script directory${NC}" >&2
    exit 1
}

echo "${GREEN}Launching Photo Nexus...${NC}"
python3 ./dist/mainwindow.py
exit 1