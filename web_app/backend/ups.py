from .utils import Utils
from . import world_amazon_pb2
from . import amazon_ups_pb2
from mini_amazon.models import Order, Stock, Product, Warehouse

import threading


class UPS(Utils):

    def init(self):
        msg = self.receive_world()
        # send back
        msg_init = amazon_ups_pb2.AUCommand()
        msg_init.acks.append(msg.seqnum)
        self.send(msg_init)
        # tell world
        self.world.init(msg.worldid)
        # update stock
        stocks = Stock.objects.all()
        for s in stocks:
            s.worldid = msg.worldid
            s.save()
        # start processing response
        responseHandler = threading.Thread(
            target=self.processResponse, args=())
        responseHandler.setDaemon(True)
        responseHandler.start()

    def setWorld(self, world):
        self.world = world

    """
    // UPS to Amazon: UPS creates a world for Amazon to connect to
    message UAstart {
        required int64 worldid = 1;
        required int64 seqnum = 2;
    }
    """

    def set_world(self):
        msg = world_amazon_pb2.UAstart()
        raw_byte = self.recv()
        msg.parseFromString(raw_byte)
        print("Received world: ", msg)
        return msg

    """
    message UACommand{
        repeated UALoadRequest loadRequests = 1;
        repeated UADelivered delivered = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    """

    def receive(self):
        msg = amazon_ups_pb2.UACommand()
        raw_byte = self.recv()
        msg.ParseFromString(raw_byte)
        print("Received message: ", msg)
        return msg

    """
    // request
    message AUCommand{
        repeated AUPickupRequest pickupRequests = 1;
        repeated AUDeliverRequest deliverRequests = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    // Amazon to UPS: when Amazon received a Buy command, it send APickupRequest to UPS to prepare a truck sent to target warehouse
    message AUPickupRequest{
        required int64 seqNum = 1;
        required int64 shipId = 2;
        required int32 warehouseId = 3;
        required int32 x = 4; // location of the warehouse
        required int32 y = 5; // location of the warehouse
        required int32 destinationX = 6;
        required int32 destinationY = 7;
    }
    """

    def pickup_request(self, worldOrder):
        print("Processing pickup request")
        msg = amazon_ups_pb2.AUCommand()
        truck = msg.pickupRequests.add()
        # warehouse info
        truck.warehouseId = worldOrder.whid
        wh = Warehouse.objects.get(whid=worldOrder.whid)
        truck.x = wh.x
        truck.y = wh.y
        # destination info
        truck.destinationX = worldOrder.x  # NOTE: check
        truck.destinationY = worldOrder.y
        truck.shipId = worldOrder.pkgid
        # TODO: any product info?
        # update sequence number
        self.seq_num += 1
        temp = self.seq_num
        truck.seqNum = temp
        self.seq_dict[temp] = msg
        # send message
        self.send(msg)

    """
    // request
    message AUCommand{
        repeated AUPickupRequest pickupRequests = 1;
        repeated AUDeliverRequest deliverRequests = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    // A -> U: when all ready, make UPS deliver the package
    message AUDeliverRequest{
        required int64 seqNum = 1;
        required int64 shipId = 2;
    }
    """

    def deliver_request(self, worldOrder):
        print("Processing deliver request")
        msg = amazon_ups_pb2.AUCommand()
        loaded = msg.deliverRequests.add()
        loaded.shipId = worldOrder.pkgid
        # update sequence number
        self.seq_num += 1
        temp = self.seq_num
        loaded.seqNum = temp
        self.seq_dict[temp] = msg
        # send message
        self.send(msg)

    """
    // response
    message UACommand{
        repeated UALoadRequest loadRequests = 1;
        repeated UADelivered delivered = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    // U -> A Arrived, ready to load
    message UALoadRequest{
        required int64 seqNum = 1;
        required int32 truckId = 2;
        required int64 shipId = 3;
    }
    """

    def load_request(self, arrived):
        print("Processing load request")
        UPSOrder = Order.objects.get(pkgid=arrived.shipId)
        UPSOrder.save()
        UPSOrder = Order.objects.get(truckid=arrived.truckId)
        self.world.put_on_truck(UPSOrder)
        return arrived.seqNum

    """
    // response
    message UACommand{
        repeated UALoadRequest loadRequests = 1;
        repeated UADelivered delivered = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    // U -> A: delivered
    message UADelivered{
        required int64 seqNum = 1;
        required int64 shipId = 2;
    }
    """

    def package_delivered(self, delivered):
        print("Processing delivered")
        return delivered.seqNum

    """
    // response
    message UACommand{
        repeated UALoadRequest loadRequests = 1;
        repeated UADelivered delivered = 2;
        repeated int64 acks = 3;
        repeated Err error = 4;
    }
    """

    def process_response(self):
        print("Processing response")
        while True:
            msg = self.receive()
            back = amazon_ups_pb2.AUCommand()
            # truck has arrived, ready to load
            for lr in msg.loadRequests:
                if lr.seqNum not in self.recv_msg:
                    self.recv_msg.add(lr.seqNum)
                    back.acks.append(self.load_request(lr))
            # package delivered
            for d in msg.delivered:
                if d.seqNum not in self.recv_msg:
                    self.recv_msg.add(d.seqNum)
                    back.acks.append(self.package_delivered(d))
            for ack in msg.acks:
                self.seq_dict.pop(ack, None)
            # send back
            self.send(back)
