import paramiko

class SSHClient:
    def __init__(self, ip, username, password):
        self.client = paramiko.SSHClient()
        self.client.connect(ip, username=username, password=password)

    def execute(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode()