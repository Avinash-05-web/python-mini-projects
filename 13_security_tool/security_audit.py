#!/usr/bin/env python3

"""
Security Audit Tool
-------------------

A read-only local security auditing utility.

Features:
- System information
- Current user / privilege checks
- Firewall status checks
- Listening network service detection
- Sensitive file permission checks
- SSH configuration checks
- Security-related environment checks
- Security scoring
- PASS / WARNING / CRITICAL findings
- JSON report export
- Cross-platform support where possible

This tool does NOT:
- Modify system configuration
- Disable security controls
- Delete files
- Collect passwords
- Execute arbitrary commands
- Exploit vulnerabilities
"""

from __future__ import annotations

import argparse
import ctypes
import getpass
import hashlib
import json
import os
import platform
import re
import shutil
import socket
import stat
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


# ============================================================
# Configuration
# ============================================================

APP_NAME = "Python Security Audit Tool"
VERSION = "1.0.0"

SUPPORTED_SYSTEMS = {
    "Windows",
    "Linux",
    "Darwin",
}

MAX_READ_SIZE = 1024 * 1024

SENSITIVE_LINUX_FILES = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/group",
    "/etc/sudoers",
    "/etc/ssh/sshd_config",
]

SENSITIVE_WINDOWS_PATHS = [
    os.environ.get("WINDIR", r"C:\Windows"),
]

COMMON_SENSITIVE_FILENAMES = {
    ".env",
    ".git-credentials",
    "id_rsa",
    "id_ed25519",
    "id_ecdsa",
    "credentials",
    "credentials.json",
    "config.json",
}


# ============================================================
# Data Classes
# ============================================================

@dataclass
class Finding:
    """Represents a single security audit finding."""

    category: str
    title: str
    severity: str
    description: str
    recommendation: str


@dataclass
class SystemInfo:
    """Stores basic system information."""

    operating_system: str
    release: str
    version: str
    architecture: str
    hostname: str
    username: str
    python_version: str
    cpu_count: int
    machine: str


# ============================================================
# Global Audit State
# ============================================================

FINDINGS: list[Finding] = []


# ============================================================
# General Helpers
# ============================================================

def add_finding(
    category: str,
    title: str,
    severity: str,
    description: str,
    recommendation: str,
) -> None:
    """Add a security finding."""

    FINDINGS.append(
        Finding(
            category=category,
            title=title,
            severity=severity,
            description=description,
            recommendation=recommendation,
        )
    )


def safe_command(
    command: list[str],
    timeout: int = 5,
) -> tuple[int, str, str]:
    """
    Execute a known, read-only system command.

    This function only receives explicitly defined commands
    from the application and does not invoke a shell.
    """

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            shell=False,
            check=False,
        )

        return (
            result.returncode,
            result.stdout.strip(),
            result.stderr.strip(),
        )

    except (
        FileNotFoundError,
        subprocess.TimeoutExpired,
        OSError,
    ):

        return (
            1,
            "",
            "",
        )


def is_windows() -> bool:
    """Return True when running on Windows."""

    return platform.system() == "Windows"


def is_linux() -> bool:
    """Return True when running on Linux."""

    return platform.system() == "Linux"


def is_macos() -> bool:
    """Return True when running on macOS."""

    return platform.system() == "Darwin"


def is_admin() -> bool:
    """Check whether the current process has administrative privileges."""

    if is_windows():

        try:
            return bool(
                ctypes.windll.shell32.IsUserAnAdmin()
            )
        except Exception:
            return False

    try:
        return os.geteuid() == 0
    except AttributeError:
        return False


def format_bytes(value: int) -> str:
    """Convert bytes to a readable size."""

    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB",
    ]

    size = float(value)

    for unit in units:

        if size < 1024 or unit == units[-1]:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{value} B"


# ============================================================
# System Information
# ============================================================

def collect_system_info() -> SystemInfo:
    """Collect basic local system information."""

    try:
        hostname = socket.gethostname()
    except OSError:
        hostname = "Unknown"

    try:
        username = getpass.getuser()
    except Exception:
        username = "Unknown"

    return SystemInfo(
        operating_system=platform.system(),
        release=platform.release(),
        version=platform.version(),
        architecture=platform.architecture()[0],
        hostname=hostname,
        username=username,
        python_version=platform.python_version(),
        cpu_count=os.cpu_count() or 1,
        machine=platform.machine(),
    )


def audit_system_information() -> None:
    """Audit basic system information."""

    info = collect_system_info()

    print("\n[+] System Information")
    print("-" * 60)

    print(
        f"Operating System : "
        f"{info.operating_system}"
    )

    print(
        f"Release          : "
        f"{info.release}"
    )

    print(
        f"Architecture     : "
        f"{info.architecture}"
    )

    print(
        f"Hostname         : "
        f"{info.hostname}"
    )

    print(
        f"Username         : "
        f"{info.username}"
    )

    print(
        f"Python Version   : "
        f"{info.python_version}"
    )

    print(
        f"CPU Count        : "
        f"{info.cpu_count}"
    )

    print(
        f"Machine          : "
        f"{info.machine}"
    )

    add_finding(
        category="System",
        title="System information collected",
        severity="INFO",
        description=(
            "Basic operating-system and runtime "
            "information was collected."
        ),
        recommendation=(
            "Keep the operating system and installed "
            "software regularly updated."
        ),
    )


# ============================================================
# Privilege Audit
# ============================================================

def audit_privileges() -> None:
    """Check whether the current process has elevated privileges."""

    elevated = is_admin()

    print("\n[+] Privilege Check")
    print("-" * 60)

    if elevated:

        print("Privilege Level : ⚠️ Elevated")

        add_finding(
            category="Privileges",
            title="Tool is running with elevated privileges",
            severity="WARNING",
            description=(
                "The current process has administrator/root "
                "privileges."
            ),
            recommendation=(
                "Run routine applications with standard user "
                "privileges whenever possible."
            ),
        )

    else:

        print("Privilege Level : ✅ Standard User")

        add_finding(
            category="Privileges",
            title="Standard user privileges detected",
            severity="PASS",
            description=(
                "The current process does not appear to have "
                "administrator/root privileges."
            ),
            recommendation=(
                "Continue using least-privilege accounts "
                "for normal activities."
            ),
        )


# ============================================================
# Firewall Audit
# ============================================================

def audit_windows_firewall() -> None:
    """Check Windows firewall profiles."""

    return_code, stdout, _ = safe_command(
        [
            "netsh",
            "advfirewall",
            "show",
            "allprofiles",
        ]
    )

    if return_code != 0:

        add_finding(
            category="Firewall",
            title="Unable to determine Windows Firewall status",
            severity="WARNING",
            description=(
                "The Windows firewall status could not "
                "be retrieved."
            ),
            recommendation=(
                "Verify Windows Defender Firewall status "
                "manually in Windows Security."
            ),
        )

        print(
            "Firewall Status : ⚠️ Unable to determine"
        )

        return

    states = re.findall(
        r"State\s+(ON|OFF)",
        stdout,
        flags=re.IGNORECASE,
    )

    states = [
        state.upper()
        for state in states
    ]

    if states and all(
        state == "ON"
        for state in states
    ):

        print(
            "Firewall Status : ✅ Enabled"
        )

        add_finding(
            category="Firewall",
            title="Windows Firewall appears enabled",
            severity="PASS",
            description=(
                "Detected Windows firewall profiles "
                "are enabled."
            ),
            recommendation=(
                "Keep the firewall enabled and review "
                "allowed applications periodically."
            ),
        )

    elif states and any(
        state == "OFF"
        for state in states
    ):

        print(
            "Firewall Status : ❌ One or more profiles disabled"
        )

        add_finding(
            category="Firewall",
            title="Windows Firewall profile disabled",
            severity="CRITICAL",
            description=(
                "At least one Windows Firewall profile "
                "appears to be disabled."
            ),
            recommendation=(
                "Enable the firewall for the affected "
                "network profile."
            ),
        )

    else:

        print(
            "Firewall Status : ⚠️ Unknown"
        )

        add_finding(
            category="Firewall",
            title="Firewall status could not be interpreted",
            severity="WARNING",
            description=(
                "Firewall information was returned but "
                "could not be interpreted reliably."
            ),
            recommendation=(
                "Check the firewall configuration manually."
            ),
        )


def audit_linux_firewall() -> None:
    """Check common Linux firewall managers."""

    commands = [
        ["ufw", "status"],
        ["firewall-cmd", "--state"],
    ]

    detected = False
    active = False

    for command in commands:

        return_code, stdout, _ = safe_command(command)

        if return_code != 0:
            continue

        detected = True

        text = stdout.lower()

        if (
            "active" in text
            or "running" in text
            or "status: active" in text
        ):

            active = True

            break

    print("\n[+] Firewall Check")
    print("-" * 60)

    if active:

        print("Firewall Status : ✅ Active")

        add_finding(
            category="Firewall",
            title="Linux firewall appears active",
            severity="PASS",
            description=(
                "A supported Linux firewall manager "
                "reported an active state."
            ),
            recommendation=(
                "Continue reviewing firewall rules and "
                "remove unnecessary exposed services."
            ),
        )

    elif detected:

        print("Firewall Status : ⚠️ Detected but inactive")

        add_finding(
            category="Firewall",
            title="Linux firewall manager is inactive",
            severity="WARNING",
            description=(
                "A firewall manager was detected, but it "
                "did not report an active state."
            ),
            recommendation=(
                "Review and enable an appropriate host firewall."
            ),
        )

    else:

        print("Firewall Status : ⚠️ Unable to determine")

        add_finding(
            category="Firewall",
            title="No supported active firewall detected",
            severity="WARNING",
            description=(
                "The tool could not identify an active "
                "supported firewall manager."
            ),
            recommendation=(
                "Verify the host firewall configuration manually."
            ),
        )


def audit_macos_firewall() -> None:
    """Check the macOS application firewall."""

    return_code, stdout, _ = safe_command(
        [
            "/usr/libexec/ApplicationFirewall/socketfilterfw",
            "--getglobalstate",
        ]
    )

    print("\n[+] Firewall Check")
    print("-" * 60)

    if return_code != 0:

        print("Firewall Status : ⚠️ Unable to determine")

        add_finding(
            category="Firewall",
            title="Unable to determine macOS firewall status",
            severity="WARNING",
            description=(
                "The application firewall state could "
                "not be retrieved."
            ),
            recommendation=(
                "Check Firewall settings in macOS System Settings."
            ),
        )

        return

    if "enabled" in stdout.lower():

        print("Firewall Status : ✅ Enabled")

        add_finding(
            category="Firewall",
            title="macOS application firewall enabled",
            severity="PASS",
            description=(
                "The macOS application firewall reports "
                "an enabled state."
            ),
            recommendation=(
                "Keep the firewall enabled and review "
                "application access periodically."
            ),
        )

    else:

        print("Firewall Status : ⚠️ Not confirmed")

        add_finding(
            category="Firewall",
            title="macOS firewall is not confirmed enabled",
            severity="WARNING",
            description=(
                "The firewall command did not report "
                "an enabled state."
            ),
            recommendation=(
                "Verify the application firewall configuration."
            ),
        )


def audit_firewall() -> None:
    """Run the appropriate firewall audit."""

    if is_windows():
        audit_windows_firewall()

    elif is_linux():
        audit_linux_firewall()

    elif is_macos():
        audit_macos_firewall()

    else:

        print("\n[+] Firewall Check")
        print("-" * 60)
        print(
            "Firewall Status : ⚠️ Unsupported operating system"
        )

        add_finding(
            category="Firewall",
            title="Firewall audit unavailable",
            severity="INFO",
            description=(
                "Automatic firewall auditing is not "
                "implemented for this operating system."
            ),
            recommendation=(
                "Review the operating system firewall manually."
            ),
        )


# ============================================================
# Listening Services Audit
# ============================================================

def parse_windows_connections(
    stdout: str,
) -> set[int]:
    """Extract listening TCP ports from netstat output."""

    ports: set[int] = set()

    for line in stdout.splitlines():

        if "LISTENING" not in line.upper():
            continue

        parts = line.split()

        if len(parts) < 2:
            continue

        local_address = parts[1]

        if ":" not in local_address:
            continue

        port = local_address.rsplit(":", 1)[-1]

        if port.isdigit():

            ports.add(int(port))

    return ports


def parse_unix_connections(
    stdout: str,
) -> set[int]:
    """Extract listening TCP ports from ss/netstat output."""

    ports: set[int] = set()

    for line in stdout.splitlines():

        lower = line.lower()

        if "listen" not in lower:
            continue

        match = re.search(
            r":(\d+)\s",
            line + " ",
        )

        if match:

            ports.add(
                int(match.group(1))
            )

    return ports


def audit_listening_services() -> None:
    """
    Detect TCP listening ports using native read-only
    networking utilities where available.
    """

    print("\n[+] Listening Network Services")
    print("-" * 60)

    ports: set[int] = set()

    if is_windows():

        return_code, stdout, _ = safe_command(
            ["netstat", "-ano"]
        )

        if return_code == 0:
            ports = parse_windows_connections(stdout)

    else:

        return_code, stdout, _ = safe_command(
            ["ss", "-ltn"]
        )

        if return_code == 0:

            ports = parse_unix_connections(
                stdout
            )

        else:

            return_code, stdout, _ = safe_command(
                ["netstat", "-lnt"]
            )

            if return_code == 0:

                ports = parse_unix_connections(
                    stdout
                )

    if not ports:

        print(
            "No listening TCP ports were detected "
            "or the information was unavailable."
        )

        add_finding(
            category="Network",
            title="Listening services could not be confirmed",
            severity="INFO",
            description=(
                "No listening TCP ports were detected, "
                "or the operating system did not provide "
                "the required command."
            ),
            recommendation=(
                "Review listening services manually if "
                "network exposure is important."
            ),
        )

        return

    sorted_ports = sorted(ports)

    print(
        "Listening TCP Ports:"
    )

    print(
        "  "
        + ", ".join(
            str(port)
            for port in sorted_ports
        )
    )

    common_risky_ports = {
        21: "FTP",
        23: "Telnet",
        25: "SMTP",
        110: "POP3",
        139: "NetBIOS",
        445: "SMB",
        3389: "RDP",
        5900: "VNC",
    }

    risky = [
        port
        for port in sorted_ports
        if port in common_risky_ports
    ]

    if risky:

        names = ", ".join(
            f"{port} ({common_risky_ports[port]})"
            for port in risky
        )

        print(
            f"Potentially sensitive services: {names}"
        )

        add_finding(
            category="Network",
            title="Potentially sensitive listening services detected",
            severity="WARNING",
            description=(
                f"The following common service ports are "
                f"listening: {names}."
            ),
            recommendation=(
                "Confirm that each exposed service is "
                "required and properly secured."
            ),
        )

    else:

        add_finding(
            category="Network",
            title="Listening TCP services detected",
            severity="PASS",
            description=(
                f"{len(sorted_ports)} listening TCP port(s) "
                "were detected."
            ),
            recommendation=(
                "Review exposed services periodically and "
                "disable services that are not required."
            ),
        )


# ============================================================
# Sensitive File Permission Audit
# ============================================================

def audit_unix_sensitive_file(
    file_path: Path,
) -> None:
    """Check permissions on sensitive Unix files."""

    if not file_path.exists():
        return

    try:

        mode = file_path.stat().st_mode

    except OSError:

        return

    permissions = stat.S_IMODE(mode)

    group_writable = bool(
        permissions & stat.S_IWGRP
    )

    world_writable = bool(
        permissions & stat.S_IWOTH
    )

    world_readable = bool(
        permissions & stat.S_IROTH
    )

    if world_writable:

        add_finding(
            category="File Permissions",
            title=f"World-writable sensitive file: {file_path}",
            severity="CRITICAL",
            description=(
                f"{file_path} is writable by all local users."
            ),
            recommendation=(
                "Restrict write permissions to trusted "
                "administrators or the owning service."
            ),
        )

    elif group_writable:

        add_finding(
            category="File Permissions",
            title=f"Group-writable sensitive file: {file_path}",
            severity="WARNING",
            description=(
                f"{file_path} is writable by its group."
            ),
            recommendation=(
                "Review group membership and restrict "
                "permissions where appropriate."
            ),
        )

    elif world_readable and file_path.name == "shadow":

        add_finding(
            category="File Permissions",
            title="Sensitive password database is world-readable",
            severity="CRITICAL",
            description=(
                f"{file_path} is readable by other local users."
            ),
            recommendation=(
                "Restrict access to the password database."
            ),
        )

    else:

        add_finding(
            category="File Permissions",
            title=f"Sensitive file permissions reviewed: {file_path}",
            severity="PASS",
            description=(
                "No obviously excessive write permissions "
                "were detected."
            ),
            recommendation=(
                "Continue following least-privilege file permissions."
            ),
        )


def audit_sensitive_file_permissions() -> None:
    """Audit sensitive Unix configuration files."""

    print("\n[+] Sensitive File Permissions")
    print("-" * 60)

    if is_windows():

        print(
            "Permission audit: Windows-specific ACL analysis "
            "is not enabled in this version."
        )

        add_finding(
            category="File Permissions",
            title="Windows ACL audit not implemented",
            severity="INFO",
            description=(
                "Detailed Windows ACL analysis is outside "
                "the current implementation."
            ),
            recommendation=(
                "Use Windows Security or PowerShell tools "
                "for detailed ACL auditing."
            ),
        )

        return

    checked = 0

    for file_name in SENSITIVE_LINUX_FILES:

        path = Path(file_name)

        if not path.exists():
            continue

        checked += 1

        print(
            f"Checking: {path}"
        )

        audit_unix_sensitive_file(
            path
        )

    if checked == 0:

        print(
            "No standard sensitive Unix configuration "
            "files were available for checking."
        )


# ============================================================
# SSH Configuration Audit
# ============================================================

def audit_ssh_configuration() -> None:
    """Check basic SSH server configuration where applicable."""

    print("\n[+] SSH Configuration")
    print("-" * 60)

    if not (is_linux() or is_macos()):

        print(
            "SSH configuration audit: Not applicable."
        )

        return

    config_path = Path(
        "/etc/ssh/sshd_config"
    )

    if not config_path.exists():

        print(
            "SSH server configuration not found."
        )

        add_finding(
            category="SSH",
            title="SSH server configuration not detected",
            severity="INFO",
            description=(
                "The standard SSH server configuration "
                "file was not found."
            ),
            recommendation=(
                "If SSH is not required, keep it disabled. "
                "If it is required, use secure configuration."
            ),
        )

        return

    try:

        content = config_path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    except OSError as error:

        print(
            f"Unable to read SSH configuration: {error}"
        )

        add_finding(
            category="SSH",
            title="Unable to inspect SSH configuration",
            severity="WARNING",
            description=(
                "The SSH server configuration exists but "
                "could not be read."
            ),
            recommendation=(
                "Review the SSH server configuration manually."
            ),
        )

        return

    normalized_lines = []

    for line in content.splitlines():

        stripped = line.strip()

        if not stripped:
            continue

        if stripped.startswith("#"):
            continue

        normalized_lines.append(
            stripped
        )

    settings = {}

    for line in normalized_lines:

        parts = line.split(
            None,
            1,
        )

        if len(parts) == 2:

            key = parts[0].lower()
            value = parts[1].strip()

            settings[key] = value

    permit_root = settings.get(
        "permitrootlogin"
    )

    password_auth = settings.get(
        "passwordauthentication"
    )

    if permit_root:

        print(
            f"PermitRootLogin: {permit_root}"
        )

        if permit_root.lower() in {
            "yes",
            "without-password",
            "prohibit-password",
        }:

            severity = (
                "WARNING"
                if permit_root.lower() == "yes"
                else "PASS"
            )

            add_finding(
                category="SSH",
                title="SSH root login configuration reviewed",
                severity=severity,
                description=(
                    f"PermitRootLogin is set to "
                    f"{permit_root}."
                ),
                recommendation=(
                    "Prefer disabling direct root login "
                    "and use individual accounts with "
                    "appropriate privilege escalation."
                ),
            )

    if password_auth:

        print(
            f"PasswordAuthentication: {password_auth}"
        )

        if password_auth.lower() == "yes":

            add_finding(
                category="SSH",
                title="SSH password authentication enabled",
                severity="WARNING",
                description=(
                    "SSH password authentication appears "
                    "to be enabled."
                ),
                recommendation=(
                    "Where practical, use strong SSH keys "
                    "and disable password authentication "
                    "after validating key-based access."
                ),
            )

        elif password_auth.lower() == "no":

            add_finding(
                category="SSH",
                title="SSH password authentication disabled",
                severity="PASS",
                description=(
                    "SSH password authentication appears "
                    "to be disabled."
                ),
                recommendation=(
                    "Continue protecting SSH private keys "
                    "and review access regularly."
                ),
            )

    if not permit_root and not password_auth:

        add_finding(
            category="SSH",
            title="SSH configuration requires manual review",
            severity="INFO",
            description=(
                "No directly relevant SSH authentication "
                "settings were found in the active configuration."
            ),
            recommendation=(
                "Review effective SSH configuration manually."
            ),
        )


# ============================================================
# Environment Security Audit
# ============================================================

def audit_environment() -> None:
    """Look for potentially risky environment configuration."""

    print("\n[+] Environment Security")
    print("-" * 60)

    path_value = os.environ.get(
        "PATH",
        "",
    )

    path_entries = path_value.split(
        os.pathsep
    )

    empty_entries = [
        entry
        for entry in path_entries
        if not entry
    ]

    if empty_entries:

        print(
            "PATH: ⚠️ Contains empty entries"
        )

        add_finding(
            category="Environment",
            title="PATH contains empty entries",
            severity="WARNING",
            description=(
                "An empty PATH entry can cause command "
                "resolution behavior that should be reviewed."
            ),
            recommendation=(
                "Remove unnecessary empty PATH entries."
            ),
        )

    else:

        print(
            "PATH: ✅ No empty entries detected"
        )

        add_finding(
            category="Environment",
            title="PATH contains no empty entries",
            severity="PASS",
            description=(
                "No empty entries were detected in PATH."
            ),
            recommendation=(
                "Keep PATH entries limited to trusted locations."
            ),
        )

    suspicious_names = []

    for key in os.environ:

        upper_key = key.upper()

        if any(
            keyword in upper_key
            for keyword in (
                "PASSWORD",
                "SECRET",
                "PRIVATE_KEY",
                "ACCESS_TOKEN",
                "API_KEY",
            )
        ):

            suspicious_names.append(
                key
            )

    if suspicious_names:

        print(
            "Sensitive-looking environment variables detected:"
        )

        for name in suspicious_names:

            print(
                f"  - {name}"
            )

        add_finding(
            category="Environment",
            title="Sensitive-looking environment variables detected",
            severity="WARNING",
            description=(
                "Environment variable names suggest that "
                "secrets may be supplied through the environment."
            ),
            recommendation=(
                "Avoid exposing secrets unnecessarily and "
                "ensure they are not written to logs or committed "
                "to source control."
            ),
        )

    else:

        print(
            "Sensitive-looking variables: None detected"
        )

        add_finding(
            category="Environment",
            title="No obvious secret-like environment variables detected",
            severity="PASS",
            description=(
                "No environment variable names matching "
                "common secret patterns were detected."
            ),
            recommendation=(
                "Continue avoiding hard-coded credentials."
            ),
        )


# ============================================================
# Sensitive File Discovery
# ============================================================

def audit_current_directory() -> None:
    """
    Check the current directory for common sensitive filenames.

    This does not open or read their contents.
    """

    print("\n[+] Sensitive Filename Check")
    print("-" * 60)

    current_directory = Path.cwd()

    detected: list[Path] = []

    try:

        for path in current_directory.rglob("*"):

            if not path.is_file():
                continue

            if path.name.lower() in {
                name.lower()
                for name in COMMON_SENSITIVE_FILENAMES
            }:

                detected.append(
                    path
                )

    except (
        PermissionError,
        OSError,
    ):
        pass

    if detected:

        print(
            "Potentially sensitive files found:"
        )

        for path in detected[:50]:

            print(
                f"  - {path}"
            )

        if len(detected) > 50:

            print(
                f"  ... and {len(detected) - 50} more"
            )

        add_finding(
            category="Sensitive Files",
            title="Potentially sensitive files detected",
            severity="WARNING",
            description=(
                f"{len(detected)} filename(s) matched "
                "common sensitive-file patterns."
            ),
            recommendation=(
                "Review whether these files should exist "
                "in the scanned directory and ensure secrets "
                "are not committed to version control."
            ),
        )

    else:

        print(
            "No common sensitive filenames detected."
        )

        add_finding(
            category="Sensitive Files",
            title="No common sensitive filenames detected",
            severity="PASS",
            description=(
                "No files matching the configured sensitive "
                "filename patterns were detected."
            ),
            recommendation=(
                "Continue keeping credentials and private keys "
                "outside source repositories."
            ),
        )


# ============================================================
# Disk / Storage Security
# ============================================================

def audit_disk_space() -> None:
    """Check available disk space."""

    print("\n[+] Disk Space")
    print("-" * 60)

    try:

        usage = shutil.disk_usage(
            Path.cwd()
        )

        total = usage.total
        used = usage.used
        free = usage.free

        percentage_used = (
            used / total * 100
            if total
            else 0
        )

        print(
            f"Total : {format_bytes(total)}"
        )

        print(
            f"Used  : {format_bytes(used)} "
            f"({percentage_used:.1f}%)"
        )

        print(
            f"Free  : {format_bytes(free)}"
        )

        if percentage_used >= 95:

            add_finding(
                category="Storage",
                title="Disk space critically low",
                severity="CRITICAL",
                description=(
                    f"Approximately {percentage_used:.1f}% "
                    "of the current filesystem is used."
                ),
                recommendation=(
                    "Free disk space and investigate unexpectedly "
                    "large files or logs."
                ),
            )

        elif percentage_used >= 85:

            add_finding(
                category="Storage",
                title="Disk space is getting low",
                severity="WARNING",
                description=(
                    f"Approximately {percentage_used:.1f}% "
                    "of the current filesystem is used."
                ),
                recommendation=(
                    "Monitor disk usage and clean unnecessary "
                    "files safely."
                ),
            )

        else:

            add_finding(
                category="Storage",
                title="Disk space appears adequate",
                severity="PASS",
                description=(
                    f"Approximately {percentage_used:.1f}% "
                    "of the current filesystem is used."
                ),
                recommendation=(
                    "Continue monitoring storage capacity."
                ),
            )

    except OSError as error:

        print(
            f"Unable to determine disk usage: {error}"
        )

        add_finding(
            category="Storage",
            title="Unable to determine disk usage",
            severity="INFO",
            description=(
                "Disk usage could not be retrieved."
            ),
            recommendation=(
                "Review storage capacity manually."
            ),
        )


# ============================================================
# Security Headers / Python Runtime
# ============================================================

def audit_python_runtime() -> None:
    """Audit the Python runtime environment."""

    print("\n[+] Python Runtime")
    print("-" * 60)

    version_info = sys.version_info

    print(
        f"Python: {platform.python_version()}"
    )

    print(
        f"Executable: {sys.executable}"
    )

    if version_info < (3, 9):

        add_finding(
            category="Runtime",
            title="Python runtime is old",
            severity="WARNING",
            description=(
                "The running Python version is older than "
                "the minimum version targeted by this project."
            ),
            recommendation=(
                "Upgrade to a currently supported Python release."
            ),
        )

    else:

        add_finding(
            category="Runtime",
            title="Python runtime meets project requirements",
            severity="PASS",
            description=(
                f"Python {platform.python_version()} "
                "is running."
            ),
            recommendation=(
                "Keep Python updated within a supported release line."
            ),
        )


# ============================================================
# Local Hostname / Network Identity
# ============================================================

def audit_hostname_resolution() -> None:
    """Check basic local hostname resolution."""

    print("\n[+] Hostname Resolution")
    print("-" * 60)

    try:

        hostname = socket.gethostname()

        addresses = socket.getaddrinfo(
            hostname,
            None,
        )

        unique_addresses = sorted(
            {
                item[4][0]
                for item in addresses
                if item[4]
            }
        )

        print(
            f"Hostname: {hostname}"
        )

        if unique_addresses:

            print(
                "Resolved Addresses:"
            )

            for address in unique_addresses:

                print(
                    f"  - {address}"
                )

            add_finding(
                category="Network",
                title="Hostname resolution succeeded",
                severity="PASS",
                description=(
                    "The local hostname resolved to one or "
                    "more addresses."
                ),
                recommendation=(
                    "Review network configuration if unexpected "
                    "addresses appear."
                ),
            )

        else:

            add_finding(
                category="Network",
                title="Hostname returned no addresses",
                severity="INFO",
                description=(
                    "The hostname did not resolve to an address."
                ),
                recommendation=(
                    "Review local DNS and network configuration "
                    "if this is unexpected."
                ),
            )

    except OSError as error:

        print(
            f"Resolution failed: {error}"
        )

        add_finding(
            category="Network",
            title="Hostname resolution failed",
            severity="WARNING",
            description=(
                "The local hostname could not be resolved."
            ),
            recommendation=(
                "Review local DNS and network configuration."
            ),
        )


# ============================================================
# Security Score
# ============================================================

def calculate_score() -> tuple[int, str]:
    """
    Calculate a simple security score.

    PASS     = +0
    INFO     = +0
    WARNING  = -10
    CRITICAL = -25

    The score is intentionally a simple educational indicator,
    not a formal security rating.
    """

    score = 100

    for finding in FINDINGS:

        if finding.severity == "WARNING":
            score -= 10

        elif finding.severity == "CRITICAL":
            score -= 25

    score = max(
        0,
        min(
            100,
            score,
        ),
    )

    if score >= 90:
        rating = "Excellent"

    elif score >= 75:
        rating = "Good"

    elif score >= 50:
        rating = "Needs Attention"

    else:
        rating = "High Risk"

    return score, rating


# ============================================================
# Findings Summary
# ============================================================

def get_counts() -> dict[str, int]:
    """Return finding counts by severity."""

    counts = {
        "PASS": 0,
        "INFO": 0,
        "WARNING": 0,
        "CRITICAL": 0,
    }

    for finding in FINDINGS:

        if finding.severity in counts:

            counts[finding.severity] += 1

    return counts


def print_findings() -> None:
    """Print all security findings."""

    print("\n" + "=" * 70)
    print("SECURITY FINDINGS")
    print("=" * 70)

    if not FINDINGS:

        print(
            "No findings were generated."
        )

        return

    for index, finding in enumerate(
        FINDINGS,
        start=1,
    ):

        print(
            f"\n[{index}] "
            f"{finding.severity}: "
            f"{finding.title}"
        )

        print(
            f"Category: {finding.category}"
        )

        print(
            f"Description: "
            f"{finding.description}"
        )

        print(
            f"Recommendation: "
            f"{finding.recommendation}"
        )


def print_summary() -> None:
    """Print the final audit summary."""

    counts = get_counts()

    score, rating = calculate_score()

    print("\n" + "=" * 70)
    print("SECURITY AUDIT SUMMARY")
    print("=" * 70)

    print(
        f"Security Score : {score}/100"
    )

    print(
        f"Security Rating: {rating}"
    )

    print(
        f"PASS           : {counts['PASS']}"
    )

    print(
        f"INFO           : {counts['INFO']}"
    )

    print(
        f"WARNING        : {counts['WARNING']}"
    )

    print(
        f"CRITICAL       : {counts['CRITICAL']}"
    )

    print("=" * 70)


# ============================================================
# JSON Report
# ============================================================

def export_report(
    output_path: Path,
    system_info: SystemInfo,
    duration: float,
) -> None:
    """Export audit results to JSON."""

    score, rating = calculate_score()

    counts = get_counts()

    report = {
        "application": APP_NAME,
        "version": VERSION,
        "generated_at": datetime.now(
            timezone.utc
        ).isoformat(),
        "duration_seconds": round(
            duration,
            3,
        ),
        "system": asdict(
            system_info
        ),
        "summary": {
            "score": score,
            "rating": rating,
            "counts": counts,
        },
        "findings": [
            asdict(finding)
            for finding in FINDINGS
        ],
    }

    try:

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            json.dumps(
                report,
                indent=4,
            ),
            encoding="utf-8",
        )

    except OSError as error:

        print(
            f"\nError writing report: {error}",
            file=sys.stderr,
        )

        return

    print(
        f"\n📄 Report saved to: {output_path}"
    )


# ============================================================
# Audit Runner
# ============================================================

def run_audit(
    report_path: Optional[Path] = None,
) -> int:
    """Run the complete security audit."""

    FINDINGS.clear()

    start_time = time.perf_counter()

    print("=" * 70)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print("=" * 70)

    print(
        "\nMode: READ-ONLY SECURITY AUDIT"
    )

    print(
        "No system configuration will be modified."
    )

    system_info = collect_system_info()

    audit_system_information()

    audit_privileges()

    audit_firewall()

    audit_listening_services()

    audit_sensitive_file_permissions()

    audit_ssh_configuration()

    audit_environment()

    audit_current_directory()

    audit_disk_space()

    audit_python_runtime()

    audit_hostname_resolution()

    duration = (
        time.perf_counter()
        - start_time
    )

    print_findings()

    print_summary()

    if report_path:

        export_report(
            report_path,
            system_info,
            duration,
        )

    counts = get_counts()

    if counts["CRITICAL"] > 0:
        return 2

    if counts["WARNING"] > 0:
        return 1

    return 0


# ============================================================
# Quick Check
# ============================================================

def quick_check() -> int:
    """
    Run a lightweight security check.

    This is useful when the user wants a quick overview.
    """

    FINDINGS.clear()

    print("=" * 70)
    print(APP_NAME)
    print("Quick Security Check")
    print("=" * 70)

    audit_privileges()

    audit_firewall()

    audit_listening_services()

    score, rating = calculate_score()

    print("\n" + "=" * 70)
    print("QUICK CHECK RESULT")
    print("=" * 70)

    print(
        f"Security Score : {score}/100"
    )

    print(
        f"Rating         : {rating}"
    )

    print(
        f"Findings       : {len(FINDINGS)}"
    )

    print("=" * 70)

    counts = get_counts()

    if counts["CRITICAL"] > 0:
        return 2

    if counts["WARNING"] > 0:
        return 1

    return 0


# ============================================================
# Version
# ============================================================

def print_version() -> None:
    """Print application version."""

    print(
        f"{APP_NAME} v{VERSION}"
    )


# ============================================================
# CLI
# ============================================================

def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        description=(
            "Read-only local security auditing "
            "and configuration assessment tool."
        ),
        epilog=(
            "Examples:\n"
            "  python security_audit.py audit\n"
            "  python security_audit.py audit "
            "--report security_report.json\n"
            "  python security_audit.py quick\n"
            "  python security_audit.py version"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # --------------------------------------------------------
    # Audit
    # --------------------------------------------------------

    audit_parser = subparsers.add_parser(
        "audit",
        help="Run the complete read-only security audit.",
    )

    audit_parser.add_argument(
        "-r",
        "--report",
        type=Path,
        help=(
            "Export the audit results "
            "to a JSON file."
        ),
    )

    # --------------------------------------------------------
    # Quick
    # --------------------------------------------------------

    quick_parser = subparsers.add_parser(
        "quick",
        help="Run a lightweight security check.",
    )

    # --------------------------------------------------------
    # Version
    # --------------------------------------------------------

    subparsers.add_parser(
        "version",
        help="Show program version.",
    )

    return parser


# ============================================================
# Main
# ============================================================

def main() -> int:
    """Application entry point."""

    parser = create_parser()

    args = parser.parse_args()

    try:

        if args.command == "audit":

            return run_audit(
                report_path=args.report
            )

        if args.command == "quick":

            return quick_check()

        if args.command == "version":

            print_version()

            return 0

        parser.print_help()

        return 1

    except KeyboardInterrupt:

        print(
            "\n\nOperation cancelled by user."
        )

        return 130

    except Exception as error:

        print(
            f"\nUnexpected error: {error}",
            file=sys.stderr,
        )

        return 1


if __name__ == "__main__":
    sys.exit(main())
