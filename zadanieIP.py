import subprocess


wynik=subprocess.check_output("ipconfig")
napis=wynik.decode(encoding="cp1252").splitlines()
for value in napis:
    if "IPv4" in value:
        print(value.split()[-1].strip())
#
# import socket
# host= socket.gethostname()
# print(socket.gethostbyname(host))
