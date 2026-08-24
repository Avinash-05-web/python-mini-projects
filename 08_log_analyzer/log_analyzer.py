import argparse
import logging
import re
from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()


logging.basicConfig(
    filename="log_analyzer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


LOG_PATTERN = re.compile(
    r'(?P<ip>\S+)'
    r'\s+\S+\s+\S+'
    r'\s+\[(?P<timestamp>[^\]]+)\]'
    r'\s+"(?P<method>[A-Z]+)\s+(?P<path>\S+)'
    r'(?:\s+[^"]*)?"'
    r'\s+(?P<status>\d{3})'
    r'\s+(?P<size>\S+)'
)


class LogAnalyzer:

    def __init__(self, log_file):

        self.log_file = Path(log_file)

        self.total_entries = 0
        self.ip_addresses = Counter()
        self.status_codes = Counter()
        self.methods = Counter()
        self.paths = Counter()

        self.failed_requests = 0
        self.errors = 0
        self.warnings = 0

        self.suspicious_ips = Counter()

    def validate_file(self):

        if not self.log_file.exists():
            raise FileNotFoundError(
                f"Log file not found: {self.log_file}"
            )

        if not self.log_file.is_file():
            raise ValueError(
                f"Path is not a file: {self.log_file}"
            )

        logger.info(
            "Analyzing log file: %s",
            self.log_file
        )

    def analyze(self):

        self.validate_file()

        try:

            with self.log_file.open(
                "r",
                encoding="utf-8",
                errors="replace"
            ) as file:

                for line in file:

                    line = line.strip()

                    if not line:
                        continue

                    self.total_entries += 1

                    match = LOG_PATTERN.search(line)

                    if match:
                        self._process_access_log(match)
                    else:
                        self._process_message_log(line)

        except PermissionError:

            raise PermissionError(
                f"Permission denied while reading: {self.log_file}"
            )

        except OSError as error:

            raise OSError(
                f"Unable to read log file: {error}"
            )

        logger.info(
            "Analysis completed. Processed %d entries.",
            self.total_entries
        )

    def _process_access_log(self, match):

        ip = match.group("ip")
        method = match.group("method")
        path = match.group("path")
        status = int(match.group("status"))

        self.ip_addresses[ip] += 1
        self.status_codes[status] += 1
        self.methods[method] += 1
        self.paths[path] += 1

        if status >= 400:
            self.failed_requests += 1

        if status >= 500:
            self.errors += 1

        elif status == 404:
            self.warnings += 1

        suspicious_paths = (
            "/admin",
            "/wp-admin",
            "/wp-login",
            "/phpmyadmin",
            "/.env",
            "/etc/passwd",
            "/config",
            "/login"
        )

        path_lower = path.lower()

        if any(
            suspicious_path in path_lower
            for suspicious_path in suspicious_paths
        ):
            self.suspicious_ips[ip] += 1

    def _process_message_log(self, line):

        line_lower = line.lower()

        if "error" in line_lower:
            self.errors += 1

        if "warning" in line_lower or "warn" in line_lower:
            self.warnings += 1

    def display_report(self):

        console.print()

        console.print(
            Panel.fit(
                "[bold cyan]📊 LOG ANALYZER[/bold cyan]\n"
                "[white]Security & Log Analysis Tool[/white]",
                border_style="cyan"
            )
        )

        console.print(
            f"\n[bold]File:[/bold] {self.log_file}"
        )

        stats_table = Table(
            title="📈 General Statistics"
        )

        stats_table.add_column("Metric")
        stats_table.add_column(
            "Value",
            justify="right"
        )

        stats_table.add_row(
            "Total Log Entries",
            str(self.total_entries)
        )

        stats_table.add_row(
            "Unique IP Addresses",
            str(len(self.ip_addresses))
        )

        stats_table.add_row(
            "Failed Requests",
            str(self.failed_requests)
        )

        stats_table.add_row(
            "Errors",
            str(self.errors)
        )

        stats_table.add_row(
            "Warnings",
            str(self.warnings)
        )

        console.print(stats_table)

        if self.ip_addresses:

            ip_table = Table(
                title="🌐 Top IP Addresses"
            )

            ip_table.add_column(
                "Rank",
                justify="center"
            )

            ip_table.add_column("IP Address")

            ip_table.add_column(
                "Requests",
                justify="right"
            )

            for rank, (ip, count) in enumerate(
                self.ip_addresses.most_common(10),
                start=1
            ):

                ip_table.add_row(
                    str(rank),
                    ip,
                    str(count)
                )

            console.print(ip_table)

        if self.status_codes:

            status_table = Table(
                title="📊 HTTP Status Codes"
            )

            status_table.add_column("Status")
            status_table.add_column(
                "Requests",
                justify="right"
            )

            for status, count in sorted(
                self.status_codes.items()
            ):

                status_table.add_row(
                    str(status),
                    str(count)
                )

            console.print(status_table)

        if self.methods:

            method_table = Table(
                title="🔧 HTTP Methods"
            )

            method_table.add_column("Method")
            method_table.add_column(
                "Requests",
                justify="right"
            )

            for method, count in self.methods.most_common():

                method_table.add_row(
                    method,
                    str(count)
                )

            console.print(method_table)

        if self.paths:

            path_table = Table(
                title="🔗 Most Requested Paths"
            )

            path_table.add_column("Path")
            path_table.add_column(
                "Requests",
                justify="right"
            )

            for path, count in self.paths.most_common(10):

                path_table.add_row(
                    path,
                    str(count)
                )

            console.print(path_table)

        security_table = Table(
            title="🛡️ Security Indicators"
        )

        security_table.add_column("Indicator")
        security_table.add_column(
            "Count",
            justify="right"
        )

        security_table.add_row(
            "Failed Requests",
            str(self.failed_requests)
        )

        security_table.add_row(
            "Server Errors",
            str(self.errors)
        )

        security_table.add_row(
            "Warnings / 404 Responses",
            str(self.warnings)
        )

        security_table.add_row(
            "Suspicious Requests",
            str(sum(self.suspicious_ips.values()))
        )

        console.print(security_table)

        if self.suspicious_ips:

            suspicious_table = Table(
                title="⚠️ Suspicious IP Addresses"
            )

            suspicious_table.add_column(
                "IP Address"
            )

            suspicious_table.add_column(
                "Suspicious Requests",
                justify="right"
            )

            for ip, count in self.suspicious_ips.most_common(10):

                suspicious_table.add_row(
                    ip,
                    str(count)
                )

            console.print(suspicious_table)

        else:

            console.print(
                Panel(
                    "[green]No basic suspicious activity "
                    "indicators detected.[/green]",
                    title="🛡️ Security Check"
                )
            )

        console.print(
            "\n[bold green]✓ Analysis Complete[/bold green]\n"
        )


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Analyze web and application log files "
            "and display useful statistics."
        )
    )

    parser.add_argument(
        "log_file",
        help="Path to the log file to analyze"
    )

    args = parser.parse_args()

    analyzer = LogAnalyzer(args.log_file)

    try:

        analyzer.analyze()
        analyzer.display_report()

    except (
        FileNotFoundError,
        PermissionError,
        ValueError,
        OSError
    ) as error:

        logger.error(str(error))

        console.print(
            f"[bold red]✗ Error:[/bold red] {error}"
        )

    except KeyboardInterrupt:

        logger.warning(
            "Analysis interrupted by user."
        )

        console.print(
            "\n[yellow]Analysis cancelled by user.[/yellow]"
        )


if __name__ == "__main__":
    main()
