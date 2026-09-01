import platform
import socket
import os
import getpass
import shutil
import time
from datetime import datetime


def get_system_info():
    """Collect basic operating system information."""

    return {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Architecture": platform.machine(),
        "Processor": platform.processor() or "Not available",
        "Hostname": socket.gethostname(),
        "Username": getpass.getuser(),
        "Python Version": platform.python_version(),
    }


def get_cpu_info():
    """Collect CPU information."""

    logical_cpus = os.cpu_count()

    return {
        "Logical CPU Cores": logical_cpus if logical_cpus else "Not available",
    }


def get_memory_info():
    """
    Get basic memory information.

    Uses platform-independent standard-library functionality
    where possible.
    """

    try:
        import ctypes

        class MemoryStatus(ctypes.Structure):
            _fields_ = [
                ("length", ctypes.c_ulong),
                ("memory_load", ctypes.c_ulong),
                ("total_phys", ctypes.c_ulonglong),
                ("avail_phys", ctypes.c_ulonglong),
                ("total_page_file", ctypes.c_ulonglong),
                ("avail_page_file", ctypes.c_ulonglong),
                ("total_virtual", ctypes.c_ulonglong),
                ("avail_virtual", ctypes.c_ulonglong),
                ("avail_extended_virtual", ctypes.c_ulonglong),
            ]

        status = MemoryStatus()
        status.length = ctypes.sizeof(MemoryStatus)

        if hasattr(ctypes, "windll"):
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status))

            total_gb = status.total_phys / (1024 ** 3)
            available_gb = status.avail_phys / (1024 ** 3)
            used_gb = total_gb - available_gb

            return {
                "Total RAM": f"{total_gb:.2f} GB",
                "Available RAM": f"{available_gb:.2f} GB",
                "Used RAM": f"{used_gb:.2f} GB",
                "Memory Usage": f"{status.memory_load}%",
            }

    except (OSError, AttributeError, TypeError):
        pass

    # Linux fallback using /proc/meminfo
    try:
        with open("/proc/meminfo", "r", encoding="utf-8") as file:
            memory_data = {}

            for line in file:
                key, value = line.split(":", 1)
                memory_data[key] = int(value.strip().split()[0])

            total_kb = memory_data.get("MemTotal", 0)
            available_kb = memory_data.get("MemAvailable", 0)

            if total_kb:
                total_gb = total_kb / (1024 ** 2)
                available_gb = available_kb / (1024 ** 2)
                used_gb = total_gb - available_gb
                usage = (used_gb / total_gb) * 100

                return {
                    "Total RAM": f"{total_gb:.2f} GB",
                    "Available RAM": f"{available_gb:.2f} GB",
                    "Used RAM": f"{used_gb:.2f} GB",
                    "Memory Usage": f"{usage:.1f}%",
                }

    except (FileNotFoundError, PermissionError, ValueError, OSError):
        pass

    return {
        "Total RAM": "Not available",
        "Available RAM": "Not available",
        "Used RAM": "Not available",
        "Memory Usage": "Not available",
    }


def get_disk_info():
    """Collect information about mounted disks."""

    disks = []

    # Windows commonly uses drive letters.
    if os.name == "nt":
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            drive = f"{letter}:\\"

            if os.path.exists(drive):
                try:
                    total, used, free = shutil.disk_usage(drive)

                    disks.append({
                        "Drive": drive,
                        "Total": format_bytes(total),
                        "Used": format_bytes(used),
                        "Free": format_bytes(free),
                        "Usage": f"{(used / total) * 100:.1f}%"
                        if total else "N/A",
                    })

                except OSError:
                    continue

    else:
        # Linux/macOS root filesystem.
        mount_points = ["/"]

        # macOS commonly has /System/Volumes/Data.
        if platform.system() == "Darwin":
            mount_points.append("/System/Volumes/Data")

        for mount in mount_points:
            if os.path.exists(mount):
                try:
                    total, used, free = shutil.disk_usage(mount)

                    disks.append({
                        "Drive": mount,
                        "Total": format_bytes(total),
                        "Used": format_bytes(used),
                        "Free": format_bytes(free),
                        "Usage": f"{(used / total) * 100:.1f}%"
                        if total else "N/A",
                    })

                except OSError:
                    continue

    return disks


def format_bytes(size):
    """Convert bytes into a human-readable format."""

    units = ["B", "KB", "MB", "GB", "TB", "PB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} EB"


def get_network_info():
    """Collect basic local network information."""

    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        local_ip = "Not available"

    return {
        "Hostname": hostname,
        "Local IP Address": local_ip,
    }


def get_uptime():
    """Try to determine system uptime."""

    # Linux
    try:
        with open("/proc/uptime", "r", encoding="utf-8") as file:
            uptime_seconds = float(file.readline().split()[0])

            return format_uptime(uptime_seconds)

    except (FileNotFoundError, PermissionError, ValueError, OSError):
        pass

    # Windows
    if os.name == "nt":
        try:
            import ctypes

            milliseconds = ctypes.windll.kernel32.GetTickCount64()
            return format_uptime(milliseconds / 1000)

        except (AttributeError, OSError):
            pass

    return "Not available"


def format_uptime(seconds):
    """Convert seconds into days, hours, minutes and seconds."""

    days = int(seconds // 86400)
    seconds %= 86400

    hours = int(seconds // 3600)
    seconds %= 3600

    minutes = int(seconds // 60)
    seconds = int(seconds % 60)

    return f"{days}d {hours}h {minutes}m {seconds}s"


def get_current_time():
    """Return the current local date and time."""

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def print_section(title):
    """Print a formatted section heading."""

    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def display_system_info():
    """Display operating system information."""

    print_section("🖥️ SYSTEM INFORMATION")

    info = get_system_info()

    for key, value in info.items():
        print(f"{key:<20}: {value}")


def display_cpu_info():
    """Display CPU information."""

    print_section("⚙️ CPU INFORMATION")

    info = get_cpu_info()

    for key, value in info.items():
        print(f"{key:<20}: {value}")


def display_memory_info():
    """Display memory information."""

    print_section("🧠 MEMORY INFORMATION")

    info = get_memory_info()

    for key, value in info.items():
        print(f"{key:<20}: {value}")


def display_disk_info():
    """Display disk information."""

    print_section("💾 DISK INFORMATION")

    disks = get_disk_info()

    if not disks:
        print("No disk information available.")
        return

    for disk in disks:
        print(f"\nDrive: {disk['Drive']}")
        print(f"  Total : {disk['Total']}")
        print(f"  Used  : {disk['Used']}")
        print(f"  Free  : {disk['Free']}")
        print(f"  Usage : {disk['Usage']}")


def display_network_info():
    """Display network information."""

    print_section("🌐 NETWORK INFORMATION")

    info = get_network_info()

    for key, value in info.items():
        print(f"{key:<20}: {value}")


def display_runtime_info():
    """Display uptime and current time."""

    print_section("⏱️ RUNTIME INFORMATION")

    print(f"{'Current Time':<20}: {get_current_time()}")
    print(f"{'System Uptime':<20}: {get_uptime()}")


def main():
    """Main application."""

    print("\n" + "=" * 60)
    print("          🖥️ SYSTEM INFORMATION TOOL")
    print("=" * 60)

    print("\nCollecting system information...")

    try:
        display_system_info()
        display_cpu_info()
        display_memory_info()
        display_disk_info()
        display_network_info()
        display_runtime_info()

    except KeyboardInterrupt:
        print("\n\n⚠️ Operation cancelled by user.")
        return

    except Exception as error:
        print(f"\n❌ An unexpected error occurred: {error}")
        return

    print("\n" + "=" * 60)
    print("✅ Information collection completed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
