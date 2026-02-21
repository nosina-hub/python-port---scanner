import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"[+] Port {port} is OPEN")

            sock.close()

        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Could not connect to server.")
            break

if __name__ == "__main__":
    try:
        target = input("Enter target IP or domain: ").strip()
        start = int(input("Start port (number only): ").strip())
        end = int(input("End port (number only): ").strip())

        if start < 1 or end > 65535 or start > end:
            print("Invalid port range. Use 1–65535 and make sure start <= end.")
        else:
            scan_ports(target, start, end)

    except ValueError:
        print("❌ Please enter only NUMBERS for ports.")