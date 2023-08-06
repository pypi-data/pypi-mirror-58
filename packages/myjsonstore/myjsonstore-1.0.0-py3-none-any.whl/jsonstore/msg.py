from termcolor import colored as c

alert = lambda msg: c("[!] ","red") + msg
plus = lambda msg: c("[+] ","green") + msg
star = lambda msg: c("[*] ","cyan") + msg
loot = lambda msg: c("[$] ","green") + msg
minus = lambda msg: c("[-] ","yellow") + msg