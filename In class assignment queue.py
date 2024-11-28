class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self, val):
        if val not in self.queue:
            self.queue.insert(0,val)
            return True
        return False

    def size(self):
        return len(self.queue)
    
TheQueue = Queue()
TheQueue.addtoq("New Hampshire")
TheQueue.addtoq("Massachusetts")
TheQueue.addtoq("Rhode Island")
TheQueue.addtoq("Connecticut") 
TheQueue.addtoq("New York")
TheQueue.addtoq("New Jersey")
TheQueue.addtoq("Delaware")
TheQueue.addtoq("Maryland")
TheQueue.addtoq("District of Columbia")
TheQueue.addtoq("Virginia")
TheQueue.addtoq("North Carolina")
TheQueue.addtoq("South Carolina")
TheQueue.addtoq("Georgia")
TheQueue.addtoq("Florida")

TheQueue.addtoq()

