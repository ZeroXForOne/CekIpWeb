import socket
import os,sys

os.system('clear')

print("""

╭━━━━╮╱╱╱╱╱╱╱╭━╮╭━╮
╰━━╮━┃╱╱╱╱╱╱╱╰╮╰╯╭╯
╱╱╭╯╭╋━━┳━┳━━╮╰╮╭╯
╱╭╯╭╯┃┃━┫╭┫╭╮┃╭╯╰╮
╭╯━╰━┫┃━┫┃┃╰╯┣╯╭╮╰╮
╰━━━━┻━━┻╯╰━━┻━╯╰━╯""")
hostname = input('Enter A Domain Name : ')
ip_address = socket.gethostbyname(hostname)

print(f'[+] Domain Name: {hostname}')
print(f'[+] IP Address: {ip_address}')
