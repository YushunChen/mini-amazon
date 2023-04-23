import socket

from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _VarintBytes


def get_open_socket(address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    return client_socket


def send_request_on_socket(request, socket):
    serialized_request = request.SerializeToString()
    size = request.ByteSize()
    socket.sendall(_VarintBytes(size) + serialized_request)


def recv_response_on_socket(response_type, sock):
    data = read_varint_delimited_stream(sock)
    response = response_type()
    response.ParseFromString(data)
    return response


def read_varint_delimited_stream(sock):
    size_variant = b''
    while True:
        size_variant += sock.recv(1)
        try:
            size = _DecodeVarint32(size_variant, 0)[0]
        except IndexError:
            continue
        break
    data = sock.recv(size)
    return data
