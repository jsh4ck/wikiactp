import sys
import os
import time
import socket
import random
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet  JsHack En YT")

print (BLUE+""" 
´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´""")

print (RED+"Autor: JsHack")
print (RED+"You Tube : https://m.youtube.com/channel/UC-Kz94tNfH4ued-Ux1p9VWg")
print (RED+"github   : https://github.com/jsh4ck")


print (BLUE+"[1]: Herramientas DDoS")
print (BLUE+"[2]: Herramienta De Fuerza Bruta")
print (BLUE+"[3]: Herramientas Phising")
print (BLUE+"[4]: Herramientas Vulnerabilidades")
print (BLUE+"[5]: Herramientas Información")
print (BLUE+"[6]: Herramientas Explotacion")
opcion=input("\nElije una opcion: ")
if opcion=="1":
  os.system ("clear")
  print (RED+"""
  


  

 .########..########...#######...######.
 .##.....##.##.....##.##.....##.##....##
 .##.....##.##.....##.##.....##.##......
 .##.....##.##.....##.##.....##..######.
 .##.....##.##.....##.##.....##.......##
 .##.....##.##.....##.##.....##.##....##
 .########..########...#######...######.
""")
  
print (BLUE+"""
 [1]: Xerxes Es Una Herramienta De DDoS Muy Potente Es Muy Recomendada Sirve Demasiado No Sera Suficiente Para Tumbar Una Pagina Pero Puedes Desde Otro Telefono Usar La Misma Herramienta



$ git clone https://github.com/ngrock90/xerxes

$ cd Xerxes

$ chmod +x *

$ ./xerxes www.fakesite.com 80



 
 
 
 [2]: DDoSJs, Esta Es Mi Herramienta, No Es Tan Buena Pero Esta Funcional, Te La Recomiendo Si No Buscas Causar Mucho Daño Y Solo Una Advertencia



$ git clone https://github.com/jsh4ck/AtaqueDDoS

$ cd AtaqueDDoS

$ python ddosjs.py

Ejemplo:

IP: 92.827.748.83

Port: 80






[3]: Hammer Es Una Herramienta DDoS No Muy Potente Pero Funciona, Juntas Las Herramientas Son Potentes. 



$ git clone https://github.com/rk1342k/Hammer

$ cd Hammer 

$ python hammer.py -s [dirección ip] -t 135

ejemplo:

$ python hammer.py -s 123.45.67.89 -t 135""")
if opcion=="2":
  os.system ("clear")
  print (RED+"""
  
  
     dMMMMMP     dMMMMb 
    dMP         dMP"dMP 
   dMMMP       dMMMMK"  
  dMP         dMP.aMF   
 dMP         dMMMMP"    
                        
     dMMMMb     dMMMMb    dMP dMP  dMMMMMMP     .aMMMb 
    dMP"dMP    dMP.dMP   dMP dMP     dMP       dMP"dMP 
   dMMMMK"    dMMMMK"   dMP dMP     dMP       dMMMMMP  
  dMP.aMF    dMP"AMF   dMP.aMP     dMP       dMP dMP   
 dMMMMP"    dMP dMP    VMMMP"     dMP       dMP dMP    """)
                                                       


print (BLUE+"""

 [1]: FireCrack: 
 
$ pkg install python2

$ git clone https://github.com/Ranginang67/Firecrack

$ ls

$ cd Firecrack

$ ls

$ pip2 install -r requirements.txt

$ pip2 install mechanize


ejecutamos la herramienta con
 
$ python2 firecrack.py

escribimos el comando help
y ya de ahí ponen el comando que quieran, en este caso el comando número dos. ponen la ID de la persona a atacar

y luego ponen el nombre de su archivo de contraseñas 




[2]: Cracker: Una Herramienta Muy Buena Ya Que Por Defecto Ya Te Da Unas Contraseñas.

$ apt update && pkg upgrade -y

$ pkg install python python2 git figlet ruby -y;gem install lolcat;pip2 install mechanize -y

$ git clone https://github.com/FearFraiming/Cracker

$ cd Cracker;pip2 install -r requirements.txt

$ bash cracker.sh

Ponen El Id Del Usuario Y Ponen password.txt o ustedes pueden exportar un diccionario.


Hay Mas, Todos Tiene  La Misma Funcion, Asi Que Solo Puse Dos.""")
if opcion=="3":
  os.system ("clear")
  print (RED+"""
  
  
  
            ####       ####              ####                     
 #######  #  #       #  #    #######   #  #   #######   ####### 
 #     ## #  ####   #####    #     #  #####   #     ## ##     # 
 #  ##  # #     ##  #   #   #  #####  #   #   #  ##  # #  ##  # 
 #  ##  # #  ##  #  ##  #   ##    ##  ##  #   #  ##  # ##     # 
 #     ## #  ##  #  ##  ##  #####  #  ##  ##  #  ##  #  ##### # 
 #  ####  #  ##  #  #    #  #     ##  #    #  #  ##  #  #    ## 
 ####     ########  ######  #######   ######  ########  ######  """)

 
  
  print (BLUE+"""
 [1] SocialSploit:
  Una Herramienta Mediamente Completa, Que Tiene Las Principales Redes Y Importantes Redes Sociales, Con Un Poco De Ingeniaria Social Junto Con Esta Herramienta Son Una Bomba.
  
  
$ pkg update

$ pkg upgrade

$ pkg install -y git

$ git clone https://github.com/Cesar-Hack-Gray/SocialSploit

$ ls

$ cd SocialSploit

$ ls

$ bash install.sh

$ ./Sploit
  
  
  
  
  
  
  [2]: zphisher, es una herramienta muy completa y una de las mejores, te la recomiendo.

pkg install -y git

git clone https://github.com/htr-tech/zphisher

ls
cd zphisher

bash zphisher.sh

Escojes Una Opcion.





  [3]: SocialFish: Una Herramienta Muy Buena 🤡

$ apt update

$ apt upgrade

$ apt install git

$ apt install python2


$ git clone https://github.com/xHak9x/SocialPhish.git


$ cd SocialFish

$ chmod +x socialphish.sh

$ ./socialphish.sh


  
  
  
  
  [4]: FotoSploit Con Esta Herramienta Puedes Agregar Imagen A Tu Link De Phising Asi Que Es Mas Creible.
 

$ pkg update && pkg upgrade -y

$ pkg install -y php

$ pkg install -y python2

$ pkg install -y git

$ git clone https://github.com/Cesar-Hack-Gray/FotoSploit

$ cd FotoSploit 

$ ls




[5]: ShellPhish Otra Herramienta Muy Completa Y Recomendada 💣.

Obligatorio Ngrok)

Comandos:

pkg upgrade

 pkg install git


Repositorio 🔧

git clone https://github.com/thelinuxchoice/shellphish

Ejecutamos:🔧

cd shellphish

chmod +x shellphish.sh

./shellphish.sh

pkg install php

 pkg install curl


pkg install ssh

pkg install SSH

 pkg install openssh

 ./shellphish

bash shellphish.sh




Hay Muchas Mas Herramientas Pero Considero Que Estas Son Las Mejores...""")
if opcion=="4":
  os.system ("clear")
  print (RED+"""
  



 .##.....##.##.....##.##.......##....##.########.########.....###....########..####.##.......####.########.....###....########.
 .##.....##.##.....##.##.......###...##.##.......##.....##...##.##...##.....##..##..##........##..##.....##...##.##...##.....##
 .##.....##.##.....##.##.......####..##.##.......##.....##..##...##..##.....##..##..##........##..##.....##..##...##..##.....##
 .##.....##.##.....##.##.......##.##.##.######...########..##.....##.########...##..##........##..##.....##.##.....##.##.....##
 ..##...##..##.....##.##.......##..####.##.......##...##...#########.##.....##..##..##........##..##.....##.#########.##.....##
 ...##.##...##.....##.##.......##...###.##.......##....##..##.....##.##.....##..##..##........##..##.....##.##.....##.##.....##
 ....###.....#######..########.##....##.########.##.....##.##.....##.########..####.########.####.########..##.....##.########.""")
 
print (RED+"""
 [1] Breacher 
 
 Un script para encontrar páginas de inicio de sesión de administrador y vulnerabilidades EAR.


• Multihilos bajo demanda
• Gran lista de rutas (482 rutas)
• Admite extensiones php, asp y html
• Comprueba posibles vulnerabilidades EAR
• Verificaciones para robots.txt
• Soporte para parches personalizados

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ apt install python -y
$ git clone https://github.com/s0md3v/Breacher.git
$ cd Breacher


$ python2 breacher.py

Uso:

• Verifique todas las rutas con extensión php: python breacher -u example.com - tipo php
• Verifique todas las rutas con extensión php con hilos: python breacher -u example.com - tipo php - rápido
• Verifique todas las rutas sin hilos: python breacher -u example.com
• Agregar una ruta personalizada.

Por ejemplo, si desea que todas las rutas comiencen con /data (example.com/data / ...) puede hacer esto: python breacher -u example.com --path /data

Nota: Cuando especifica una extensión usando la opción --type, Breacher incluye rutas de esa extensión, así como rutas sin extensiones como /admin/login





[2]: GoldenEye

GoldenEye es una aplicación de Python para FINES DE PRUEBA DE SEGURIDAD SOLAMENTE! GoldenEye es una herramienta de prueba HTTP DoS. Vector de ataque explotado: HTTP Keep Alive + NoCache

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ git clone https://github.com/jseidl/GoldenEye

USO:

$ cd GoldenEye
$ chmod +x *
$ python2 goldeneye.py [url]

OPCIONES:

 -u, --useragents Archivo con agentes de usuario para usar (predeterminado: generado aleatoriamente)
-w, --workers Número de trabajadores concurrentes (predeterminado: 50)
-s, --sockets Número de sockets concurrentes (predeterminado: 30)
-m, --method Método HTTP para usar 'get' o 'post' o 'random' (valor predeterminado: get)
-d, --debug Habilitar modo de depuración [salida más detallada] (predeterminado: Falso)
-n, --nosslcheck No verificar el certificado SSL (predeterminado: True)
-h, --help Muestra esta ayuda





[3]: Hunner Framework

Este marco está diseñado para realizar pruebas de penetración.

FUNCIONES:

-Analizar vulnerabilidad sql
-Analizar vulnerabilidad xss
-DDos sitios
-Fuerza bruta ftp
-Fuerza bruta SSh
-Cuentas de correo electrónico de fuerza bruta

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python -y
$ git clone https://github.com/b3-v3r/Hunner
$ cd Hunner
$ chmod 777 hunner.py

MÉTODO DE USO:

$ python hunner.py





[4]: ClickJacking

Un script de Python diseñado para verificar si el sitio web es vulnerable al clickjacking y crea un poc.

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ apt install python -y
$ git clone https://github.com/D4Vinci/Clickjacking-Tester.git
$ cd Clickjacking-Tester
$ chmod +x *

MÉTODO DE USO:

Cree un archivo ejem:"sites.txt" aquí pegue los sitios web de las víctimas.

python clickjacking_tester.py sites.txt



 
[4]: Optiva Framework

Puede usar este marco en su sitio web para verificar la seguridad de su sitio web al encontrar la vulnerabilidad en su sitio web o puede usar esta herramienta para obtener la inyección SQL de búsqueda del panel de administración por parte de dork, así como recopilar información y cifrar Hash.

CARACTERISTICAS:

1. Módulos de información:
• Port Scanner
• Búsqueda de Whois
• Búsqueda inversa de dominio IP
• Búsqueda de dominio de encabezado HTTP
• Iplocator recupera información de geolocalización IP
2. Módulos hash:
• Texto de codificación Md5
• Texto de codificación Sha1
• SHA256 Codificar texto
• SHA384 Codificar texto
• SHA512 Codificar texto
3. Módulos de escáner:
• Scripting de sitios cruzados (XSS) • Escáner de inyección SQL (SQL)
• Vuln de inyección SQL de Dork Search
• Escáner de ejecución remota de código (RCE)
• Buscador del escáner del panel de administración del sitio web

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ git clone https://github.com/joker25000/Optiva-Framework
$ cd Optiva-Framework
$ chmod +x *
$ bash installer.sh selecciona la opción 3.

MÉTODO DE USO:

$ python2 optiva.py





[5]: Striker

Striker es un escáner de información y vulnerabilidad ofensivo.

CARACTERISTICAS:

Solo proporcione un nombre de dominio a Striker y automáticamente hará lo siguiente:
• Verificar y omitir Cloudflare
• Recuperar servidor y alimentado por encabezados
• Huella digital del sistema operativo del servidor web
• Detectar CMS (se admiten más de 197 CMS)
• Inicie WPScan si el objetivo está usando Wordpress
• Recuperar robots.txt
• Búsqueda de Whois
• Compruebe si el objetivo es un honeypot
• Escaneo de puertos con captura de pancartas
• Vuelca todo tipo de registros DNS • Genere un mapa para visualizar la superficie de ataque.
• Recopilar correos electrónicos relacionados con el objetivo
• Encuentra sitios web alojados en el mismo servidor web
• Encuentra hosts usando google
• Rastrear el sitio web en busca de URL que tengan parámetros
• Escaneo SQLi usando la implementación en línea de SQLMap (toma <3 min.)
• Escaneo XSS básico

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ git clone https://github.com/s0md3v/Striker
$ cd Striker
$ pip2 install -r requirements.txt

MÉTODO DE USO:

$ python2 striker.py





[6]: SQLMAP


sqlmap es una herramienta de prueba de penetración de código abierto que automatiza el proceso de detección y explotación de fallas de inyección SQL y toma de control de los servidores de bases de datos. Viene con un potente motor de detección, muchas funciones de nicho para el último probador de penetración y una amplia gama de interruptores que duran desde la toma de huellas digitales de la base de datos, la obtención de datos desde la base de datos, hasta el acceso al sistema de archivos subyacente y la ejecución de comandos en el sistema operativo a través de out- conexiones fuera de banda.

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ git clone https://github.com/sqlmapproject/sqlmap

MÉTODO DE USO:

$ cd sqlmap
$ chmod +x *

• Para obtener una lista de opciones básicas y conmutadores, use: python2 sqlmap.py -h

• Para obtener una lista de todas las opciones y conmutadores, use: python2 sqlmap.py -hh""")


print(RED+"Para Mi Son Las Mejores")

if opcion=="5":
  os.system ("clear")
  print (RED+"""
  
   .####.##....     ##.######      #########
 ..##   ..###...##.  ##.....    ##.....##
 ..##..   ####..##  .##......  .##.....##
 ..##.   .##.##.##.  ######..  .##.....##
 ..##.   .##..####.  ##.....  ..##.....##
 ..##.   .##...###.  ##....  ...##.....##
 .####   .##....##.  ##.... ....#########""")

print (BLUE+"""
 
 [1]: A2SV

A2SV significa Vulnerabilidad de escaneo automático a SSL. A2SV realiza un análisis de vulnerabilidades para la inyección CCS, Heartbleed, Logjam, Freak Attack, Anonymous Cipher, SSL v3 POODLE, SSL v2 Drown y Crime (SPDY).

INSTALACIÓN:

$ pkg install git -y
$ git clone https://github.com/hahwul/a2sv.git
$ cd a2sv
$ pkg install python -y
$ pip install argparse
$ pip install netaddr
$ apt-get install openssl-tool

• Correr A2SV

$ python a2sv.py -h

MÉTODO DE USO:

a2sv [-h] [-t TARGET] [-tf TARGETFILE] [-p PORT] [-m MODULE] [-d DISPLAY] [-u] [-v]

ESCANEAR SSL:

$ python a2sv.py -t 127.0.0.1
$ python a2sv.py -t 127.0.0.1 -m heartbleed
$ python a2sv.py -t 127.0.0.1 -d n
$ python a2sv.py -t 127.0.0.1 -p 8111
$ python a2sv.py -tf target_list.txt""")



print (RED+"""


[2]: AndroBugs 


AndroBugs Framework es un sistema de análisis de vulnerabilidad de Android que ayuda a los desarrolladores o hackers a encontrar posibles vulnerabilidades de seguridad en las aplicaciones de Android. Sin una interfaz GUI espléndida, pero la más eficiente (menos de 2 minutos por escaneo en promedio) y más precisa.

INSTALACIÓN:

$ apt update
$ apt upgrade
$ apt install git -y
$ apt install python2 -y
$ git clone https://github.com/AndroBugs/AndroBugs_Framework.git
$ cd AndroBugs_Framework
$ chmod +x *

METODO DE USO:

Nos dirigimos a la carpeta donde esta nuestra app:
EJEMPLO:

cd /sdcard/Download

ls

Buscamos el nombre de nuestra app y la movemos:

mv app.apk /$HOME/AndroBugs_Framework

Entramos a la carpeta AndroBugs:

cd

cd AndroBugs_Framework

ls

Ahora ejecuta este comando:

python2 androbugs.py -f app.apk -o result.txt

[*] app.apk es el nombre del apk, result.txt almacenará toda la información. Esto mostrará todos los errores y vulnerabilidades de su aplicación.""")



print (BLUE+"""

[3]: AngryFuzzer


AngryFuzz3r es una colección de herramientas para pentesting para recopilar información y descubrir vulnerabilidades de los objetivos basadas en Fuzzedb.


CARACTERISTICAS:

 • URL de fuzz establecida desde un archivo de entrada
 • Búsqueda de ruta relativa concurrente
 • Número configurable de trabajadores difusos
 • Fuzz CMS ==> Wordpress, Durpal, Joomla
 • Generar informes de las rutas válidas.

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python -y
$ git clone https://github.com/ihebski/angryFuzzer.git
$ cd angryFuzzer
$ pip install -r requirements.txt
$ pip install requests
$ chmod +x *
$ python angryFuzzer.py

MÉTODO DE USO:

$ python angryFuzzer.py -h
uso: angryFuzzer.py [opciones]

opciones:
 -h, - Muestra mensaje de ayuda.

-q, - Modo silencioso silencioso, solo informa.

-u URL, --url = URL URL del destino.

-c CMS, --cms = CMS scan CMS ==> wp, dp

 -w WORDLIST, --wordlist = WORDLIST Lista de palabras personalizada

Ejemplos:

• Fuzzing una url con diccionario predeterminado:
$ python angryFuzzer.py -u http://127.0.0.1

• CMS difuso (wp: ¡en este ejemplo!):
python angryFuzzer.py -u http://127.0.0.1 --cms wp

• Difuminar una lista de palabras personalizada:
python angryFuzzer.py -u http://127.0.0.1 -w fuzzdb / discovery / predictable-filepaths / php / PHP.txt""")


print (RED+"""


[4]: Crips IP 


Crips IP Tools: esta herramienta es una colección de herramientas IP en línea que se pueden utilizar para obtener rápidamente información sobre direcciones IP, páginas web y registros DNS.

Menú:

-Búsqueda Whois
-Traceroute
-Búsqueda DNS
-Búsqueda DNS inversa
-Búsqueda GeoIP
-Escaneo de puertos
-Búsqueda IP inversa

Instalación:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ apt install python -y
$ git clone https://github.com/Manisso/Crips
$ cd Crips
$ chmod +x *
$ ./install.sh

Uso:

$ python2 crips.py

Ahora seleccione su opción.""")



print (BLUE+"""

[5]: PureBlood


Un marco de prueba de penetración creado para Hackers / Pentester / Bug HunterWeb Pentest

Recopilación de información:

-Banner Grab Quien es
-Traceroute Registro DNS
-Búsqueda inversa de DNS
-Búsqueda de transferencia de zona -Escaneo de puertos
-Escaneo del panel de administración
-Escaneo de subdominio CMS Identify
-Búsqueda inversa de IP
-Búsqueda de subred
-Extraer enlaces de página Fuzz de directorio
-File Fuzz Shodan Search
-Shodan Host Lookup
-Ataque a la aplicación web:Wordpress Inyección automática de SQL

*Generador: Desfigurar página

*Generador de contraseñas Text To Hash

Instalación:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python -y
$ git clone https://github.com/cr4shcod3/pureblood
$ cd pureblood
$ chmod +x *
$ pip install -r requirements.txt

Uso :

$ python2 pureblood.py

Ahora seleccione su opción.""")



print (RED+"""

[6] RED HAWK


Herramienta todo en uno para recopilación de información y escaneo de vulnerabilidades.

SCANNER:

• Escaneo básico
- Título del sitio NUEVO
- Dirección IP
- Detección del servidor web MEJORADO
- Detección CMS
- Detección de Cloudflare
- Escáner robots.txt
• Búsqueda Whois MEJORADA
• Búsqueda de geo-IP
• Agarrar pancartas MEJORADO
• Búsqueda de DNS
• Calculadora de subred
• Escaneo de puertos Nmap
• Sub-Domain Scanner MEJORADO - Subdominio - Dirección IP
• Búsqueda inversa de IP y detección de CMS MEJORADO
- Nombre de host
- Dirección IP
- CMS
• Escáner SQLi basado en errores
• Bloggers Ver NUEVO
- Código de respuesta HTTP
- Título del sitio
- Ranking de Alexa
- Autoridad de dominio
- Autoridad de la página
- Extractor de enlaces sociales
- Link Grabber
• WordPress Scan NUEVO
- Archivos sensibles arrastrándose
- Detección de versión
- Versión Vulnerability Scanner
• Crawler
• Búsqueda de MX NUEVO
• Escanear para todo: el escáner Old Lame

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install php -y
$ git clone https://github.com/Tuhinshubhra/RED_HAWK

MÉTODO DE USO:

$ cd RED_HAWK
$ chmod +x *
$ php rhawk.php

• Use el comando "help" para ver la lista de comandos o escriba el nombre de dominio que desea escanear (sin Http: // O Https: //) """)



print (BLUE+"""

[7]: InfoGA


Infoga es una herramienta que recopila información de cuentas de correo electrónico (ip, nombre de host, país, ...) de diferentes fuentes públicas (motores de búsqueda, servidores de clave pgp y shodan) y comprueba si los correos electrónicos se filtraron utilizando la API de correos electrónicos pirateados.
Es una herramienta realmente simple, pero muy efectiva para las primeras etapas de una prueba de penetración o simplemente para conocer la visibilidad de su empresa en Internet.

Instalación:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python -y
$ git clone https://github.com/m4ll0k/Infoga.git infoga
$ cd infoga
$ python setup.py install
$ python infoga.py


Uso:

$ python infoga.py

Ahora muestra todas las opciones para usar esta herramienta:

$ python infoga.py -t gmail.com -s all

Ahora ha comenzado a recopilar información de correos electrónicos y correos electrónicos [nombre de host, ciudad, organización, puertos de longitud y latitud ...] """)
if opcion=="6":
  os.system ("clear")
  print (RED+"""
███████████▓▓▓▓▓▓▓▓▒░░░░░▒▒░░░░░░░▓█████
██████████▓▓▓▓▓▓▓▓▒░░░░░▒▒▒░░░░░░░░▓████
█████████▓▓▓▓▓▓▓▓▒░░░░░░▒▒▒░░░░░░░░░▓███
████████▓▓▓▓▓▓▓▓▒░░░░░░░▒▒▒░░░░░░░░░░███
███████▓▓▓▓▓▓▓▓▒░░▒▓░░░░░░░░░░░░░░░░░███
██████▓▓▓▓▓▓▓▓▒░▓████░░░░░▒▓░░░░░░░░░███
█████▓▒▓▓▓▓▓▒░▒█████▓░░░░▓██▓░░░░░░░▒███
████▓▒▓▒▒▒░░▒███████░░░░▒████░░░░░░░░███
███▓▒▒▒░░▒▓████████▒░░░░▓████▒░░░░░░▒███
██▓▒▒░░▒██████████▓░░░░░▓█████░░░░░░░███
██▓▒░░███████████▓░░░░░░▒█████▓░░░░░░███
██▓▒░▒██████████▓▒▒▒░░░░░██████▒░░░░░▓██
██▓▒░░▒███████▓▒▒▒▒▒░░░░░▓██████▓░░░░▒██
███▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░███████▓░░░▓██
███▓░░░░░▒▒▒▓▓▒▒▒▒░░░░░░░░░██████▓░░░███
████▓▒▒▒▒▓▓▓▓▓▓▒▒▓██▒░░░░░░░▓███▓░░░░███
██████████▓▓▓▓▒▒█████▓░░░░░░░░░░░░░░████
█████████▓▓▓▓▒▒░▓█▓▓██░░░░░░░░░░░░░█████
███████▓▓▓▓▓▒▒▒░░░░░░▒░░░░░░░░░░░░██████
██████▓▓▓▓▓▓▒▒░░░░░░░░░░░░░░░░▒▓████████
██████▓▓▓▓▓▒▒▒░░░░░░░░░░░░░░░▓██████████
██████▓▓▓▓▒▒██████▒░░░░░░░░░▓███████████
██████▓▓▓▒▒█████████▒░░░░░░▓████████████
██████▓▓▒▒███████████░░░░░▒█████████████
██████▓▓░████████████░░░░▒██████████████
██████▓░░████████████░░░░███████████████
██████▓░▓███████████▒░░░████████████████
██████▓░███████████▓░░░█████████████████
██████▓░███████████░░░██████████████████
██████▓▒██████████░░░███████████████████
██████▒▒█████████▒░▓████████████████████
██████░▒████████▓░██████████████████████
██████░▓████████░███████████████████████
██████░████████░▒███████████████████████
█████▓░███████▒░████████████████████████
█████▒░███████░▓████████████████████████
█████░▒██████░░█████████████████████████
█████░▒█████▓░██████████████████████████
█████░▓█████░▒██████████████████████████
█████░▓████▒░███████████████████████████
█████░▓███▓░▓███████████████████████████
██████░▓▓▒░▓████████████████████████████
███████▒░▒██████████████████████████████
████████████████████████████████████████
████████████████████████████████████████""")

print (BLUE+"""
[1]: CyberScan 

CyberScan es una herramienta de prueba de penetración de código abierto que puede analizar paquetes, decodificar, escanear puertos, hacer ping y geolocalizar una IP incluyendo (latitud, longitud, región, país ...)

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ apt install python -y
$ git clone https://github.com/medbenali/CyberScan.git
$ cd CyberScan

MÉTODO DE USO:

$ python2 CyberScan.py -v

Ayuda:

$ python2 CyberScan.py -h





[2]: D-TECT


D-TECT es una herramienta todo en uno para pruebas de penetración. Esto está especialmente programado para los probadores de penetración y los investigadores de seguridad para facilitar su trabajo, en lugar de lanzar diferentes herramientas para realizar diferentes tareas.
D-TECT proporciona múltiples funciones y funciones de detección que recopilan información del objetivo y encuentran diferentes defectos en ella.

CARACTERISTICAS:

• Escaneo de subdominios
• Escaneo de puertos
• Escaneo de Wordpress
• Enumeración de nombre de usuario de Wordpress
• Wordpress Backup Grabbing
• Detección de archivos sensibles
• Escaneo de secuencias de comandos en el mismo sitio
• Detección de jacking de clics
• Potente escaneo de vulnerabilidades XSS
• Escaneo de vulnerabilidades de inyección SQL
• Interfaz de usuario amigable

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ git clone https://github.com/shawarkhanethicalhacker/D-TECT-1.git
$ cd D-TECT-1
$ chmod +x *
$ pip2 install requests
$ python2 d-tect.py





[3]: Hakku


Hakku es un marco simple creado para herramientas de prueba de penetración. El marco Hakku ofrece una estructura simple, CLI básica y características útiles para el desarrollo de herramientas de prueba de penetración.

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python -y
$ git clone https://github.com/4shadoww/hakkuframework

MÉTODO DE USO:

$ cd hakkuframework
$ chmod +x *
$ python hakku.py

• Para ver todos los módulos, use este comando:

$ show modules

• Para mostrar todas las opciones de un módulo en particular:

$ use module name
$ show options

MODÚLOS(24):

• apache_users
• arp_dos
• arp_monitor
• arp_spoof
• bluetooth_pod
• cloudflare_resolver
• dhcp_dos
• dir_scanner
• dns_spoof
• email_bomber
• hostname_resolver
• mac_spoof
• mitm
• network_kill
• pma_scanner
• port_scanner
• proxy_scout
• whois
• web_killer
• web_scout
• wifi_jammer
• zip_cracker
• rar_cracker
• wordlist_gen





[4]: TheHarvester


theHarvester es una herramienta muy simple pero efectiva diseñada para usarse en las primeras etapas de una prueba de penetración.
Úselo para recopilar información de código abierto y ayudar a determinar el panorama de amenazas externas de una empresa en Internet.
La herramienta recopila correos electrónicos, nombres, subdominios, direcciones IP y URL utilizando múltiples fuentes de datos públicos.

INSTALACIÓN:

$ apt update && apt upgrade
$ apt install git -y
$ apt install python2 -y
$ apt install python -y
$ git clone https://github.com/laramies/theHarvester

MÉTODO DE USO:

$ cd theHarvester
$ chmod +x *
$ python2 theHarvester.py
$ python2 theHarvester.py -d site.com -b google

DATOS PUBLICOS:

• www.baidu.com
• www.bing.com
• www.censys.io
• www.crt.sh
• www.cymon.io
• dnsdumpster.com
• www.dogpile.com
• www.duckduckgo.com
• www.google.com
• google-certificates
• www.hunter.io
• www.intelx.io
• www.linkedin.com
• www.netcraft.com
• www.securitytrails.com
• www.shodanhq.com
• www.threatcrowd.org
• trello
• twitter
• vhost(Bing virtual hosts search)
• virustotal.com
• yahoo





[5]: Zarp


Zarp es una herramienta de ataque de red centrada en la explotación de redes locales. Esto no incluye la explotación del sistema, sino más bien el abuso de protocolos de red y pilas para hacerse cargo, infiltrarse y eliminar. Las sesiones se pueden administrar para envenenar y oler rápidamente varios sistemas a la vez, descargando información confidencial automáticamente o directamente al atacante. Se incluyen varios rastreadores para analizar automáticamente los nombres de usuario y las contraseñas de varios protocolos, así como ver el tráfico HTTP y más. Se incluyen ataques DoS para eliminar varios sistemas y aplicaciones. Estas herramientas abren la posibilidad de escenarios de ataque muy complejos en redes en vivo de forma rápida, limpia y silenciosa.

INSTALACIÓN:

$ apt update
$ apt upgrade
$ apt install git -y
$ apt install python2  -y
$ git clone https://github.com/hatRiot/zarp

MÉTODO DE USO:

$ cd zarp
$ chmod +x *
$ python2 zarp.py

[!] Necesario root correr con proot o tsu.""")
