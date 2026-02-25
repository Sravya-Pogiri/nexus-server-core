#!/bin/bash

echo "Starting Nexus System Health Check..."
echo "------------------------------------"

# Check Python environment
if command -v python3 &>/dev/null; then
    echo "[OK] Python 3 is installed."
else
    echo "[FAIL] Python 3 not found."
fi

# Check Disk Space
echo "[INFO] Checking disk usage..."
df -h | grep '^/dev/'

echo "------------------------------------"
echo "Health check complete."
