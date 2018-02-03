import paramiko

def fileTransfer(folder):
    tranferAgent= paramiko.SSHClient()
    tranferAgent.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    tranferAgent.connect("192.168.2.21",2222,username="Bryan-Elliott's_Fire",password='123')
    
    sftp = tranferAgent.open_sftp()
    sftp.put(r'C:\Users\Utilisateur\Documents\Python_Scripts\webScraping\manga\mangaScrapper\15.jpg', 
             r'\storage\sdcard1\Manga\15.jpg')  
fileTransfer('l')