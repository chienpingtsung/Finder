import argparse
import ipaddress
import logging
from multiprocessing.dummy import Pool

import paramiko

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', required=True, help='CIDR address')
parser.add_argument('-u', '--username', required=True, help='username')
parser.add_argument('-p', '--password', required=True, help='password')
args = parser.parse_args()


def test_ssh(hostname):
    hostname = str(hostname)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.client.WarningPolicy())
    try:
        ssh.connect(hostname=hostname, username=args.username, password=args.password, timeout=1)
        logging.info(f'success on {hostname}')
    except:
        pass


pool = Pool(16)
pool.map(test_ssh, ipaddress.IPv4Network(args.name))
pool.close()
pool.join()
