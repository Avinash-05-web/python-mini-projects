import time
import ssl
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def validate_url(url):
    """Validate and prepare the URL."""

    url = url.strip()

    if not url:
        return None

    # Add HTTPS if the user doesn't provide a scheme
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)

    # Only allow HTTP and HTTPS
    if parsed.scheme not in ("http", "https"):
        return None

    # A valid URL must have a hostname
    if not parsed.hostname:
        return None

    return url


def check_website(url):
    """Check whether a website is reachable."""

    try:
        request = Request(
            url,
            headers={
                "User-Agent": "Python-Website-Status-Checker/1.0"
            },
            method="GET"
        )

        start_time = time.perf_counter()

        # Create a default secure SSL context
        ssl_context = ssl.create_default_context()

        with urlopen(
            request,
            timeout=10,
            context=ssl_context
        ) as response:

            end_time = time.perf_counter()

            status_code = response.status
            final_url = response.geturl()
            response_time = (end_time - start_time) * 1000

            return {
                "status": "ONLINE",
                "code": status_code,
                "time": response_time,
                "url": final_url
            }

    except HTTPError as error:
        end_time = time.perf_counter()

        return {
            "status": "REACHABLE",
            "code": error.code,
            "time": (end_time - start_time) * 1000,
            "url": url
        }

    except URLError as error:

        if isinstance(error.reason, TimeoutError):
            return {
                "status": "TIMEOUT",
                "code": None,
                "time": None,
                "url": url
            }

        return {
            "status": "UNREACHABLE",
            "code": None,
            "time": None,
            "url": url
        }

    except TimeoutError:

        return {
            "status": "TIMEOUT",
            "code": None,
            "time": None,
            "url": url
        }

    except ssl.SSLError:

        return {
            "status": "SSL ERROR",
            "code": None,
            "time": None,
            "url": url
        }

    except Exception as error:

        return {
            "status": "ERROR",
            "code": None,
            "time": None,
            "url": url
        }


def main():

    print("=" * 55)
    print("          🌐 WEBSITE STATUS CHECKER")
    print("=" * 55)

    website = input("\nEnter website URL: ")

    url = validate_url(website)

    if not url:
        print("\n❌ Invalid URL.")
        return

    print("\nChecking website...")
    print("-" * 55)

    result = check_website(url)

    print(f"Website : {result['url']}")
    print(f"Status  : {result['status']}")

    if result["code"] is not None:
        print(f"HTTP Code: {result['code']}")

    if result["time"] is not None:
        print(f"Response: {result['time']:.2f} ms")

    print("-" * 55)

    if result["status"] == "ONLINE":
        print("✅ Website is reachable.")

    elif result["status"] == "REACHABLE":
        print("⚠️ Website is reachable but returned an HTTP error.")

    elif result["status"] == "TIMEOUT":
        print("⏱️ Website request timed out.")

    elif result["status"] == "UNREACHABLE":
        print("❌ Website could not be reached.")

    elif result["status"] == "SSL ERROR":
        print("🔒 SSL/TLS connection error.")

    else:
        print("❌ An unexpected error occurred.")

    print("=" * 55)


if __name__ == "__main__":
    main()
