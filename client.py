class Client(Socket):
 
    def __init__(self):
        super(Client, self).__init__()
        self.messages = ''
 
    def set_up(self):
        try:
            self.socket.connect(
                ("127.0.0.1", 5000)
            )
 
        except ConnectionRefusedError:
            print("Sorry, server is offline!")
            exit(0)
 
        self.socket.setblocking(False)    # non-block
 
    async def listen_socket(self, listened_socket=None):    # listening
        while True:
            data = await self.main_loop.sock_recv(self.socket, 2048)    # get
            self.messages += f"{datetime.now().date()}: {data.decode('utf-8')}\n"
 
            system("cls")
            print(self.messages)
 
    async def send_data(self, data=None):
        while True:
            data = await self.main_loop.run_in_executor(None, input)  # get
            await self.main_loop.sock_sendall(self.socket, data.encode('utf-8'))
 
    async def main(self):
        await asyncio.gather(
            # all in await
            self.main_loop.create_task(self.listen_socket()),
            self.main_loop.create_task(self.send_data())
 
        )
 

if __name__ == '__main__':
    client = Client()
    client.set_up()
    client.start()
