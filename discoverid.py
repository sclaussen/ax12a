from AX12A import *

# The ID is a unique value in the network to identify each
# DYNAMIXEL with an Instruction Packet. 0~252 (0xFC) values can be
# used as an ID, and 254(0xFE) is occupied as a broadcast ID. The
# Broadcast ID(254, 0xFE) can send an Instruction Packet to all
# connected DYNAMIXEL simultaneously.
# for deviceId in range(0, 252):
for deviceId in range(0, 252):
    try:
        ax12a = AX12A('/dev/tty.usbserial-FT3WFGSI', deviceId)
    except Exception as e:
        print(e)
        print("Unable to connect to the AX-12A (tty=%s, id=%s)" % ('/dev/tty.usbserial-FT3WFGSI', deviceId))
        continue
    print("SUCCESS: This AX-12A's ID is %s" % deviceId)
    break
