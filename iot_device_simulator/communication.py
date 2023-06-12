# comment each line with an explination, 
# at the end the code should be veiwed as it is written by you (a professional developer)

class Communication:
    def __init__(self, server_url):
        self.server_url = server_url

    def send_data(self, data):
        print(f"Sending data to {self.server_url}: {data}")

    def receive_data(self):
        print(f"Receiving data from {self.server_url}")
