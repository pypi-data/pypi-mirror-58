from .lib.atc_pb2 import Status

class Default:
    channel = "/FlightData"
    rpcURL = "127.0.0.1:5555"

class Type:
    SCHEDULED = Status.SCHEDULED
    DELAYED = Status.DELAYED
    CANCELLED = Status.CANCELLED
    ON_TIME = Status.ON_TIME
    GATE_OPEN = Status.GATE_OPEN
    FINAL_CALL = Status.FINAL_CALL
    GATE_CLOSED = Status.GATE_CLOSED
    DEPARTED = Status.DEPARTED
    IN_AIR = Status.IN_AIR
    LANDED = Status.LANDED
    ARRIVED = Status.ARRIVED   
