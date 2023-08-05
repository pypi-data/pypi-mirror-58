from fabric import (
    Connection,
)
from paramiko import SSHException

import subprocess
import os
import tempfile


retry = True
connect_kwargs = dict()
while retry:
    try:
        con = Connection('datalad-test', connect_kwargs=connect_kwargs)
        chan = con.create_session()
        retry = False
    except SSHException as e:

        # try detect a paramiko issue with certain key formats
        # TODO: Link respective paramiko gh-issue
        message = str(e)
        if message.startswith("not a valid") and message.endswith("private key file"):
            # try fixing by using a temp. reformatted key:
            f_name = os.path.join(tempfile.mkdtemp(), "id_rsa")
            subprocess.run(["cp", "{}/.ssh/id_rsa".format(os.path.expanduser('~')), f_name])
            subprocess.run(["ssh-keygen", "-p", "-m", "PEM",  "-f", f_name])
            connect_kwargs['key_filename'] = f_name
        else:
            raise

        # Notes:
        # - doesn't detect the encryption in addition, but ssh-keygen asks for the passphrase
        # - should use a persistent location and set a config to include that key in the future
        # - remains fragile - we can't tell which key file paramiko stumbled upon. That it's
        #   about ~/.ssh/id_rsa is just a guess
        # - don't even know whether the issue is limited to RSA keys

print("connected: %s" % con.is_connected)


# TODO: test and time! remote execution and file transfer similar to https://github.com/psychoinformatics-de/inm7_org/issues/3
# sftp (remote exec + actual transfer) via paramiko
# sftp
# scp
# ssh remote shell
# ssh remote shell via paramiko
