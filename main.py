import socket
import subprocess
import os
import pyfiglet
import youtube_dl
import os
os.system("'C://Documents and Settings//flow_model//flow.exe'") 
print(pyfiglet.figlet_format('     Hackster'))
print('---------------------------------------------------------')
print('Made By - @TheHackerClown,replit-ID ,github.com/TheHackerClown')
print('                                         Version - "2.0" ')

print(
    'What would you like to choose:\n1. Ip Finder\n2.Youtube Video Downloader \n3. Screen Caster\n4. Minecraft classic [made by https://github.com/fogleman]\n5. Camera\n6. Speed Test\n7. Turtle World\n8. Calculator'
)
print()
print()
command = input('user@Hackster #- ')
if command == '1':
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
elif command == '2':
    url = input('Enter the url : ')
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print('Downloaded')
elif command == '3':
    print('[only works on android]\nPlease Install the requirements to run screen caster:\nADB platform tools {https://dl.google.com/android/repository/platform-tools-latest-windows.zip}')
    print()
    print()
    exec(open('Screen Caster/scrcpy-console.bat').read())
elif command == '4':
    print('Happy Playing \"_"/')
    exec(open("Craft/mc-runner.bat").read())
elif command == '5':
    exec(open('Cam/main.py').read())
elif command == '6':
    exec(open('SpeedTest/main.py').read())
elif command == '7':
    print('Happy Playing')
    exec(open('Turtle/main.py').read())
elif command == '8':
    exec(open('Calc/main.py').read())
