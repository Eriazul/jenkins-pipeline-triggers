import socket
import os
//HI
def main():
    hostname = socket.gethostname()
    print(f"Name of the server: {hostname}")
    print(f'The current directory is: {os.getcwd()}')

if __name__ == "__main__":
    main()
        
