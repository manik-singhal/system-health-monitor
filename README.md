# System Health Monitor

A menu-driven Python-based system health monitoring tool that checks disk, memory, CPU usage, running services, generates reports, and sends email alerts.

---

## Features

- Disk usage monitoring
- Memory usage monitoring
- CPU usage monitoring
- Running services monitoring
- Report generation
- Email alert system
- Automated email reports every 4 hours using cron jobs
- Logging and exception handling

---

## Project Structure

```bash
system_health_check.py   # Main interactive monitoring script
automated_report.py      # Automation script for scheduled reports
setup_cron.sh            # Shell script to configure cron job
```

---

## Run

```bash
python3 system_health_check.py
```

---

## Automated Scheduling Setup

**Give execute permission:**

```bash
chmod +x setup_cron.sh
```

**Run the setup script:**

```bash
./setup_cron.sh
```

This configures a cron job that automatically sends system health reports every 4 hours.

---

## Email Setup

1. Enable **2-Step Verification** on your Google account
2. Generate a **Gmail App Password**
3. Replace the sender email and app password inside the script

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core scripting language |
| Bash | Shell scripting |
| Cron Jobs | Automated scheduling |
| SMTP | Email alert delivery |
| Logging | Error and event tracking |
| Subprocess Module | System command execution |
