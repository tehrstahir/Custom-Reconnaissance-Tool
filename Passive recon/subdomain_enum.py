import requests
import logging
import json
import re

def setup_logger(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=level
    )

def validate_domain(domain):
    pattern = r'^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$'
    if re.match(pattern, domain):
        return True
    else:
        logging.error("Invalid domain format. Please enter a valid domain (e.g., example.com).")
        return False

def query_crtsh(domain):
    url = f'https://crt.sh/?q=%25.{domain}&output=json'
    logging.info(f"[*] Querying crt.sh for {domain}")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            logging.error("Failed to fetch data from crt.sh")
            return []
        data = json.loads(response.text)
        subdomains = set()
        for entry in data:
            subdomain = entry['name_value']
            if '\n' in subdomain:
                subdomains.update(subdomain.split('\n'))
            else:
                subdomains.add(subdomain)
        return list(subdomains)
    except Exception as e:
        logging.error(f"Error querying crt.sh: {e}")
        return []

def query_hackertarget(domain):
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    logging.info(f"[*] Querying HackerTarget for {domain}")
    try:
        response = requests.get(url, timeout=10)
        if "error" in response.text.lower():
            logging.warning("HackerTarget returned an error or rate limit.")
            return []
        subdomains = set()
        lines = response.text.strip().splitlines()
        for line in lines:
            sub = line.split(',')[0]
            if sub and domain in sub:
                subdomains.add(sub)
        return list(subdomains)
    except Exception as e:
        logging.error(f"Error querying HackerTarget: {e}")
        return []

def enumerate_subdomains(domain, verbose=False):
    setup_logger(verbose)

    if not validate_domain(domain):
        logging.error("Domain validation failed. Exiting enumeration.")
        return []

    all_subdomains = set()

    # crt.sh
    subdomains_crtsh = query_crtsh(domain)
    logging.info(f"[+] Found {len(subdomains_crtsh)} subdomains from crt.sh")
    all_subdomains.update(subdomains_crtsh)

    # HackerTarget
    subdomains_hackertarget = query_hackertarget(domain)
    logging.info(f"[+] Found {len(subdomains_hackertarget)} subdomains from HackerTarget")
    all_subdomains.update(subdomains_hackertarget)

    return sorted(all_subdomains)
