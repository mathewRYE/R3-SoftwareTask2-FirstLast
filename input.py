import socket
import msvcrt as m
#dictionary that converts keyboard inputs into direction
convert = {
    "w" : "forward",
    "a" : "left",
    "s" : "backward",
    "d" : "right",
}
# dictionary that converts keyboard inputs 1-5, into a speed value
speed_convert = {
    "1" : "52",
    "2" : "102",
    "3" : "153",
    "4" : "204",
    "5" : "255",
}
HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # let's us know that server and client are connected
    print('waiting for server')
    s.connect((HOST, PORT))
    while True:
        #converts keyboard input into a string
        key = m.getwch()
        print(key)
        # if the keyboard input is located in convert dictionary, send type and value to server
        if key in convert:
            key =( f"d {convert[key]}")
            s.sendall(key.encode("utf-8"))
        # if the keyboard input is located in speed_convert dictionary, send type and value to server
        elif key in speed_convert:
            key = (f"s {speed_convert[key]}")
            s.sendall(key.encode("utf-8"))
    



