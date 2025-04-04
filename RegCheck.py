import paramiko
import time
import csv

# CUCM SSH credentials
CUCM_IP = "your-cucm-ip"
USERNAME = "admin"
PASSWORD = "your-password"

# Read device names from CSV
def load_device_names(csv_file):
    devices = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            devices.append(row['DeviceName'].strip())
    return devices

def check_phone_status(ssh_client, device_name):
    command = f"show risdb query phone name {device_name}"
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode()
    return output

def main(csv_file):
    devices = load_device_names(csv_file)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(CUCM_IP, username=USERNAME, password=PASSWORD)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Connected to CUCM")

        for device in devices:
            output = check_phone_status(ssh, device)
            print(f"--- Status for {device} ---")
            print(output.strip())
            print()
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 check_cucm_phones.py phones.csv")
    else:
        main(sys.argv[1])