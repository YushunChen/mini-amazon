import socket
import threading

import amazon_ups_pb2 as ups
import world_amazon_pb2 as world

from pb_utils import recv_response_on_socket as recv_response
from pb_utils import send_request_on_socket as send_request
from pb_utils import get_open_socket
from db_utils import connect_db


WEBAPP_ADDRESS = ("0.0.0.0", 45678)
WORLD_ADDRESS = ("vcm-32290.vm.duke.edu", 23456)
# TODO: change this to the correct address
UPS_ADDRESS = ("vcm-32290.vm.duke.edu", 8888)

world_socket = get_open_socket(WORLD_ADDRESS)


def connect_webapp(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(address)
    sock.listen(10)
    webapp_socket, _ = sock.accept()
    sock.close()
    return webapp_socket


def build_connect_world_request():
    _, cursor = connect_db()

    query = f"""
        SELECT id, location_x, location_y
        FROM amazon_frontend_warehouse
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    initWarehouses = []
    for row in rows:
        initWarehouse = world.AInitWarehouse()
        initWarehouse.id = row[0]
        initWarehouse.x = row[1]
        initWarehouse.y = row[2]
        initWarehouses.append(initWarehouse)

    request = world.AConnect()
    # request.worldid = world_id
    request.isAmazon = True
    for initWarehouse in initWarehouses:
        request.initwh.add().CopyFrom(initWarehouse)

    return request


# Start server
print("Starting Mini Amazon server...")

world_socket = get_open_socket(WORLD_ADDRESS)
# ups_socket = get_open_socket(UPS_ADDRESS)
webapp_socket = connect_webapp(WEBAPP_ADDRESS)

# Connect to world
request = build_connect_world_request()
send_request(request, world_socket)
response = recv_response(world.AConnected, world_socket)
print(response.result)
