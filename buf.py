import socket
from optparse import OptionParser
from colorama import init, Fore, Style

# Colorama başlat
init(autoreset=True)

# Komut satırı argümanları
parser = OptionParser()
parser.add_option("-i", "--ip", dest="host", help="Target IP", default="127.0.0.1")
parser.add_option("-p", "--port", dest="port", type="int", help="Target port", default=9090)
parser.add_option("-m", "--message", dest="msg", help="Message to send", default="Hello")
parser.add_option("-c", "--count", dest="count", type="int", help="Multiplier for message length", default=1)

(options, args) = parser.parse_args()

host = options.host
port = options.port
msg = options.msg
count = options.count

# Payload oluştur
payload = msg.encode() * count

print(Fore.GREEN + f"[+] Connecting to {host}:{port}")
print(Fore.YELLOW + f"[!] Sending payload ({len(payload)} bytes): {payload[:50]}{'...' if len(payload) > 50 else ''}")

# Socket ile gönder
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
    s.sendall(payload)
    print(Fore.CYAN + "[+] Payload sent successfully!")
except Exception as e:
    print(Fore.RED + f"[-] Connection failed: {e}")
finally:
    s.close()
