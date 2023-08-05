#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import socket
from contextlib import closing
from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6
import platform
import os
import sys
import traceback
import threading
import time
import json


def check_if_python3():
    """
    We check if we are running Python 3.
    It may work in python 2.7 but we want to be sure to avoid issues ;)
    """
    if sys.version_info.major != 3:
        logging.error("This program must be run with Python 3.x! Exiting...")
        sys.exit(1)



def build_server_informations(address, role):
    """
    Build the message to send for discovery

    Parameters:

    address (string): ip:port
    role (string) : ocr, motion.detection, ...

    Returns:

    (json as string) : {"address" : <ip>:<port>, "role": <role>, "name": <role>@<hostname>}
    """
    hostname = get_hostname()
    name = "{0}@{1}".format(role, hostname)
    return json.dumps({"address" : address, "role" : role, "name" : name})

class ShowMeToTheLan (threading.Thread):

    def __init__(self, message):
        self.discovery_srv_addr         = ('224.0.0.1', 9999)
        # TODO : not needed for now : used only for reading
        # discovery_max_datagramSize = 8192
        self.discovery_delay_seconds    = 5
        self.message = message
        threading.Thread.__init__(self)

    def run(self):
        try:
            logging.info("Start ShowMeToTheLAN : we will emit a 'alive' message each {0} seconds".format(self.discovery_delay_seconds))
            logging.info("The alive message will be : {0}".format(self.message))

            # Create a UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.settimeout(5)

        except:
            logging.error("ShowMeToTheLAN : Error while initiating UDP dialog : {0}".format(traceback.format_exc()))
            sys.exit(1)

        while True:  # TODO : improve : thread
            #logging.debug("ShowMeToTheLAN : send '{0}'".format(self.message))
            sock.sendto(self.message.encode(), self.discovery_srv_addr)
            time.sleep(self.discovery_delay_seconds)

def get_hostname():
    return platform.node().split('.')[0]

def get_main_ip():
    """
    Return the first ip which is not 127.*

    Parameters:

    n/a

    Returns:

    (string): ip address
    """
    for intf in interfaces():
        for addr in ifaddresses(intf)[AF_INET]:   # TODO : upgrade here to handle ipv6
            ip = addr['addr']
            if not ip.startswith("127.0"):
                logging.info("Main ip is : {0}".format(ip))
                return ip
    return None

def find_free_port():
    """
    Find a free port and return it

    Parameters:

    n/a

    Returns:

    (int): a free port
    """
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        logging.info("Free port found : '{0}'".format(s.getsockname()))
        return s.getsockname()[1]

def generate_selfsigned_cert(cert_file, key_file, hostname, public_ip, private_ip):
    """
    Generate a self signed certificate for the webserver.
    If the files already exist, do nothing

    Parameters:

    cert_file (string): path to the cert file
    key_file (string): path to the key file
    hostname (string): the hostname
    public_ip (string): the public ip
    private_ip (string): the private ip

    Returns:

    n/a
    """
    try:
        # 1. check if the both files exist
        if os.path.isfile(cert_file) and os.path.isfile(key_file):
            logging.info("SSL : certificate and key files are already generated :)")
            return

        # 2. if not, generate the data
        logging.info("SSL : no certificate and key file are present. Generating them...")
        cert, key = get_selfsigned_cert(hostname, public_ip, private_ip)

        # 3. and write the files :)
        fp = open(cert_file, "w")
        fp.write(cert.decode("utf-8") )
        fp.close()

        fp = open(key_file, "w")
        fp.write(key.decode("utf-8") )
        fp.close()

        logging.info("SSL : files generated!")
    except:
        logging.error("SSL : Unable to generate the certificate and key files. The error is : {0}".format(traceback.format_exc()))

# From : https://gist.github.com/bloodearnest/9017111a313777b9cce5
def get_selfsigned_cert(hostname, public_ip, private_ip):
    from cryptography import x509
    from cryptography.x509.oid import NameOID
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import rsa

    # Fritz - patch to allow just string as input :)
    import ipaddress
    from datetime import datetime, timedelta
    #public_ip = ipaddress.ip_address(public_ip)
    #private_ip = ipaddress.ip_address(private_ip)
    # Fritz - end patch

    # Generate our key
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    name = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, hostname)
    ])
    alt_names = x509.SubjectAlternativeName([
        # best practice seem to be to include the hostname in the SAN, which *SHOULD* mean COMMON_NAME is ignored.
        x509.DNSName(hostname),
        # allow addressing by IP, for when you don't have real DNS (common in most testing scenarios)
        # openssl wants DNSnames for ips...
        x509.DNSName(public_ip),
        x509.DNSName(private_ip),
        # ... whereas golang's crypto/tls is stricter, and needs IPAddresses
        x509.IPAddress(ipaddress.IPv4Address(public_ip)),
        x509.IPAddress(ipaddress.IPv4Address(private_ip)),
    ])
    # path_len=0 means this cert can only sign itself, not other certs.
    basic_contraints = x509.BasicConstraints(ca=True, path_length=0)
    now = datetime.utcnow()
    cert = (
        x509.CertificateBuilder()
        .subject_name(name)
        .issuer_name(name)
        .public_key(key.public_key())
        .serial_number(1000)
        .not_valid_before(now)
        .not_valid_after(now + timedelta(days=10*365))
        .add_extension(basic_contraints, False)
        .add_extension(alt_names, False)
        .sign(key, hashes.SHA256(), default_backend())
    )
    cert_pem = cert.public_bytes(encoding=serialization.Encoding.PEM)
    key_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    print(cert_pem)
    print(key_pem)
    return cert_pem, key_pem
