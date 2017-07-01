import paramiko  


class Ali_ssh():
    def __init__(self,hostname='47.93.217.185', port=22, username='****', password='*******'):
        paramiko.util.log_to_file("paramiko.log")
    
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
        self.ssh.connect(hostname=hostname, port=port, username=username, password=password)
#        stdin, stdout, stderr = s.exec_command (execmd)
#        stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
#    
#        print stdout.read()
#        cmd_in, cmd_out, err = s.exec_command('chmod -R 777 /var/www/html/phpProject/')
#        cmd_in.write('-a')
#        print cmd_out.read()
#    
#        cmd_in_1, cmd_out_1, err_1 = s.exec_command('ls /var/www/html/phpProject/')
#        cmd_in_1.write('-a')
#        print cmd_out_1.read()
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
    
    def __del__(self):
        self.ssh.close()
    def close(self):
        self.ssh.close()

    def exec_command(self,cmd,write_in=''):
#        stdin, stdout, stderr = self.ssh.exec_command ('free')
#        stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
#        print stdout.read()
        cmd_in, cmd_out, err = self.ssh.exec_command(cmd)
        if write_in=='':
            pass
        else:
            cmd_in.write(write_in)
#        print err
        return cmd_out.read()

def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")  
      
    s = paramiko.SSHClient()  
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
    s.connect(hostname=hostname, port=port, username=username, password=password)
    
    stdin, stdout, stderr = s.exec_command ('free')
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.  

    print stdout.read()  
    cmd_in, cmd_out, err = s.exec_command('chmod -R 777 /var/www/html/phpProject/')
    cmd_in.write('-a')
    print cmd_out.read()
    
    cmd_in_1, cmd_out_1, err_1 = s.exec_command('ls /var/www/html/phpProject/')
    cmd_in_1.write('-a')
    print cmd_out_1.read()
    
    cmd_in_1, cmd_out_1, err_1 = s.exec_command('ls /var/www/html/phpProject/')
    cmd_in_1.write('-a')
    print cmd_out_1.read()
    
    print 'process ok!!!'
    s.close()
      
def main():  
     
    hostname = '47.93.217.185'  
    port = 22  
    username = '****'
    password = '*******'
    execmd = "free"  
   
#    tryModule('paramiko')
  
    sshclient_execmd(hostname, port, username, password, execmd)  
      
      
if __name__ == "__main__":  
    main()  
