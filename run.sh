#!/bin/bash

# Path to your Python script and CSV
CSV_FILE="phones.csv"
PYTHON_SCRIPT="RegCheck.py"

# Log file
LOG_FILE="phone_status_$(date '+%Y%m%d_%H%M%S').log"

# Run the script
echo "Running phone status check at $(date)" >> "$LOG_FILE"
python3 "$PYTHON_SCRIPT" "$CSV_FILE" >> "$LOG_FILE" 2>&1