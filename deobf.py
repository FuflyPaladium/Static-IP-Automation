# 2022 portforwarding lifetime trick 
# samay python programming 
# Cyber security expert samay 
# python object oriented programming

# ------ imports 

try:
    import os 
    import sys
    import requests
    import time
    import colorama
    import selenium
    import shutil
except ImportError:
    os.system(\'pip install requests\' if os.name==\'nt\' else \'pip3 install requests\')
    os.system(\'pip install colorama\' if os.name==\'nt\' else \'pip3 install colorama\')
    os.system(\'pip install selenium\' if os.name==\'nt\' else \'pip3 install selenium\')

from colorama import Fore
from selenium import webdriver
from selenium.webdriver.common.by import By


# ------ colors
r = "\\033[1;31m"
g = "\\033[1;32m"
y = "\\033[1;33m"
b = "\\033[1;34m"
d = "\\033[2;37m"
R = "\\033[1;41m"
Y = "\\033[1;43m"
B = "\\033[1;44m"
w = "\\033[1;37m"
g = "\\033[0;90m"
y = r


# ---------- banner and functions 

def banner():
    print(y+y+"               ) ")
    print(w+y+"              (( ")
    print(w+y+"              ) \\ ")
    print(w+y+"            (   ) ") 
    print(w+y+"            (  )  ) ") 
    print(w+y+"            ) (  ( \\ ")
    print(w+y+"          (   )$ )  ) ")
    print(w+y+"          ($$  ( \\   )           ")
    print(w+b+"    ^^^^^"+w+g+",r@@@@@@@@@@e,"+w+b+"^^^^^^   \xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/")
    print(w+b+"      ^^^"+w+g+"@@@@@@@@@@@@@@@@"+w+b+"^^^    "+w+b+"Port-Forwarding( Pro ) - version 3.0         /")
    print(w+g+"      \\@@/"+r+",:::,"+w+g+"\\/"+r+",:::,"+w+g+"\\@@       "+w+"\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/")
    print(w+g+"     /@@@|"+r+":::::"+w+g+"||"+r+":::::"+w+g+"|@@@\\\\     "+w+"Author by "+y+"@Samay825                        /")
    print(w+g+"    / @@@\\\\"+r+"\':::\'"+w+g+"/\\\\"+r+"\':::\'"+w+g+"/@@@ \\\\    "+w+"The author is not responsible             /")
    print(w+g+"   /  /@@@@@@@//\\\\\\@@@@@@@\\  \\\\   "+w+"for any issues or damage                 /")
    print(w+g+"  (  /  \'@@@@@====@@@@@\'  \\  )  "+w+"caused by this program                  /")
    print(w+g+"   \\(     /          \\     )/ "+"\\033[1;33m  \xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/")
    print(w+g+"     \\   (            )   /")
    print(w+g+"          \\          /"+w)

def returnfunc():
    samay_return = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mReturn or Exit [y/n] : "+r)
    if samay_return==\'y\' or samay_return==\'Y\':
        os.system(\'python main.py\' if os.name==\'nt\' else \'python3 main.py\')
    else:
        under()
        print_content("Exiting ...")
        sys.exit()

def clear():
    os.system(\'cls\' if os.name==\'nt\' else \'clear\')

def under():
    print(\'\
\')

about = """ 
        \\033[1;37mDeveloper  \\033[1;34m: \\033[1;31mZork
        \\033[1;37mGithub     \\033[1;34m: \\033[1;31mSamay825
        \\033[1;37mInstagram  \\033[1;34m: \\033[1;31m@sincryptzork
"""


def print_content(ops):
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37m"+ops)

def options_front():
    clear()
    banner()
    for i in about:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
    under()
    print_content(\'[ 1 ] Portforwarding Setup\')
    print_content(\'[ 2 ] Login & Start\')
    print_content(\'[ 3 ] About us\')
    print_content(\'[ 4 ] Update \')
    print_content(\'[ 5 ] Exit\')
    under()

def options_second():
    clear()
    banner()
    under()

options_front()



#-------headers



class Samay:
    project = \'portforwarding project 2022\'
    def __init__(self,data):
        self.data = data
    def Functions(self):
        if self.data==1:
            options_second()
            samay_start = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mStart the Setup Dont close After started [y/n] : "+r)
            if samay_start==\'y\' or samay_start==\'Y\':
                pass
            else:
                os.system(\'python main.py\' if os.name==\'nt\' else \'python3 main.py\')
                sys.exit()
            options_second()
            samay_email  = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Email to Create Account : "+r).strip()
            samay_email_password = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the password : "+r).strip()
            headers1 = {
                \'authority\': \'api.playit.cloud\',
                \'accept\': \'*/*\',
                \'accept-language\': \'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5\',
                \'content-type\': \'text/plain;charset=UTF-8\',
                \'dnt\': \'1\',
                \'origin\': \'https://playit.gg\',
                \'referer\': \'https://playit.gg/\',
                \'sec-fetch-dest\': \'empty\',
                \'sec-fetch-mode\': \'cors\',
                \'sec-fetch-site\': \'cross-site\',
                \'user-agent\': \'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\',
            }

            data1 = \'{"type":"create-account","email":"<email>","password":"<password>"}\'
            data1 = data1.replace(\'<email>\',samay_email)
            data1 = data1.replace(\'<password>\',samay_email_password)
            with requests.session() as s:
                d = s.post(\'https://api.playit.cloud/login\', headers=headers1, data=data1)
                if d.status_code==200:
                    pass
                else:
                    under()
                    print_content(\'check the email or retry again ..\')
                    under()
                    returnfunc()
                options_second()
                headers2 = {
                    \'authority\': \'api.playit.cloud\',
                    \'accept\': \'*/*\',
                    \'accept-language\': \'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5\',
                    \'content-type\': \'text/plain;charset=UTF-8\',
                    \'dnt\': \'1\',
                    \'origin\': \'https://playit.gg\',
                    \'referer\': \'https://playit.gg/\',
                    \'sec-fetch-dest\': \'empty\',
                    \'sec-fetch-mode\': \'cors\',
                    \'sec-fetch-site\': \'cross-site\',
                    \'user-agent\': \'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\',
                }

                data2 = \'{"type":"sign-in","email":"<email>","password":"<password>"}\'
                data2 = data2.replace(\'<email>\',samay_email)
                data2 = data2.replace(\'<password>\',samay_email_password)

                response2 = s.post(\'https://api.playit.cloud/login\', headers=headers2, data=data2)

                sessionkey = response2.json()[\'session_key\']


                print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Account Created ..")
                samay_1 = ("Your Email : "+Fore.GREEN+f"{samay_email}")
                samay_2 = ("Your Password : "+Fore.GREEN+f"{samay_email_password}")
                print_content(samay_1)
                print_content(samay_2)
                with open(\'emailpass.txt\',\'a\') as filesamay:
                    data11 = samay_1
                    data2 = samay_2
                    filesamay.write(f\'{data11}\
\')
                    filesamay.write(f\'{data2}\
\')
                    print_content("Copied email and pass into emailpass.txt you can check it out !")
                print_content("Mail has sended to your email : "+str(samay_email))
                under()
                print_content(\'type resend to resend verification code\')
                under()
                headers3 = {
                    \'authority\': \'api.playit.cloud\',
                    \'accept\': \'*/*\',
                    \'accept-language\': \'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5\',
                    \'authorization\': f\'bearer {sessionkey}\',
                    \'content-type\': \'text/plain;charset=UTF-8\',
                    \'dnt\': \'1\',
                    \'origin\': \'https://playit.gg\',
                    \'referer\': \'https://playit.gg/\',
                    \'sec-fetch-dest\': \'empty\',
                    \'sec-fetch-mode\': \'cors\',
                    \'sec-fetch-site\': \'cross-site\',
                    \'user-agent\': \'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\',
                }

                data3 = \'{"type":"send-verify-email-link"}\'

                
                verifycode = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the verification code : "+r).strip()
                

                if verifycode==\'resend\':
                    options_second()
                    under()
                    print_content(\'mail sended again ..\')
                    response3 = s.post(\'https://api.playit.cloud/login\', headers=headers3, data=data3)
                    verify2s = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the verification code : "+r).strip()
                    verifycode = verify2s



                #
                headers4 = {
                    \'authority\': \'api.playit.cloud\',
                    \'accept\': \'*/*\',
                    \'accept-language\': \'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5\',
                    \'authorization\': f\'bearer {sessionkey}\',
                    \'content-type\': \'text/plain;charset=UTF-8\',
                    \'dnt\': \'1\',
                    \'origin\': \'https://playit.gg\',
                    \'referer\': \'https://playit.gg/\',
                    \'sec-fetch-dest\': \'empty\',
                    \'sec-fetch-mode\': \'cors\',
                    \'sec-fetch-site\': \'cross-site\',
                    \'user-agent\': \'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\',
                }

                data4 = \'{"type":"verify-email","code":"<code>"}\'
                data4 = data4.replace(\'<code>\',verifycode)

                response4 = s.post(\'https://api.playit.cloud/login\', headers=headers4, data=data4)
                if response4.status_code==200:
                    under()
                    print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Checking..")
                    time.sleep(1.5)
                    print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Email Verfied")
                    print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Downloading exe file to excute !")
                    time.sleep(0.5)
                    with s.get(\'https://objects.githubusercontent.com/github-production-release-asset-2e65be/445695426/bbac8128-50dc-4a04-9e10-977fb368583f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20220917%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220917T003134Z&X-Amz-Expires=300&X-Amz-Signature=d4d0df139904192d6cc217d6b54b1e88ec65bc72cab3e402a9d6f7127ca9a2b8&X-Amz-SignedHeaders=host&actor_id=98804125&key_id=0&repo_id=445695426&response-content-disposition=attachment%3B%20filename%3Dplayit-0.9.3-signed.exe&response-content-type=application%2Foctet-stream\') as vaimsamaymandir_bikhari:
                        with open(\'static-ips.exe\',\'wb\') as samay_file_write:
                            samay_file_write.write(vaimsamaymandir_bikhari.content)
                            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Downloaded the exe file ")
                    under()
                    session_key2 = response4.json()[\'session_key\']
                    headers5 = {
                        \'authority\': \'api.playit.cloud\',
                        \'accept\': \'*/*\',
                        \'accept-language\': \'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5\',
                        \'authorization\': f\'bearer {session_key2}\',
                        \'content-type\': \'text/plain;charset=UTF-8\',
                        \'dnt\': \'1\',
                        \'origin\': \'https://playit.gg\',
                        \'referer\': \'https://playit.gg/\',
                        \'sec-fetch-dest\': \'empty\',
                        \'sec-fetch-mode\': \'cors\',
                        \'sec-fetch-site\': \'cross-site\',
                        \'user-agent\': \'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\',
                    }

                    data5 = \'{"type":"create-tunnel","tunnel_type":null,"port_type":"tcp","port_count":1,"local_ip":"127.0.0.1","local_port":<port>}\'


                    portlistner = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Listener Port to add  : "+r).strip()

                    data5 = data5.replace(\'<port>\',portlistner)

                    response5 = s.post(\'https://api.playit.cloud/account\', headers=headers5, data=data5)

                    if response5.status_code==401 or response5.status_code==200:
                        #

                        under()
                        print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Port added ")
                        print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Account Created")
                        if os.name==\'nt\':
                            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Opening chrome Browser ")
                            under()
                            time.sleep(2.0)
                            scan_path = os.path.realpath(\'Config\\chromedriverwin.exe\')
                            scan_browser_support = webdriver.Chrome(executable_path=str(scan_path))
                            url = \'https://playit.gg/login\'
                            scan_browser_support.get(url)
                            time.sleep(1.0)
                            driver_username2 = scan_browser_support.find_element(By.NAME,\'email\')
                            driver_username2.send_keys(f\'{samay_email}\')
                            driver_password2 = scan_browser_support.find_element(By.NAME,\'password\')
                            driver_password2.send_keys(f\'{samay_email_password}\')
                            login2 = scan_browser_support.find_element(By.CSS_SELECTOR,"input[type=\\"submit\\"]")
                            login2.click()
                            time.sleep(5.5)
                            url = "https://playit.gg/account/tunnels"
                            scan_browser_support.get(url)
                            time.sleep(0.8)
                            options_second()
                            print_content("Copy the tunnel Address shown in the browser ! ")
                            under()
                            driver_port = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the tunnel address : "+r)
                            driver_port_split = driver_port.split(\'.\')
                            os.system(\'\'\'wmic process where "name=\'chromedriverwin.exe\'" delete\'\'\')
                            options_second()
                            your_port = (driver_port_split[0]+\'.\'+driver_port_split[1]+\'.\'+driver_port_split[2]+\'.\'+\'gg\')
                            your_port_ip = (driver_port_split[3]).split(\':\')
                            content1 = "Your IP == "+str(your_port)
                            content2 = "Your Port == "+str(your_port_ip[1])
                            content3 = "Your Listener port == "+str(portlistner)
                            print_content(content1)
                            print_content(content2)
                            with open(\'tcp_port_ip.txt\',\'w\') as tcp:
                                tcp.write(f\'{content1}\
\')
                                tcp.write(f\'{content2}\
\')
                                tcp.write(f\'{content3}\
\')
                            print_content("Your listener port : "+str(portlistner))
                            print_content(\'Your ip address and port saved in tcp_port_ip.txt\')
                            under()
                            under()
                            samay_regis_token = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mType [y/n] : "+r)
                            if samay_regis_token==\'Y\' or samay_regis_token==\'Y\' or samay_regis_token==\'n\' or samay_regis_token==\'N\':
                                pass
                            else:
                                pass
                            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Registration of exe ")
                                # this time !
                            time.sleep(0.5)
                            options_second()
                            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Registration and all required things are installed ...")
                            os.startfile(\'static-ip.exe\')
                            os.system(\'\'\'wmic process where "name=\'chrome.exe\'" delete\'\'\')
                            time.sleep(0.4)
                            os.system(\'\'\'wmic process where "name=\'chrome.exe\'" delete\'\'\')
                            time.sleep(0.5)
                            os.system(\'\'\'wmic process where "name=\'chrome.exe\'" delete\'\'\')
                            options_second()
                            user = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the link to validate : "+r)
                            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Opening chrome Browser ")
                            under()
                            time.sleep(2.0)
                            data_path_sk = os.path.realpath(str(\'Config\\chromedriverwin.exe\'))
                            scan_browser_support = webdriver.Chrome(executable_path=str(data_path_sk))
                            scan_browser_support.get(user)
                            driver_username9 = scan_browser_support.find_element(By.NAME,\'email\')
                            driver_username9.send_keys(f\'{samay_email}\')
                            driver_password9 = scan_browser_support.find_element(By.NAME,\'password\')
                            driver_password9.send_keys(f\'{samay_email_password}\')
                            login7 = scan_browser_support.find_element(By.CSS_SELECTOR,"input[type=\\"submit\\"]")
                            login7.click()
                            options_second()
                            print(\'\
\')
                            iosj = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mType [y/n] : \
"+r)
                            os.system(\'\'\'wmic process where "name=\'chrome.exe\'" delete\'\'\')
                            options_second()
                            time.sleep(0.4)
                            os.system(\'\'\'wmic process where "name=\'static-ip.exe\'" delete\'\'\')
                            print(\'\
\')
                            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] All Registration Completed !")
                            under()
                            returnfunc()    


                else:
                    under()
                    print_content(\'Incorrect Code Retry with Other gmail\')
                    under()
                    sys.exit()
        elif self.data==2:

            with open(\'emailpass.txt\',\'r\') as ossamay:
                data_read = ossamay.read()

            data_read = data_read.replace(\'\\x1b[32m\',\'\').strip()

            samay_read_new = data_read.split()

            options_second()
            print_content(\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Logged in !\')
            under()
            with open(\'tcp_port_ip.txt\',\'r\') as _final_:
                data_final = _final_.read()
            _final_read_ = str(data_final).split()

            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Your Ip : "+Fore.GREEN+str(_final_read_[3]))
            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Your Port : "+Fore.GREEN+str(_final_read_[7]))
            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Your Listener port : "+Fore.GREEN+str(_final_read_[12]))
            under()
            _second_final = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mConnect [y/n] : "+r)
            if _second_final==\'n\':
                sys.exit()
            os.startfile(\'static-ip.exe\')
            options_second()
            print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Connected ")
            under()
            wow_final_year = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mIf you want to kill connection type \'y\' : "+r)
            if wow_final_year==\'Y\' or wow_final_year==\'y\':
                    nicework_final_year = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mConfirm [y/n] : "+r)
                    if nicework_final_year==\'y\' or nicework_final_year==\'Y\':
                        os.system(\'\'\'wmic process where "name=\'static-ip.exe\'" delete\'\'\')
                        time.sleep(0.6)
                        print_content("\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ]  killed connection ")
                        under()
                        returnfunc()
                    elif wow_final_year==\'n\' or wow_final_year==\'N\':
                        pass
                    else:
                        pass
      
        elif self.data==3:
            options_second()
            samay_write_about_func = Fore.GREEN+\'\'\'hi, i\'m Ethical Hacker Zork,\
 a passionate self-taught Powerful Ethical Hacker and C,C++,JS,Shell and Python developer and a freelance software engineer from india. my passion for software lies with dreaming up ideas and making them come true with elegant interfaces. i take great care in the experience, architecture, and code quality of the things I build.
            i am also an open-source enthusiast and maintainer. i learned a lot from the open-source community and i love how collaboration and knowledge sharing happened through open-source.
            
            \'\'\'
            for i in samay_write_about_func:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.01)
            print(\'\
\')
            returnfunc()
        elif self.data==4:
            os.system(\'python update.py\')
        else:
            under()
            print_content(\'Exiting ..\')
            under()
            sys.exit()
                








try:
    userdata2 = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mEnter the Desire option : "+r))
except:
    under()
    print_content(\'Put numbers to choose options not letters ..\')
    under()
    sys.exit()

if __name__ == \'__main__\':
    Vrushabh = Samay(userdata2)
    Vrushabh.Functions()
