import time
import os

print('CONFIGURANDO IP_TABLES...')
os.system('sudo iptables -F && sudo iptables -X && sudo iptables -Z')
os.system('sudo iptables -P INPUT ACCEPT && sudo iptables -P FORWARD ACCEPT && sudo iptables -P OUTPUT ACCEPT')
os.system('sudo iptables -t nat -A OUTPUT -p tcp --dport 80 -j REDIRECT --to-port 9040')
os.system('sudo iptables -t nat -A OUTPUT -p tcp --dport 443 -j REDIRECT --to-port 9040')
os.system('sudo iptables -t nat -A OUTPUT -p tcp --dport 21 -j REDIRECT --to-port 9040')
os.system('sudo iptables -t nat -A OUTPUT -p tcp --dport 22 -j REDIRECT --to-port 9040')

print('CONFIGURANDO TOR...')
os.system('sudo service tor start')
os.system('sudo systemctl enable tor')

os.system('trace -m')
print('ANONIMATO ATIVO')
