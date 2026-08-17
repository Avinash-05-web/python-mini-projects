import socket
import ipaddress


def validate_domain(domain):
    """Basic validation for a domain name."""

    domain = domain.strip().lower()

    # Remove protocol if the user enters a URL
    if domain.startswith("https://"):
        domain = domain[8:]

    elif domain.startswith("http://"):
        domain = domain[7:]

    # Remove paths
    domain = domain.split("/")[0]

    # Remove port number if provided
    domain = domain.split(":")[0]

    if not domain:
        return None

    # Domain should not contain spaces
    if " " in domain:
        return None

    # Prevent direct IP addresses
    try:
        ipaddress.ip_address(domain)
        return None
    except ValueError:
        pass

    # Basic domain validation
    if "." not in domain:
        return None

    if len(domain) > 253:
        return None

    return domain


def get_ipv4(domain):
    """Find IPv4 addresses for a domain."""

    try:
        addresses = socket.getaddrinfo(
            domain,
            None,
            socket.AF_INET
        )

        return sorted(
            set(address[4][0] for address in addresses)
        )

    except socket.gaierror:
        return []


def get_ipv6(domain):
    """Find IPv6 addresses for a domain."""

    try:
        addresses = socket.getaddrinfo(
            domain,
            None,
            socket.AF_INET6
        )

        return sorted(
            set(address[4][0] for address in addresses)
        )

    except socket.gaierror:
        return []


def get_hostname(domain):
    """Get the canonical hostname."""

    try:
        hostname = socket.getfqdn(domain)

        if hostname:
            return hostname

        return "Not available"

    except socket.error:
        return "Not available"


def display_results(domain):
    """Perform the DNS lookup and display results."""

    print("\n" + "=" * 60)
    print("              DNS LOOKUP RESULTS")
    print("=" * 60)

    print(f"\nDomain: {domain}")

    # IPv4
    print("\nIPv4 Addresses:")
    ipv4_addresses = get_ipv4(domain)

    if ipv4_addresses:
        for address in ipv4_addresses:
            print(f"  • {address}")
    else:
        print("  No IPv4 address found.")

    # IPv6
    print("\nIPv6 Addresses:")
    ipv6_addresses = get_ipv6(domain)

    if ipv6_addresses:
        for address in ipv6_addresses:
            print(f"  • {address}")
    else:
        print("  No IPv6 address found.")

    # Canonical hostname
    print("\nCanonical Hostname:")
    print(f"  • {get_hostname(domain)}")

    print("\n" + "=" * 60)


def main():
    print("=" * 60)
    print("                 🔎 DNS LOOKUP TOOL")
    print("=" * 60)

    domain_input = input("\nEnter a domain name: ")

    domain = validate_domain(domain_input)

    if not domain:
        print("\n❌ Invalid domain name.")
        print("Example: example.com")
        return

    print(f"\nLooking up DNS information for: {domain}")
    print("Please wait...")

    try:
        display_results(domain)

    except KeyboardInterrupt:
        print("\n\nLookup cancelled.")

    except Exception:
        print("\n❌ An unexpected error occurred.")


if __name__ == "__main__":
    main()
