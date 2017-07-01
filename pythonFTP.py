#!/usr/bin/python
# -*- coding: utf-8 -*-
import ftplib
import os
import socket

HOST = '47.93.217.185'
DIRN = 'phpProject/'
FILE = 'Jack.php'

USER = '******'
PASSWORLD = '******'
#def main():
#    try:
#        f = ftplib.FTP()
#    except (socket.error, socket.gaierror):
#        print 'ERROR:cannot reach " %s"' % HOST
#        return
#    print '***Connected to host "%s"' % HOST
#    try:
#        timeout = 300
#        port = 21
#        f.connect(HOST,port,timeout) # 连接FTP服务器
#
#    except ftplib.error_perm:
#        print 'ERROR: cannot connect anonymously'
#        f.quit()
#        return
#
#    try:
#        f.login(USER,PASSWORLD)
#    except ftplib.error_perm:
#        print 'ERROR: cannot login anonymously'
#        f.quit()
#        return
#        print '*** Logged in as "anonymously"'
#    try:
#        f.cwd(DIRN)
#    except ftplib.error_perm:
#        print 'ERRORL cannot CD to "%s"' % DIRN
#        f.quit()
#        return
#        print '*** Changed to "%s" folder' % DIRN
#    try:
#        #传一个回调函数给retrbinary() 它在每接收一个二进制数据时都会被调用
#        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
#    except ftplib.error_perm:
#        print 'ERROR: cannot read file "%s"' % FILE
#        os.unlink(FILE)
#    else:
#        print '*** Downloaded "%s" to CWD' % FILE
#    f.quit()
#    return
from ftplib import FTP as _FTP

class FTP():
    
    def __init__(self,ip='47.93.217.185',port=21,timeout=60):
        self.ip = ip
        self.port = port
        self.timeout = timeout
        self.ftp = _FTP()
    
    def __del__(self):
        self.quit();
    
    def login(self,user=USER,passworld=PASSWORLD):
        # FTP编程
        ftp = self.ftp
#        timeout = 500
#        port = 21
        print "ftp connect ..."
        ftp.connect(self.ip,self.port,self.timeout) # 连接FTP服务器
        print "ftp login ...."
        ftp.login(user,passworld) # 登录
        print ftp.getwelcome()  # 获得欢迎信息
        print "ftp cmd cd"
        ftp.set_pasv(False) #解决等待过长passive
        
        ftp.cwd(DIRN)    # 设置FTP路径
        list = ftp.nlst()       # 获得目录列表
        print "ftp file list\r\n###########:\r\n"
        for name in list:
            pass
        # print(name)             # 打印文件名字
        print '\r\n############\r\nlogin success'
        return ftp
    

#    ftp.storlines('test44.py', w) # 上传FTP文件
#    ftp.quit()                  # 退出FTP服务器

    def upload(self,remotepath,localpath):
        #    f.close()
        #    ftp.delete(name)            # 删除FTP文件
        w = open(localpath,'rb')
        self.ftp.storbinary("STOR "+remotepath,w)  #上传目标文件


    def download(self,remtepath,localpath):
        path =  localpath    # 文件保存路径
        f = open(path,'wb')         # 打开要保存文件
        filename = 'RETR ' + remtepath   # 保存FTP文件
        self.ftp.retrbinary(filename,f.write) # 保存FTP上的文件
    
    def mkdir(self,dirname):
        #       self.ftp.rmd(dirname)
        self.ftp.mkd(dirname)

    def quit(self):
        self.ftp.quit()


def uploadToFTP(path):
    import os ,time
#    from login_ali import *
    from login_ali import Ali_ssh as ssh
                            #/Users/rainpoll/Desktop/icon
    newpath = path+".zip"   # newpath /Users/rainpoll/Desktop/icon.zip
#    print "newpath",newpath
    
    url = path
    result = url.split("/")[-1]
    if len(result) < 1:
        result = url.split("/")[-2]
    print 'result',result  #result icon
    if os.path.isfile(path):
        f = FTP()
        f.login()

        print 'start upload to servers'
        f.upload(result,path)
        ss = ssh()
        ss.exec_command('chmod -R 777 /var/www/html/phpProject/')
        print 'upload to servers success'
    else :
        os.chdir(path)
        pardir = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
    #    print "+++++++",pardir  #/Users/rainpoll/Desktop
        print 'start create zip files'
        time.sleep(1)
    #    os.chdir(pardir)
        os.system('cd '+path)
    #    os.system('pwd')
        os.system('zip -r '+newpath+' '+'*')
        os.system('chmod -777 '+newpath)
        time.sleep(1)
        f = FTP()
        f.login()
        f.upload(result+'.zip',newpath)
        os.system('rm '+newpath)
        ss = ssh()
        old = newpath
        re = old.replace('./','/')

        rmpath = '/var/www/html/phpProject/'+result+'.zip'  #os.path.join('/var/www/html/phpProject',rootdir)
        print 'rmpath  ',rmpath
        print 'start upload to servers'
        #   ss.exec_command('rm -r '+rmpath)
        ss.exec_command('chmod -R 777 /var/www/html/phpProject/')
        ss.exec_command('cd /var/www/html/phpProject/ \n sudo unzip -o '+result+'.zip','A')
        ss.exec_command('chmod -R 777 /var/www/html/phpProject/')
        ss.exec_command('cd /var/www/html/phpProject/ \n rm '+result+'.zip','A')
        print 'upload to servers success'
    ss.close()



def main():
    import os, sys, stat
    from login_ali import Ali_ssh as ssh
    
    f = FTP()
    f.login()
    rootdir = './t/'
    
#    strFileName = rootdir
#    n = strFileName.ReverseFind('\\'); #从后往前寻找
#    strFilePath = strFileName.Left(n);
#    strFileName = strFileName.Right( strFileName.GetLength()-(n+1) );
#    print strFilePath
#    print strFileName;
    url = rootdir
    result = url.split("/")[-1]
    if len(result) < 1:
        result = url.split("/")[-2]
    
#    print 'result',result

    if os.path.isdir(rootdir):
        try :
            ss = ssh()
            old = rootdir
            re = old.replace('./','/')
            rmpath = '/var/www/html/phpProject'+re  #os.path.join('/var/www/html/phpProject',rootdir)
            print rmpath
            print ss.exec_command('rm -r '+rmpath)

            f.mkdir(result)
        
        except ftplib.error_perm:
            print "mkdir false"

    for parent,dirnames,filenames in os.walk(rootdir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    #            print "parent :  ",parent
    #            print "filename :  ",filename
        for dirname in dirnames:

            dir = os.path.join(parent,dirname)
            print "dir ***",dir
            try :
                # ss.exec_command('rm -r /var/www/html/phoProject/'+dir)
                f.mkdir(dir)
            except ftplib.error_perm:
                print "mkdir false"


        for filename in filenames:
            path = os.path.join(parent,filename)
            print "full file name of file is : ",path
            if os.path.isfile(path):
                print "path ---",path
                oldpath = path.replace('rootdir','')
                
                f.upload(oldpath,path)
            
            if os.path.isdir(path):
                print "dir ----",path

def arg():
    
    import sys, time
    print 'please enter dir path or file path !!'
#    name = raw_input()
#    print name

#    if len(name) > 0:
#        pass
#    else:
#        opt()

    if len(sys.argv) <= 1:
        print 'please enter dir path or file path !!'
        sys.exit()

    print 'check python module ....'
    time.sleep(1)
    tryModule('ftplib')
    print 'check ftplib module ....ok!'

# tryModule('paramiko')
    print 'check paramiko module ....ok!'
    time.sleep(1)
    for i in range(1, len(sys.argv)):
        print i, sys.argv[i]
        path = sys.argv[i]
        uploadToFTP(path)

#    if len(name) > 0:
#        uploadToFTP(name)


    if "-help" in sys.argv:
        help();
        return


def tryModule(module):
    import imp,sys
    try:
            #		imp.find_module(module)
        print 'try find module'
        found = True
        imp.find_module(module)
    except ImportError:
        found = False
        print 'not found module'
        import time, os
        print 'start download '+module
        time.sleep(2)
        os.system('sudo pip install '+module)
        print 'check down files'
        time.sleep(1)

    try:
        imp.find_module(module)
    except ImportError:
        print "error: module not found "
        print "application will exit, please download "+module+" module by youself"
        sys.exit(0)

def opt():
    import sys, getopt
    opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
    input_file=""
    output_file=""
    
    for op, value in opts:
        if op == "-i":
            input_file = value
        elif op == "-o":
            output_file = value
        elif op == "-h":
            help()
            sys.exit()

def help():
    print " are you SB ?"

if __name__ == '__main__':
    arg()


