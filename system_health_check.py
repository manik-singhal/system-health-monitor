import smtplib
import subprocess
import logging
from email.message import EmailMessage
from datetime import datetime

logging.basicConfig(
    filename = "system_health.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("System health script started.")

def check_disk_usage():
    try:
        result = subprocess.check_output(["df", "-h"], text = True)

        logging.info("Checked disk usage successfully.")

        return result

    except Exception as e:
        logging.error(f"Error checking disk usage: {e}") 
        return "Error collecting disk usage data."   

def check_memory_usage():
    try:
        result = subprocess.check_output(["vm_stat"], text = True)

        logging.info("Checked memory usage successfully.")

        return result

    except Exception as e:
        logging.error(f"Error checking memory usage: {e}")
        return "Error collecting memory usage data."

def check_cpu_usage():
    try:
        result = subprocess.check_output(["top", "-l", "1"], text = True)

        logging.info("Checked CPU usage successfully.")

        return result

    except Exception as e:
        logging.error(f"Error checking CPU usage: {e}")  
        return "Error collecting cpu usage data."  

def monitor_running_services():
    try:
        result = subprocess.check_output(["launchctl", "list"], text = True)

        logging.info("Services monitored successfully.")

        return result

    except Exception as e:
        logging.error(f"Error monitoring services: {e}")  
        return "Error collecting running services data."  

def generate_report():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"health_report_{timestamp}.txt"
        disk_data = check_disk_usage()
        memory_data = check_memory_usage()
        cpu_data = check_cpu_usage()
        services_data = monitor_running_services()

        with open(filename, "w") as report:
            report.write("===== SYSTEM HEALTH REPORT =====\n\n")
            report.write("===== DISK USAGE =====\n")
            report.write(disk_data)
            report.write("\n\n")
            report.write("===== MEMORY USAGE =====\n")
            report.write(memory_data)
            report.write("\n\n")
            report.write("===== CPU USAGE =====\n")
            report.write(cpu_data)
            report.write("\n\n")
            report.write("===== RUNNING SERVICES =====\n")
            report.write(services_data)
            report.write("\n\n")

        logging.info("Health report generated successfully.")

        print(f"\nReport generated successfully: {filename}")

        return filename
                            
    except Exception as e:
        logging.error(f"Error generating report: {e}")  

def send_email(filename):

    try:
        message = EmailMessage()

        message["Subject"] = "System Health Report."
        message["From"] = "yourgmail@gmail.com"   
        message["To"] = "receiversgmail@gmail.com" 

        with open(filename, "r") as file:
            content = file.read()

        message.set_content(content)

        with smtplib.SMTP("smtp.gmail.com", 587, timeout = 30) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login("yourgmail@gmail.com", "your_app_password")
            smtp.send_message(message)

            logging.info("Email sent successfully.")   
            print("\nEmail sent successfully.")

    except Exception as e:
        logging.error(f"Error creating email: {e}")
        print(f"\nError sending email: {e}")

while True:
    print("\n=====SYSTEM HEALTH MENU=====")
    print("1. Check Disk Usage.")
    print("2. Check Memory Usage.")
    print("3. Check CPU Usage.")
    print("4. Check Running Services.")
    print("5. Generate Report.")
    print("6. Exit.")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n===== DISK USAGE =====")
        print(check_disk_usage())

    elif choice == "2":
        print("\n===== MEMORY USAGE =====")
        print(check_memory_usage())

    elif choice == "3":
        print("\n===== CPU USAGE =====")
        print(check_cpu_usage())

    elif choice == "4":
        print("\n===== RUNNING SERVICES =====")
        print(monitor_running_services())

    elif choice == "5": 
        report_file = generate_report()  
        send_email(report_file)

    elif choice == "6":
        print("Exiting System Health Monitor.")
        break  

    else:
        print("Invalid choice. Please try again.")  

              

         
