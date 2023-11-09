import random

class Packet:
    
    
    def __init__(self, PacketSize, ArrivalTime, ServiceStartTime, ServiceEndTime, Wait =0):
        self.PacketSize = PacketSize
        self.ArrivalTime = ArrivalTime
        self.ServiceStartTime = ServiceStartTime
        self.ServiceTime = ServiceEndTime - ServiceStartTime
        self.ServiceEndTime = ServiceEndTime
        self.Wait = Wait


def Simulation(avgSize, avgTime, RunTime):
    t = 0
    Queue = []
    ArrivalTime = 0
    ServiceEndTime = 0
    PacketData = []
    PacketWaitingTime = []
    Wait = 0
    
    while t < RunTime:

        #Retrieve Packet Information
        ArrivalTime += CalcTime(avgTime)
        PacketSize = PacketSizing(avgSize)

        #Time keeping
        t = ArrivalTime
        print("Time: ", t)
        
        if ArrivalTime >= ServiceEndTime and len(Queue)==0:
            ServiceStartTime = ArrivalTime
            ServiceEndTime, Wait = ServicePacket(ArrivalTime, ServiceStartTime, PacketSize)
            PacketData.append(Packet(PacketSize, ArrivalTime, ServiceStartTime, ServiceEndTime, Wait))
            PacketWaitingTime.append(PacketData[-1].Wait)


        else:
            ServiceStartTime = ServiceEndTime
            ServiceEndTime, Wait = ServicePacket(ArrivalTime, ServiceStartTime, PacketSize)


            PacketData.append(Packet(PacketSize, ArrivalTime, ServiceStartTime, ServiceEndTime, Wait))
            PacketWaitingTime.append(PacketData[-1].Wait)

                




        
        print("PacketSize: ", PacketSize)
        print("ArrivalTime: ", ArrivalTime)
        print("ServiceStartTime: ", ServiceStartTime)
        print("ServiceEndTime: ", ServiceEndTime)
        print("ServiceTime: ", PacketData[-1].ServiceTime, "\n\n")

        print(PacketWaitingTime)

        


        
    
def CalcStats():
    return

def CalcTime(x):
    InterArrivalTime = 100*(random.expovariate(x))
    return InterArrivalTime

def PacketSizing(avgSize):
#    PacketSize = np.random.exponential(avgSize)
    return 5

def ServicePacket(ArrivalTime, ServiceStartTime, PacketSize):
    ServiceEndTime = ServiceStartTime + CalcTime(PacketSize)
    if ArrivalTime != ServiceStartTime:
        Wait = ServiceStartTime - ArrivalTime
    else:
        Wait = 0
    return ServiceEndTime, Wait   


Simulation(5,10,100)
