import socket
HOST = "127.0.0.1"
PORT = 8080
speed = 0
direction = ""


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    #this print statement helps show that they are connected
    print("listening")
    conn, addr =s.accept()
    with conn:
       print('Connected by', addr)
       while True:
        #decodes the data upon receiving it from client
           data = conn.recv(1024).decode("utf-8")
           if not data:
               break
            #splits the data into type and value
           data = data.split()
            # if type is s, change the value of speed
           if data[0] == "s":
               speed = data[1]
            # if the type is d, change the value of direction
           elif data[0] == "d":
               direction = data[1]
        #prints the current speed and direction values following keyboard input
           print(f"Current Speed: {speed} Current Direction: {direction}")
           





