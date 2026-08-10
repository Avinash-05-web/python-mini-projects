import socket

print("=" * 40)
print("        PYTHON PORT SCANNER")
print("=" * 40)

target = input("Enter target IP: ")

start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print(f"\nScanning {target}...")
print(f"Ports: {start_port}-{end_port}\n")

open_ports = []

for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} is OPEN")
        open_ports.append(port)

    sock.close()

print("\n" + "=" * 40)
print("             SCAN COMPLETE")
print("=" * 40)

if open_ports:
    print("Open ports:")
    for port in open_ports:
        print(f"  - {port}")
else:
    print("No open ports found.")