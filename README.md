This repository contains a Python class and some getting started
scripts to provide a simple but useful abstraction for the Robotis
Dynapixel SDK Python functions.



# AX12A Class

The scripts section below provides some useful scripts to get started
with the AX-12A actuators.  They can also be used as simple getting
started samples for how to use the [AX12A Python class](./AX12A.py)
included in this repository.  That said, the class is rather trivial
to use, containing getters/setters for all the properties in the
control table of the AX-12A actuator.  Here's a quick usage sample:

```
ax12a = AX12A("/dev/tty.usbserial-FT3WFGSI", 1);  # where 1 is the AX-12A's ID
ax12a.getId();
ax12a.setId(2);
ax12a.setGoalPosition(300);
```



# Installing and Configuring Dependencies

## Dynapixel SDK

The AX12A class abstracts the Dynamixel SDK, thus the SDK will need to
be cloned and the python libraries installed.  I'm using ~/src here as
an example, but of course, any directory will work.

```
cd ~/src
git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
cd DynamixelSDK/src/python
python3 setup.py install
```



## Configure the U2D2

Once the SDK is installed you'll need to connect the AX-12A
actuator(s).  I used the U2D2 to connect it from my Mac.  The
[instructions can be found here.](https://emanual.robotis.com/docs/en/parts/interface/u2d2)



## Determine the TTY device name

On MacOS, the USB serial tty device that represents the U2D2 can be
found by running `ls /dev/tty.usbserial*`.



# Scripts

## interrogate

[Python script](./interrogate.py) to interrogate an AX-12A actuator
using the AX12A class.

```
$ python3 interrogate.py /dev/tty.usbserial-FT3WFGSI 1
                  Model Number: 12
              Firmware Version: 24
                            Id: 1
                     Baud Rate: 1
             Return Delay Time: 250
                Cw Angle Limit: 0
               Ccw Angle Limit: 1023
             Temperature Limit: 70
             Min Voltage Limit: 60
             Max Voltage Limit: 140
                    Max Torque: 1023
           Status Return Level: 2
                     Alarm LED: 36
                      Shutdown: 36
                 Torque Enable: 1
                           LED: 0
          Cw Compliance Margin: 1
         Ccw Compliance Margin: 1
           Cw Compliance Slope: 32
          Ccw Compliance Slope: 32
                 Goal Position: 1000
                  Moving Speed: 0
                  Torque Limit: 1023
              Present Position: 997
                 Present Speed: 0
                  Present Load: 0
               Present Voltage: 126
           Present Temperature: 32
        Registered Instruction: 0
                        Moving: 0
                          Lock: 0
                         Punch: 32
```


## discover-id

[Python script](./discover-id.py) to discover the ID of the first
AX-12A actuator on the bus using the AX12A class.  This script is
useful if you have a single AX-12A actuator connected on the bus.

```
$ p3 discover-id.py /dev/tty.usbserial-FT3WFGSI
SUCCESS: Discovered a Robotis AX-12A actuator at ID 1
```



## discover-ids

[Python script](./discover-ids.py) to discover all the IDs of the
AX-12A actuators on the bus using the AX12A class.  This script is
useful if you have several AX-12A actuators connected on the bus.

```
$ p3 discover-ids.py /dev/tty.usbserial-FT3WFGSI
SUCCESS: Discovered a Robotis AX-12A actuator at ID 1
SUCCESS: Discovered a Robotis AX-12A actuator at ID 2
SUCCESS: Discovered a Robotis AX-12A actuator at ID 3
SUCCESS: Discovered a Robotis AX-12A actuator at ID 4
SUCCESS: Discovered a Robotis AX-12A actuator at ID 5
```



## set-id

[Python script](./set-id.py) to change the ID of an AX-12A actuator
using the AX12A class.

```
$ python3 set-id.py /dev/tty.usbserial-FT3WFGSI 5 9
SUCCESS: Discovered the Robotis AX-12A actuator at ID 5
Change the Robotis AX-12A actuator ID from 5 to 9? [Y/n]
SUCCESS: Updated the Robotis AX-12A actuator to ID 9
```
