st = speedtest.Speedtest()
    option = int(input('''What speed do you want to test:\n1) Download Speed\n2) Upload Speed\n3) Ping\nYour Choice: '''))
    if option == 1:
      print('All thing in bits')
      print(st.download())
    elif option == 2:
      print('All thing in bits')
      print(st.upload())
    elif option == 3:
      servernames = []
      st.get_servers(servernames)
      print(st.results.ping)
    else:
      print("Please enter the correct choice !")