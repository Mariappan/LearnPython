#!/usr/bin/env python3

from scp import SCPClient
import paramiko
import sys
import os

import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

class MySSHObject():
    def __init__(self, host):
        # Parse .ssh/config file
        ssh_config_file = os.path.expanduser("~/.ssh/config")
        conf = paramiko.SSHConfig()
        with open(ssh_config_file) as f:
            conf.parse(f)
        host_config = conf.lookup(host)
        self._host = host_config['hostname']
        self._user = host_config['user']
        self._key = os.path.expanduser(host_config['identityfile'][0])
        self._ssh = None

    def connect(self):
        # Open SSH connection
        print('Connecting to', self._host, '...')
        self._ssh = paramiko.SSHClient()
        self._ssh.load_system_host_keys()
        self._ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._ssh.connect(self._host, username=self._user, key_filename=self._key)
        print('Connected successfully to', self._host)

    # Send file thro SSH
    def send_file(self, src, dest, prog=False):
        if self._ssh is None:
            print('SSH not connected ...')
            return

        def progress(filename, size, sent):
            sys.stdout.write("%s progress: %.2f%%   \r" % (str(filename), float(sent)/float(size)*100) )
        if prog:
            scp = SCPClient(self._ssh.get_transport(), progress=progress)
        else:
            scp = SCPClient(self._ssh.get_transport())
        print('Sending', src, ' to', self._host, '...')
        scp.put(os.path.expanduser(src), dest)
        scp.close()

ssh = MySSHObject('vm')
ssh.connect()
ssh.send_file("~/dl.tgz", "dl.tgz", True)

