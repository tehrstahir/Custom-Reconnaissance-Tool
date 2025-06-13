# whois_lookup.py

import whois
import logging

def get_whois_info(domain, verbose=False):
    try:
        domain_info = whois.whois(domain)
        if verbose:
            logging.info("WHOIS lookup successful.")
        return domain_info
    except Exception as e:
        logging.error(f"WHOIS lookup failed: {e}")
        return None

def print_whois_info(domain_info):
    print("\n====== WHOIS INFORMATION ======\n")
    for key, value in domain_info.items():
        print(f"{key}: {value}")
