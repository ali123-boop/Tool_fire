import os, sys
from time import sleep
import time
os.system('pkg install git')
os.system('pkg install proot')
os.system('pkg install python')
os.system('pkg install bash')
os.system('pkg install python2')
os.system('clear')
def open(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
os.system('clear')
print(''' \033[0;31m
              _______________________________
              |                             |   
              |                             |
              |          Tool_fire          |
              |                             |
              |_____________________________|
 \033[1;97m''')
print('============================================================')
print('''\033[1;32m
[1].metasploit

[2].ngrok

[3].wifite

[4].phone sploit

[5].nmap

[6].hammer

[7].IPGeoLocation

[8].wifiphisher

[9].ALIENS.HaCK.Camera

[10].pemulungBTC

[11].Ledear-Hacking

[12].Router Sploit

[13].fbvid

[14].SocialBox-Termux

[15].PhoneInfoga

[16].BRUTEFORCEnew

[17].zeroeye

[18].fb-group-hack

[19].AMF1

[20].Termux basics

[21].termux-sudo

[22].virus_99

[23].Termux-Banner

[24].Xerxes

[25].FBI

[26].HxWhatsApp

[27].Card-Number

[28].seeker

[29].crips

[30].SpamCal
\033[1;97m''')
print('============================================================')
print('')
a = input('[+] Enter the tool number:')
print(a)
if a == '1' :
	os.system('clear')
	os.system('git clone https://github.com/gushmazuko/metasploit_in_termux')
	os.system('ls')
	os.system('cd metasploit_in_termux ')
	os.system('chmod +x metasploit.sh')
	os.system('./metasploit.sh')
	os.system('msfconsole')
elif a == '2' :
	os.system('clear')
	os.system('git clone https://github.com/MoMuilWH/TmX-FW')
	os.system('cd TmX-FW')
	os.system('chmod 777 TmX-FW.py')
	os.system('python2 TmX-FW.py')
elif a == '3' :
	os.system('clear')
	os.system('pkg instsll wget')
	os.system('wget https://raw.github.com/derv82/wifite/master/wifite.py')
	os.system('chmod +x wifite.py')
	os.system('apt-get update')
	os.system('apt-get upgrade')
	os.system('pkg install python2')
	os.system('python2 wifite.py')
elif a == '4' :
	os.system('clear')
	os.system('pkg install git')
	os.system('git clone https://github.com/Uditprabhakar6/PhoneSploit ')
	os.system('cd PhoneSploit')
	os.system('pip install colorama')
	os.system('python2 main_linux.py')
elif a == '5' :
	os.system('clear')
	os.system('pkg up -y')
	os.system('pkg install curl -y')
	os.system('pkg install nmap -y')
	os.system('nmap')
elif a == '6' :
	os.system('clear')
	os.system('git clone https://github.com/cyweb/hammer.git')
	os.system('cd hammer')
	os.system('chmod +x hammer.py')
	os.system('python hammer.py')
elif a == '7' :
	os.system('clear')
	os.system('git clone https://github.com/maldevel/IPGeoLocation')
	os.system('cd IPGeoLocation')
	os.system('pip install colorama')
	os.system('pip install termcolor')
	os.system('python ipgeolocation.py -t ib')
elif a == '8' :
	os.system('clear')
	os.system('pip install scapy')
	os.system('git clone https://github.com/wifiphisher/wifiphisher.git')
	os.system('cd wifiphisher')
elif a == '9' :
	os.system('clear')
	os.system('pkg install openssh ')
	os.system('pkg install php')
	os.system('termux-setup-storage')
	os.system('git clone https://github.com/hackermohamedPro/ALIENS.HaCK.Camera')
	os.system('cd ALIENS.HaCK.Camera')
	os.system('pkg install bash')
	os.system('bash alienshack.sh')
elif a == '10' :
	os.system('clear')
	os.system('git clone https://github.com/Cvar1984/pemulungBTC')
	os.system('cd pemulungBTC')
	os.system('php mulung.php')
elif a > '30' :
	print('There is no tool with this number!!')
elif a == '11' :
	os.system('clear')
	os.system('git clone https://github.com/Ledear-Hacker/LEDEAR_HACKING')
	os.system('cd LEDEAR_HACKING ')
	input('the bassword tool is Ledear-Hacking enter yes:')
	os.system('python2 ledearhacking.py')
elif a == '12' :
	os.system('clear')
	os.system('git clone https://github.com/reverse-shell/routersploit')
	os.system('cd routersploit')
	os.system('chmod +x LICENSE')
	os.system('chmod +x Makefile')
	os.system('pip2 install -r requirements-dev.txt')
	os.system('pip2 install -r requirements.txt')
	os.system('pip2 install requests')
	os.system('python rsf.py')
elif a == '13' :
	os.system('clear')
	os.system('pkg install php')
	os.system('git clone https://github.com/Tuhinshubhra/fbvid')
	os.system('cd fbvid')
	os.system('chmod +x *')
	os.system('php fb.php')
elif a == '14' :
	os.system('clear')
	os.system('git clone https://github.com/samsesh/SocialBox-Termux.git')
	os.system('cd SocialBox-Termux')
	os.system('chmod 777 install-sb.sh')
	os.system('SocialBox.sh')
	os.system('bash install-sb.sh')
	os.system('bash SocialBox.sh')
elif a == '15' :
	os.system('clear')
	os.system('git clone https://github.com/sundowndev/PhoneInfoga')
	os.system('cd PhoneInfoga')
	os.system('python3 -m pip install -r requirements.txt')
	os.system('python  phoneinfoga.py -n nmber phone')
elif a == '16' :
	os.system('clear')
	os.system('git clone https://github.com/FR13ND8/BRUTEFORCEnew')
	os.system('cd BRUTEFORCEnew')
	os.system('chmod +x *')
	os.system('sh new.sh')
elif a == '17' :
	os.system('clear')
	os.system('git clone https://github.com/skolldz/zeroeye')
	os.system('cd zeroeye')
	os.system('python dream.py')
elif a == '18' :
	os.system('clear')
	os.system('git clone https://github.com/Mr-NemrMedo/fb-group-hack')
	os.system('cd fb-group-hack')
	os.system('chmod 777 fb-group-hack.py')
	os.system('python2 fb-group-hack.py')
elif a == '19' :
	os.system('clear')
	os.system('git clone https://github.com/abdalkreemafm/AMF1')
	os.system('cd AMF1')
	os.system('chmod +x AMF1.py')
	os.system('python AMF1.py')
elif a == '20' :
	os.system('clear')
	os.system('pkg update -y')
	os.system('pkg install python -y')
	os.system('pkg upgrade -y')
	os.system('pkg install python2 -y') 
	os.system('pkg install bash')
	os.system('pkg install python2-dev -y')
	os.system('pkg install python3 -y') 
	os.system('pkg install java -y')
	os.system('pkg install fish -y')
	os.system('pkg install ruby -y') 
	os.system('pkg install help -y')
	os.system('pkg install git -y')
	os.system('pkg install host -y')
	os.system('pkg install php -y')
	os.system('pkg install perl -y') 
	os.system('pkg install nmap -y')
	os.system('pkg install bash -y') 
	os.system('pkg install clang -y') 
	os.system('pkg install nano -y') 
	os.system('pkg install w3m -y') 
	os.system('pkg install havij -y') 
	os.system('pkg install hydra -y')
	os.system('pkg install figlet -y') 
	os.systme('pkg install cowsay -y') 
	os.system('pkg install curl -y') 
	os.system('pkg install tar -y') 
	os.system('pkg install zip -y') 
	os.system('pkg install unzip -y') 
	os.system('pkg install tor -y') 
	os.system('pkg install google -y') 
	os.system('pkg install sudo -y') 
	os.system('pkg install wget -y') 
	os.system('pkg install wireshark -y') 
	os.system('pkg install wgetrc -y') 
	os.system('pkg install wcalc -y')
	os.system('pkg install bmon -y') 
	os.system('pkg install tor') 
	os.system('pkg install vpn -y') 
	os.system('pkg install unrar -y') 
	os.system('pkg install toilet -y') 
	os.system('pkg install proot -y') 
	os.system('pkg install net-tools -y') 
	os.system('pkg install golang -y') 
	os.system('pkg install chroot -y') 
	os.system('termux-chroot -y') 
	os.system('pkg install macchanger -y')
	os.system('pkg install openssl -y') 
	os.system('pkg install cmatrix -y') 
	os.system('pkg install openssh -y') 
	os.systme('pkg install wireshark -y') 
	os.system('termux-setup-storage -y') 
	os.system('pkg install macchanger -y')
	os.system('apt update && apt upgrade') 
elif a == '21' :
	os.system('clear')
	os.system('pkg install ncurses-utils')
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('cd termux-sudo')
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	os.system('sudo')
elif a == '22' :
	os.system('clear')
	os.system('pkg install git')
	os.system('pkg install python')
	os.system('git clone https://github.com/ali123-boop/virus_2021')
	os.system('cd virus_2021')
	os.system('python virus_99.py')
elif a == '23' :
	os.system('clear')
	os.system('cd $HOME')
	os.system('git clone https://github.com/Bhai4You/Termux-Banner')
	os.system('cd Termux-Banner')
	os.system('chmod 777 *')
	os.system('bash requirement.sh')
	os.system('bash t-ban.sh')
elif a == '24' :
	os.system('clear')
	os.system('git clone https://github.com/CyberXCodder/XerXes.git')
	os.system('cd XerXes')
	os.system('gcc xerxes.c -o xerxes')
	os.system('./xerxes url  80')
elif a == '25' :
	os.system('clear')
	os.system('git clone https://github.com/xHak9x/fbi.git')
	os.system('cd fbi')
	os.system('pip2 install -r requirements.txt')
	os.system('python2 fbi.py')
elif a == '26' :
	os.system('clear')
	os.system('gir clone https://github.com/Bl4ckDr460n/HxWhatsApp')
	os.system('cd HxWhatsApp')
	os.system('python2 HxWhatsApp.py')
elif a == '27' :
	os.system('clear')
	os.system('git clone https://github.com/INDOnimous/Card-Number')
	os.system('cd Card-Number')
	os.system('bash Card.sh')
elif a == '28' :
	os.system('clear')
	os.system('git clone https://github.com/thewhiteh4t/seeker')
	os.system('cd seeker')
	os.system('pip install requests')
	os.system('python seeker.py')
elif a == '29' :
	os.system('clear')
	os.system('git clone https://github.com/Manisso/Crips')
	os.system('cd Crips')
	os.system('python2 crips.py')
elif a == '30' :
	os.system('clear')
	os.system('git clone https://github.com/gutclone/SpamCal')
	os.system('cd SpamCal')
	os.system('chmod 777 SpamCall.py')
	os.system('python SpamCall.py')
