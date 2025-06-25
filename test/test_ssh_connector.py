import unittest
from unittest.mock import Mock, patch
from ssh_connector.ssh_client import SSHClient

class TestSSHClient(unittest.TestCase):
    @patch('paramiko.SSHClient')
    def test_execute_command(self, mock_ssh):
        # 创建模拟连接
        mock_client = Mock()
        mock_ssh.return_value = mock_client
        
        # 设置模拟输出
        mock_exec = mock_client.exec_command
        mock_exec.return_value = (None, Mock(read=Mock(return_value=b'success')), None)
        
        # 测试执行命令
        client = SSHClient("192.168.1.1", "admin", "password")
        result = client.execute("show version")
        
        # 验证结果
        self.assertEqual(result.strip(), "success")
        # 验证调用参数
        mock_exec.assert_called_once_with("show version")

if __name__ == '__main__':
    unittest.main()