import sys
from AX12A import *

if len(sys.argv) != 4:
    print("Usage: python3 setid.py TTY_NAME OLD_ID NEW_ID");
    quit(1);

ttyName = sys.argv[1];
oldId = int(sys.argv[2])
newId = int(sys.argv[3])

try:
    ax12a = AX12A('/dev/tty.usbserial-FT3WFGSI', oldId)
except Exception as e:
    print(e)
    print("ERROR: Unable to connect to the Robotis AX-12A actuator (tty=%s, id=%s)" % ('/dev/tty.usbserial-FT3WFGSI', oldId))
    quit(1)


print("SUCCESS: Discovered the Robotis AX-12A actuator at ID %s" % oldId)
print("Change the Robotis AX-12A actuator ID from %s to %s? [Y/n] " % (oldId, newId), flush=True, end="")
ch = sys.stdin.read(1)
if ch == "n" or ch == "N":
    print("Ok, try again...")
    quit()

ax12a.setId(newId)
print("SUCCESS: Updated the Robotis AX-12A actuator to ID %s" % ax12a.getId())
