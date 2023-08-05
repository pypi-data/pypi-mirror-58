"""Modules for using Cloudflare's API"""
import requests


def cloudflare(ip, CONFIG, log):
    """main function for cloudflare"""
    log.info("Cloudflare selected")
    log.debug(CONFIG.items("Cloudflare"))

    check = check_record(CONFIG, log)
    log.debug("Check: {}".format(check))
    if check:
        update_record(ip, check, CONFIG, log)
    else:
        add_record(ip, CONFIG, log)


def check_record(CONFIG, log):
    """Checks if an existing record already exists"""
    record = {}
    record["type"] = "A"
    record["name"] = CONFIG['Cloudflare']['name']
    output = send(record, 1, CONFIG, log)
    if output:
        return output
    return False


def add_record(ip, CONFIG, log):
    """Creates a new record"""
    record = {}
    record["type"] = "A"
    record["name"] = CONFIG['Cloudflare']['name']
    record['content'] = ip
    record['proxied'] = CONFIG['Cloudflare']['proxied'] == 'True'
    output = send(record, 2, CONFIG, log)
    if not output['success']:
        try:
            error_code = output['errors'][0]['error_chain'][0]['code']
        except KeyError:
            error_code = output['errors'][0]['code']
        # This error code means the record can not be proxied.
        # Likely due to a private IP
        if error_code == 9041:
            record['proxied'] = False
            r = send(record, 2, CONFIG, log)
            if r.json()['success']:
                log.info("The record was created successfully")
        else:
            log.error("There was an error\n")
            log.error(output['errors'])
    if output['success']:
        log.info("The record was created successfully")


def update_record(ip, record_id, CONFIG, log):
    """updates an existing record"""
    record = {}
    record["type"] = "A"
    record["name"] = CONFIG['Cloudflare']['name']
    record['content'] = ip
    output = send(record, 3, CONFIG, log, record_id)
    if not output['success']:
        log.error("There was an error:")
        log.error(output)
    else:
        log.info("Record updated successfully")


def send(content, which, CONFIG, log, extra=None):
    """Function that sends the information"""
    BASE_URL = "https://api.cloudflare.com/client/v4/zones/"
    headers = {"Authorization": "Bearer {}"
                                .format(CONFIG['Cloudflare']['API_Token']),
               "X-Auth-Email": CONFIG['Cloudflare']['Email'],
               "Content-Type": "application/json"}
    zone = CONFIG['Cloudflare']['Zone']
    api_url = BASE_URL + zone + "/dns_records"
    if which == 1:
        r = requests.get(api_url, params=content, headers=headers).json()
        log.debug(r)
        if r['result']:
            return r['result'][0]['id']
    elif which == 2:
        r = requests.post(api_url, json=content, headers=headers).json()
        log.debug(r)
        return r
    elif which == 3:
        api_url = api_url + "/" + extra
        r = requests.put(api_url, json=content, headers=headers).json()
        log.debug(r)
        return r
    return False
