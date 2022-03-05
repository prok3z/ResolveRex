import socket
import sys
import os
from faker import Faker
import argparse
from time import sleep

#cores
red = "\033[91;1m"

print(red + """  
    { }
         {^^,
         (   `-;
    _     `;;~~ DNS RESOLVER
   /(______);
  (         ( COFFEE IS LIFE
   |:------( )
 _//         \\
/ /          vv
                      """)

def main():
  sleep(2)
  os.system(['clear', 'cls'][os.name == 'nt'])

  host = input('URL: ')

  print(red + host, "-->", socket.gethostbyname(host))
  sleep(1)
  print("Scan Finalizado Com Sucesso!")

main()
