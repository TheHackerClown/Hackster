import socket
import youtube_dl
import subprocess
import sys, string, os
import pyglet
import cv2
import speedtest
import turtle 
print('██╗░░██╗░█████╗░░█████╗░██╗░░██╗░██████╗████████╗███████╗██████╗░')
print('██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗')
print('███████║███████║██║░░╚═╝█████═╝░╚█████╗░░░░██║░░░█████╗░░██████╔╝')
print('██╔══██║██╔══██║██║░░██╗██╔═██╗░░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗')
print('██║░░██║██║░░██║╚█████╔╝██║░╚██╗██████╔╝░░░██║░░░███████╗██║░░██║')
print('╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝')




print()
print()
print('Made By - @TheHackerClown,replit-ID ,github.com/TheHackerClown')
print('                                         Version - "1.0" ')

print('What would you like to choose:\n1. Ip Finder\n2.Youtube Video Downloader \n3. Screen Caster\n4. Minecraft classic [made by https://github.com/fogleman]\n5. Camera\n6. Speed Test\n7. Turtle World\n8. Calculator')
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
  print('Please double-click scrcpy-console.bat in this folder')
elif command == '4':
  print('Now Happy Playing ')
  os.system("craft.exe")
elif command == '5':
  vid = cv2.VideoCapture(0)
  while(True):
    ret, frame = vid.read()
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  vid.release()
  cv2.DestroyAllWindows()
elif command == '6':
  st = speedtest.Speedtest()
  option = int(input('''What speed do you want to test:\n1) Download Speed\n2) Upload Speed\n3) Ping\nYour Choice: '''))
  if option == 1:  
    print('All thing in bits')
    print(st.download())  
  elif option == 2: 
    print('All thing in bits')
    print(st.upload())  
  elif option == 3:  
  
    servernames =[]  
  
    st.get_servers(servernames)  
  
    print(st.results.ping)  
  else:
  
    print("Please enter the correct choice !") 
elif command == '7':
  print('Happy Playing')
  wn=turtle.Screen()      

  babbage=turtle.Turtle() 

  babbage.shape("turtle") 

  move_speed = 15

  turn_angle = 18

  def forward():
    babbage.forward(move_speed)

  def backward():
    babbage.backward(move_speed)

  def left():
    babbage.left(turn_angle)

  def right():
    babbage.right(turn_angle)

  wn.onkey(forward,"Up")

  wn.onkey(backward,"Down")

  wn.onkey(left,"Left")

  wn.onkey(right,"Right")

  wn.listen()
elif command == '8':
  exec(open('calcul.py').read())