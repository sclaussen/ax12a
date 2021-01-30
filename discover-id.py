import sys
from AX12A import *

if len(sys.argv) != 2:
    print("Usage: python3 discover-id.py TTY_NAME");
    quit(1);

ttyName = sys.argv[1]


# The ID is a unique value in the network to identify each
# DYNAMIXEL with an Instruction Packet. 0~252 (0xFC) values can be
# used as an ID, and 254(0xFE) is occupied as a broadcast ID. The
# Broadcast ID(254, 0xFE) can send an Instruction Packet to all
# connected DYNAMIXEL simultaneously.
# for deviceId in range(0, 252):
for deviceId in range(0, 252):
    try:
        ax12a = AX12A(ttyName, deviceId)
    except Exception as e:
        continue
    print("SUCCESS: Discovered a Robotis AX-12A actuator at ID %s" % deviceId)
    break
