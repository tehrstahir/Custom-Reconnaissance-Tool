import dns.resolver

def get_dns_records(domain):
    records = {
        'A': [], 
        'MX': [], 
        'TXT': [], 
        'NS': [], 
        'CNAME': [],
        'SOA': []
    }

    try: 
        a_records = dns.resolver.resolve(domain, 'A')
        records['A'] = [r.to_text() for r in a_records]
    except Exception as e:
        records['A'] = [f"Error: {e}"]

    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        records['MX'] = [r.to_text() for r in mx_records]
    except Exception as e:
        records['MX'] = [f"Error: {e}"]

    try: 
        ns_records = dns.resolver.resolve(domain, 'NS')
        records['NS'] = [r.to_text() for r in ns_records]
    except Exception as e:
        records['NS'] = [f"Error: {e}"]

    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        records['TXT'] = [r.to_text() for r in txt_records]
    except Exception as e:
        records['TXT'] = [f"Error: {e}"]

    try:
        cname_records = dns.resolver.resolve(domain, 'CNAME')
        records['CNAME'] = [r.to_text() for r in cname_records]
    except Exception as e:
        records['CNAME'] = [f"Error: {e}"]

    try:
        soa_records = dns.resolver.resolve(domain, 'SOA')
        records['SOA'] = [r.to_text() for r in soa_records]
    except Exception as e:
        records['SOA'] = [f"Error: {e}"]

    return records
