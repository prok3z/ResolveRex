import socket
import sys
import os
from faker import Faker
import argparse
from time import sleep

#cores
red = "\033[91;1m"

print(red + """....._      
 `.   ``-.                               .-----.._
   `,     `-.   DNS RESOLVER            .:      /`
     :       `".. Simple Tool Scan ..-``       :
     /   ...--:::`n            n.`::...       :
     `:``      .` ::          /  `.     ``---..:.
       `\    .`  ._:   .-:   ::    `.     .-``
         :  :    :_\\_/: :  .::      `.  /
         : /      \-../:/_.`-`         \ :
         :: _.._  q` p ` /`             \|
         :-`    ``(_. ..-----hh``````/-._:
                     `:      ``     /     `
                     E:            /
       [dock]         :          _/
                      :    _..-``
                      l--``""")
sleep(2)
os.system(['clear', 'cls'][os.name == 'nt'])

host = input('URL: ')

print(host,red + "-->", socket.gethostbyname(host))