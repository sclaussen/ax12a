import dynamixel_sdk as sdk

# EEPROM Control Area (durable)
FIELD_MODEL_NUMBER = 0
FIELD_FIRMWARE_VERSION = 2
FIELD_ID = 3
FIELD_BAUD_RATE = 4
FIELD_RETURN_DELAY_TIME = 5
FIELD_CW_ANGLE_LIMIT = 6
FIELD_CCW_ANGLE_LIMIT = 8
FIELD_TEMPERATURE_LIMIT = 11
FIELD_MIN_VOLTAGE_LIMIT = 12
FIELD_MAX_VOLTAGE_LIMIT = 13
FIELD_MAX_TORQUE = 14
FIELD_STATUS_RETURN_LEVEL = 16
FIELD_ALARM_LED = 17
FIELD_SHUTDOWN = 18

# RAM Control Area (transient)
FIELD_TORQUE_ENABLE = 24
FIELD_LED = 25
FIELD_CW_COMPLIANCE_MARGIN = 26
FIELD_CCW_COMPLIANCE_MARGIN = 27
FIELD_CW_COMPLIANCE_SLOPE = 28
FIELD_CCW_COMPLIANCE_SLOPE = 29
FIELD_GOAL_POSITION = 30
FIELD_MOVING_SPEED = 32
FIELD_TORQUE_LIMIT = 34
FIELD_PRESENT_POSITION = 36
FIELD_PRESENT_SPEED = 38
FIELD_PRESENT_LOAD = 40
FIELD_PRESENT_VOLTAGE = 42
FIELD_PRESENT_TEMPERATURE = 43
FIELD_REGISTERED_INSTRUCTION = 44
FIELD_MOVING = 46
FIELD_LOCK = 47
FIELD_PUNCH = 48

class AX12A:
    ttyName = None
    tty = None
    deviceId = None
    protocol = sdk.PacketHandler(1.0)

    # EEPROM Control Area (durable)

    def __init__(self, tty, deviceId):
        self.ttyName = tty
        self.tty = sdk.PortHandler(tty)
        self.deviceId = deviceId
        # Verify that the connection over the tty to the deviceId
        # specified works
        self.getId()


    # This address stores model number of DYNAMIXEL.
    def getModelNumber(self):
        return self.__read2(FIELD_MODEL_NUMBER)



    # This address stores firmware version of DYNAMIXEL.
    def getFirmwareVersion(self):
        return self.__read1(FIELD_FIRMWARE_VERSION)



    # The ID is a unique value in the network to identify each
    # DYNAMIXEL with an Instruction Packet. 0~252 (0xFC) values can be
    # used as an ID, and 254(0xFE) is occupied as a broadcast ID. The
    # Broadcast ID(254, 0xFE) can send an Instruction Packet to all
    # connected DYNAMIXEL simultaneously.
    def getId(self):
        return self.__read1(FIELD_ID)

    def setId(self, value):
        self.__write1(FIELD_ID, value)
        self.deviceId = value


    # Baud Rate determines serial communication speed between a
    # controller and DYNAMIXEL’s.
    def getBaudRate(self):
        return self.__read1(FIELD_BAUD_RATE)

    def setBaudRate(self, value):
        self.__write1(FIELD_BAUD_RATE, value)



    # If the DYNAMIXEL receives an Instruction Packet, it will return
    # the Status Packet after the time of the set Return Delay
    # Time(5).  Note that the range of values is 0 to 254 (0XFE) and
    # its unit is 2 [μsec]. For instance, if the Return Delay Time(5)
    # is set to ‘10’, the Status Packet will be returned after
    # 20[μsec] when the Instruction Packet is received.
    def getReturnDelayTime(self):
        return self.__read1(FIELD_RETURN_DELAY_TIME);

    def setReturnDelayTime(self, value):
        self.__write1(FIELD_RETURN_DELAY_TIME, value);



    # The angle limit allows the motion to be restrained. The range
    # and the unit of the value is the same as Goal Position(30).  CW
    # Angle Limit: the minimum value of Goal Position(30) CCW Angle
    # Limit: the maximum value of Goal Position(30) The following two
    # modes can be set pursuant to the value of CW and CCW.
    #
    # Wheel Mode  both are 0
    # Joint Mode  neither are 0
    #
    # The wheel mode can be used to wheel-type operation robots since
    # motors of the robots spin infinitely. The joint mode can be used
    # to multi-joints robot since the robots can be controlled with
    # specific angles.
    def getCwAngleLimit(self):
        return self.__read2(FIELD_CW_ANGLE_LIMIT)

    def setCwAngleLimit(self, value):
        self.__write2(FIELD_CW_ANGLE_LIMIT, value)



    def getCcwAngleLimit(self):
        return self.__read2(FIELD_CCW_ANGLE_LIMIT)

    def setCcwAngleLimit(self, value):
        self.__write2(FIELD_CCW_ANGLE_LIMIT, value)



    # About 1°C 0 ~ 99
    def getTemperatureLimit(self):
        return self.__read1(FIELD_TEMPERATURE_LIMIT)

    def setTemperatureLimit(self, value):
        self.__write1(FIELD_TEMPERATURE_LIMIT, value)



    # About 0.1V        50 ~ 160        5.0 ~ 16.0V
    #
    # For example, if the value is 80, the voltage is 8V. If Present
    # Voltage(42) is out of the range, Voltage Range Error Bit (Bit0)
    # of Status Packet is returned as ‘1’ and Alarm is triggered as
    # set in the addresses 17 and 18.
    def getMinVoltageLimit(self):
        return self.__read1(FIELD_MIN_VOLTAGE_LIMIT);

    def setMinVoltageLimit(self, value):
        self.__write1(FIELD_MIN_VOLTAGE_LIMIT, value);



    def getMaxVoltageLimit(self):
        return self.__read1(FIELD_MAX_VOLTAGE_LIMIT);

    def setMaxVoltageLimit(self, value):
        self.__write1(FIELD_MAX_VOLTAGE_LIMIT, value);



    # It is the torque value of maximum output. 0 to 1,023 (0x3FF) can
    # be used, and the unit is about 0.1%.  For example, Data 1,023
    # (0x3FF) means that DYNAMIXEL will use 100% of the maximum torque
    # it can produce while Data 512 (0x200) means that DYNAMIXEL will
    # use 50% of the maximum torque.  When the power is turned on,
    # Torque Limit(34) uses the value as the initial value.
    def getMaxTorque(self):
        return self.__read2(FIELD_MAX_TORQUE);

    def setMaxTorque(self, value):
        self.__write2(FIELD_MAX_TORQUE, value);



    # The Status Return Level(68) decides how to return Status Packet
    # when DYNAMIXEL receives an Instruction Packet.
    # 0 PING Instruction        Returns the Status Packet for PING Instruction only
    # 1 PING/Read Instruction   Returns the Status Packet for PING and READ Instruction
    # 2 All Instructions        Returns the Status Packet for all Instructions
    def getStatusReturnLevel(self):
        return self.__read1(FIELD_STATUS_RETURN_LEVEL);

    def setStatusReturnLevel(self, value):
        self.__write1(FIELD_STATUS_RETURN_LEVEL, value);



    # The DYNAMIXEL can protect itself by detecting dangerous
    # situations that could occur during the operation.  Each Bit
    # is inclusively processed with the ‘OR’ logic, therefore,
    # multiple options can be generated.  For instance, when
    # ‘0x05’ (binary : 00000101) is defined in Shutdown(18),
    # DYNAMIXEL can detect both Input Voltage Error(binary :
    # 00000001) and Overheating Error(binary : 00000100).  If
    # those errors are detected, Torque Enable(24) is cleared to
    # ‘0’ and the motor output becomes 0 [%].  REBOOT is the only
    # method to reset Torque Enable(24) to ‘1’(Torque ON) after
    # the shutdown. The followings are detectable situations.
    # Bit 7     0       -
    # Bit 6     Instruction Error       Detects that undefined Instruction is transmitted or the Action command is delivered without the reg_write command
    # Bit 5     Overload Error  Detects that persistent load exceeds maximum output
    # Bit 4     CheckSum Error  Detects that the Checksum of the transmitted Instruction Packet is invalid
    # Bit 3     Range Error     Detects that the command is given beyond the range of usage
    # Bit 2     Overheating Error       Detects that the internal temperature exceeds the set temperature
    # Bit 1     Angle Limit Error       Detects that Goal Position is written with the value that is not between CW Angle Limit and CCW Angle Limit
    # Bit 0     Input Voltage Error     Detects that input voltage exceeds the configured operating voltage
    def getAlarmLed(self):
        return self.__read1(FIELD_ALARM_LED);

    def setAlarmLed(self, value):
        self.__write1(FIELD_ALARM_LED, value);



    def getShutdown(self):
        return self.__read1(FIELD_SHUTDOWN);

    def setShutdown(self, value):
        self.__write1(FIELD_SHUTDOWN, value);



    # RAM Control Area (transient)



    # 0 (Default)   Turn off the torque
    # 1             Turn on the torque and lock EEPROM area
    def getTorqueEnable(self):
        return self.__read1(FIELD_TORQUE_ENABLE)

    def setTorqueEnable(self, value):
        self.__write1(FIELD_TORQUE_ENABLE, value)



    # 0 (Default)   Turn OFF the LED
    # 1             Turn ON the LED
    def getLed(self):
        return self.__read1(FIELD_LED)

    def setLed(self, value):
        self.__write1(FIELD_LED, value)



    # It exists in each direction of CW/CCW and means the error
    # between goal position and present position. The range of the
    # value is 0~255, and the unit is the same as Goal
    # Position.(Address 30,31) The greater the value, the more
    # difference occurs.
    def getCwComplianceMargin(self):
        return self.__read1(FIELD_CW_COMPLIANCE_MARGIN);

    def setCwComplianceMargin(self, value):
        self.__write1(FIELD_CW_COMPLIANCE_MARGIN, value);



    def getCcwComplianceMargin(self):
        return self.__read1(FIELD_CCW_COMPLIANCE_MARGIN);

    def setCcwComplianceMargin(self, value):
        self.__write1(FIELD_CCW_COMPLIANCE_MARGIN, value);



    # It exists in each direction of CW/CCW and sets the level of
    # Torque near the goal position. Compliance Slope is set in 7
    # steps, the higher the value, the more flexibility is
    # obtained. Data representative value is actually used value. That
    # is, even if the value is set to 25, 16 is used internally as the
    # representative value.
    # 1 0(0x00) ~ 3(0x03)       2(0x02)
    # 2 4(0x04) ~ 7(0x07)       4(0x04)
    # 3 8(0x08)~15(0x0F)        8(0x08)
    # 4 16(0x10)~31(0x1F)       16(0x10)
    # 5 32(0x20)~63(0x3F)       32(0x20)
    # 6 64(0x40)~127(0x7F)      64(0x40)
    # 7 128(0x80)~254(0xFE)     128(0x80)
    def getCwComplianceSlope(self):
        return self.__read1(FIELD_CW_COMPLIANCE_SLOPE);

    def setCwComplianceSlope(self, value):
        self.__write1(FIELD_CW_COMPLIANCE_SLOPE, value);



    def getCcwComplianceSlope(self):
        return self.__read1(FIELD_CCW_COMPLIANCE_SLOPE);

    def setCcwComplianceSlope(self, value):
        self.__write1(FIELD_CCW_COMPLIANCE_SLOPE, value);



    # It is a position value of destination. 0 ~ 1,023 (0x3FF) is
    # available. The unit is 0.29°. If Goal Position is out of the
    # range, Angle Limit Error Bit (Bit 1) of Status Packet is
    # returned as ‘1’ and Alarm is triggered as set in Alarm
    # LED/Shutdown.
    def getGoalPosition(self):
        return self.__read2(FIELD_GOAL_POSITION)

    def setGoalPosition(self, value):
        self.__write2(FIELD_GOAL_POSITION, value)
        while True:
            currentPosition = self.getPresentPosition()
            print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (self.deviceId, value, currentPosition))
            if abs(value - currentPosition) < 20:
                break



    # It is a moving speed to Goal Position.  The range and the unit
    # of the value may vary depending on the operation mode.
    #
    # Joint Mode
    # 0 ~ 1,023(0x3FF) can be used, and the unit is about 0.111rpm.
    # If it is set to 0, it means the maximum rpm of the motor is used
    # without controlling the speed.
    # If it is 1023, it is about 114rpm.  For example, if it is set to
    # 300, it is about 33.3 rpm.
    #
    # Wheel Mode
    # 0 ~ 2,047(0x7FF) can be used, the unit is about 0.1%.
    # If a value in the range of 0 ~ 1,023 is used, it is stopped by
    # setting to 0 while rotating to CCW direction.
    # If a value in the range of 1,024 ~ 2,047 is used, it is stopped
    # by setting to 1,024 while rotating to CW direction.  That is,
    # the 10th bit becomes the direction bit to control the direction.
    # In Wheel Mode, only the output control is possible, not speed.
    # For example, if it is set to 512, it means the output is
    # controlled by 50% of the maximum output.

    def getMovingSpeed(self):
        return self.__read2(FIELD_MOVING_SPEED)

    def setMovingSpeed(self, value):
        self.__write2(FIELD_MOVING_SPEED, value)



    # It is the value of the maximum torque limit. 0 ~ 1,023(0x3FF) is
    # available, and the unit is about 0.1%. For example, if the value
    # is 512, it is about 50%; that means only 50% of the maximum
    # torque will be used. If the power is turned on, the value of Max
    # Torque(14) is used as the initial value.
    def getTorqueLimit(self):
        return self.__read2(FIELD_TORQUE_LIMIT)

    def setTorqueLimit(self, value):
        self.__write2(FIELD_TORQUE_LIMIT, value)



    # It is the present position value of DYNAMIXEL.
    # The range of the value is 0~1023 (0x3FF), and the unit is 0.29 [°].
    def getPresentPosition(self):
        return self.__read2(FIELD_PRESENT_POSITION)



    # It is the present moving speed. 0~2,047 (0x7FF) can be used. If
    # a value is in the rage of 0~1,023, it means that the motor
    # rotates to the CCW direction. If a value is in the rage of
    # 1,024~2,047, it means that the motor rotates to the CW
    # direction. That is, the 10th bit becomes the direction bit to
    # control the direction, and 0 and 1,024 are equal. The unit of
    # this value varies depending on operation mode.
    #
    # Joint Mode
    # The unit is about 0.111rpm. For example, if it is set to 300, it
    # means that the motor is moving to the CCW direction at a rate of
    # about 33.3rpm.
    #
    # Wheel Mode
    #
    # The unit is about 0.1%. For example, if it is set to 512, it
    # means that the torque is controlled by 50% of the maximum torque
    # to the CCW direction.
    def getPresentSpeed(self):
        return self.__read2(FIELD_PRESENT_SPEED);



    # It means currently applied load. The range of the value is
    # 0~2047, and the unit is about 0.1%. If the value is 0~1,023, it
    # means the load works to the CCW direction. If the value is
    # 1,024~2,047, it means the load works to the CW direction. That
    # is, the 10th bit becomes the direction bit to control the
    # direction, and 1,024 is equal to 0. For example, the value is
    # 512, it means the load is detected in the direction of CCW about
    # 50% of the maximum torque.
    def getPresentLoad(self):
        return self.__read2(FIELD_PRESENT_LOAD);



    # It is the size of the present voltage supplied. This value is 10
    # times larger than the actual voltage. For example, when 10V is
    # supplied, the data value is 100 (0x64) If Present Voltage(42)
    # value is out of range, Voltage Range Error Bit (Bit0) of Status
    # Packet is returned as ‘1’ and Alarm is triggered and set the
    # address 17 and set 1 to the Bit 0 of the address 18.
    def getPresentVoltage(self):
        return self.__read1(FIELD_PRESENT_VOLTAGE);



    # It is the internal temperature of DYNAMIXEL in Celsius.  Data
    # value is identical to the actual temperature in Celsius. For
    # example, if the data value is 85 (0x55), the current internal
    # temperature is 85°C.
    def getPresentTemperature(self):
        return self.__read1(FIELD_PRESENT_TEMPERATURE);



    # 0 No instruction registered by REG_WRITE.
    # 1 Instruction registered by REG_WRITE exsists.
    def getRegisteredInstruction(self):
        return self.__read1(FIELD_REGISTERED_INSTRUCTION);



    # 0 Goal position command execution is completed
    # 1 Goal position command execution is in progress
    def getMoving(self):
        return self.__read1(FIELD_MOVING);



    # 0 EEPROM area can be modified
    # 1 EEPROM area cannot be modified
    def getLock(self):
        return self.__read1(FIELD_LOCK);

    def setLock(self, value):
        self.__write1(FIELD_LOCK, value);



    # Minimum current to drive motor. This value ranges from 0x20 to
    # 0x3FF.
    def getPunch(self):
        return self.__read2(FIELD_PUNCH);

    def setPunch(self, value):
        self.__write2(FIELD_PUNCH, value);



    # Private functions



    def __read1(self, field):
        self.tty.openPort()
        self.tty.setBaudRate(1000000)
        response, result, error = self.protocol.read1ByteTxRx(self.tty, self.deviceId, field)
        self.__verifyResponse(result, error, "read1ByteTxRx (tty: " + self.ttyName + " id=" + str(self.deviceId) + " field=" + self.__fieldToString(field) + ")")
        self.tty.closePort()
        return response

    def __read2(self, field):
        self.tty.openPort()
        self.tty.setBaudRate(1000000)
        response, result, error = self.protocol.read2ByteTxRx(self.tty, self.deviceId, field)
        self.__verifyResponse(result, error, "read2ByteTxRx (tty: " + self.ttyName + " id=" + str(self.deviceId) + " field=" + self.__fieldToString(field) + ")")
        self.tty.closePort()
        return response

    def __write1(self, field, value):
        self.tty.openPort()
        self.tty.setBaudRate(1000000)
        result, error = self.protocol.write1ByteTxRx(self.tty, self.deviceId, field, value)
        self.__verifyResponse(result, error, "write1ByteTxRx (tty: " + self.ttyName + " id=" + str(self.deviceId) + " field=" + self.__fieldToString(field) + " value=" + str(value) + ")")
        self.tty.closePort()

    def __write2(self, field, value):
        self.tty.openPort()
        self.tty.setBaudRate(1000000)
        result, error = self.protocol.write2ByteTxRx(self.tty, self.deviceId, field, value)
        self.__verifyResponse(result, error, "write2ByteTxRx (tty: " + self.ttyName + " id=" + str(self.deviceId) + " field=" + self.__fieldToString(field) + " value=" + str(value) + ")")
        self.tty.closePort()

    def __verifyResponse(self, result, error, s):
        if result != sdk.COMM_SUCCESS:
            raise Exception("%s %s" % (s, self.protocol.getTxRxResult(result)))
        elif error != 0:
            raise Exception("%s %s" % (s, self.protocol.getRxPacketError(error)))

    def __fieldToString(self, field):
        if field == FIELD_MODEL_NUMBER:
            return "MODEL_NUMBER"
        if field == FIELD_FIRMWARE_VERSION:
            return "FIRMWARE_VERSION"
        if field == FIELD_ID:
            return "ID"
        if field == FIELD_BAUD_RATE:
            return "BAUD_RATE"
        if field == FIELD_RETURN_DELAY_TIME:
            return "RETURN_DELAY_TIME"
        if field == FIELD_CW_ANGLE_LIMIT:
            return "CW_ANGLE_LIMIT"
        if field == FIELD_CCW_ANGLE_LIMIT:
            return "CCW_ANGLE_LIMIT"
        if field == FIELD_TEMPERATURE_LIMIT:
            return "TEMPERATURE_LIMIT"
        if field == FIELD_MIN_VOLTAGE_LIMIT:
            return "MIN_VOLTAGE_LIMIT"
        if field == FIELD_MAX_VOLTAGE_LIMIT:
            return "MAX_VOLTAGE_LIMIT"
        if field == FIELD_MAX_TORQUE:
            return "MAX_TORQUE"
        if field == FIELD_STATUS_RETURN_LEVEL:
            return "STATUS_RETURN_LEVEL"
        if field == FIELD_ALARM_LED:
            return "ALARM_LED"
        if field == FIELD_SHUTDOWN:
            return "SHUTDOWN"
        if field == FIELD_TORQUE_ENABLE:
            return "TORQUE_ENABLE"
        if field == FIELD_LED:
            return "LED"
        if field == FIELD_CW_COMPLIANCE_MARGIN:
            return "CW_COMPLIANCE_MARGIN"
        if field == FIELD_CCW_COMPLIANCE_MARGIN:
            return "CCW_COMPLIANCE_MARGIN"
        if field == FIELD_CW_COMPLIANCE_SLOPE:
            return "CW_COMPLIANCE_SLOPE"
        if field == FIELD_CCW_COMPLIANCE_SLOPE:
            return "CCW_COMPLIANCE_SLOPE"
        if field == FIELD_GOAL_POSITION:
            return "GOAL_POSITION"
        if field == FIELD_MOVING_SPEED:
            return "MOVING_SPEED"
        if field == FIELD_TORQUE_LIMIT:
            return "TORQUE_LIMIT"
        if field == FIELD_PRESENT_POSITION:
            return "PRESENT_POSITION"
        if field == FIELD_PRESENT_SPEED:
            return "PRESENT_SPEED"
        if field == FIELD_PRESENT_LOAD:
            return "PRESENT_LOAD"
        if field == FIELD_PRESENT_VOLTAGE:
            return "PRESENT_VOLTAGE"
        if field == FIELD_PRESENT_TEMPERATURE:
            return "PRESENT_TEMPERATURE"
        if field == FIELD_REGISTERED_INSTRUCTION:
            return "REGISTERED_INSTRUCTION"
        if field == FIELD_MOVING:
            return "MOVING"
        if field == FIELD_LOCK:
            return "LOCK"
        if field == FIELD_PUNCH:
            return "PUNCH"
