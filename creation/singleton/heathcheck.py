

class HeathCheck:
    __instance = None
    def __new__(self, *args, **kwds):
        if self.__instance is None:
            self.__instance = super(HeathCheck, self).__new__(self, *args, **kwds)
        return self.__instance

    def __init__(self):
        self.servers = []

    def add_servers(self):
        self.servers.append("server_1")
        self.servers.append("server_2")
        self.servers.append("server_3")
        self.servers.append("server_4")

    def change_servers(self):
        self.servers.pop()
        self.servers.append("server_5")

    def update_servers(self):
        self.servers.pop()
        self.servers.append("server_6")


if __name__ == "__main__":
    hc1 = HeathCheck()
    hc2 = HeathCheck()
    hc1.add_servers()
    
    print("\nScheduled Heath Check (1) for server...")
    for i in hc1.servers:
        print(f"Checking {i}")
    
    hc2.change_servers()
    print("\nScheduled Heath Check (2) for server...")
    for i in hc2.servers:
        print(f"Checking {i}")

    hc1.update_servers()
    print("\nScheduled Heath Check (1) for server...")
    for i in hc1.servers:
        print(f"Checking {i}")
    print("\nScheduled Heath Check (2) for server...")
    for i in hc2.servers:
        print(f"Checking {i}")

