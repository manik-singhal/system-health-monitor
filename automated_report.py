from system_health_check import generate_report, send_email

report_file = generate_report()

send_email(report_file)

