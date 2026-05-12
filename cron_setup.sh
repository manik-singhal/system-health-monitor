#!/bin/bash

CRON_JOB="0 */4 * * * /usr/bin/python3 $(pwd)/automated_report.py"

(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "Cron job added successfully!"

echo "Current crontab:"
crontab -l
