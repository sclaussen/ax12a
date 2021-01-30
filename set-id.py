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
    print("Unable to connect to the AX-12A (tty=%s, id=%s)" % ('/dev/tty.usbserial-FT3WFGSI', oldId))
    quit(1)

print("Successfully connected to AX-12A with ID: %s" % oldId)
print("Change id from %s to %s? [Y/n] " % (sys.argv[1], sys.argv[2]), flush=True, end="")
ch = sys.stdin.read(1)
if ch == "n" or ch == "N":
    print("Ok, try again...")
    quit()

ax12a.setId(newId)
print("SUCCESS: The AX-12A's ID was updated to %s" % ax12a.getId())
