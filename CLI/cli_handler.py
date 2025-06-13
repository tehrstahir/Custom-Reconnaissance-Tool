import argparse
from urllib.parse import urlparse

def handle_cli():
    parser = argparse.ArgumentParser(
        description="Custom Reconnaissance Tool - Perform subdomain enumeration, WHOIS, DNS lookup, port scanning, banner grabbing, and tech detection."
    )

    # Full URL input instead of separate domain and scheme
    parser.add_argument("url", help="Target URL (e.g., http://example.com)")

    # Optional features
    parser.add_argument("--whois", action="store_true", help="Perform WHOIS lookup")
    parser.add_argument("--dns", action="store_true", help="Perform DNS enumeration")
    parser.add_argument("--subdomains", action="store_true", help="Perform subdomain enumeration")
    parser.add_argument("--ports", action="store_true", help="Perform full port scanning (1-65535)")
    parser.add_argument("--banner", action="store_true", help="Perform banner grabbing on open ports")
    parser.add_argument("--tech", action="store_true", help="Detect technologies using Wappalyzer")

    args = parser.parse_args()

    # Parse the input URL to extract scheme and domain
    parsed_url = urlparse(args.url)
    if not parsed_url.scheme or not parsed_url.netloc:
        parser.error("Invalid URL format. Example usage: http://example.com")

    # Attach parsed parts for easier access
    args.domain = parsed_url.netloc
    args.scheme = parsed_url.scheme

    return args
