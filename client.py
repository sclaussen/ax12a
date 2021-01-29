from AX12A import *
ax12a = AX12A('/dev/tty.usbserial-FT3WFGSI', 1)
print("getModelNumber(): " + str(ax12a.getModelNumber()))
print("getFirmwareVersion(): " + str(ax12a.getFirmwareVersion()))
print("getId(): " + str(ax12a.getId()))
print("getBaudRate(): " + str(ax12a.getBaudRate()))
print("getReturnDelayTime(): " + str(ax12a.getReturnDelayTime()))
print("getCwAngleLimit(): " + str(ax12a.getCwAngleLimit()))
print("getCcwAngleLimit(): " + str(ax12a.getCcwAngleLimit()))
print("getTemperatureLimit(): " + str(ax12a.getTemperatureLimit()))
print("getMinVoltageLimit(): " + str(ax12a.getMinVoltageLimit()))
print("getMaxVoltageLimit(): " + str(ax12a.getMaxVoltageLimit()))
print("getMaxTorque(): " + str(ax12a.getMaxTorque()))
print("getStatusReturnLevel(): " + str(ax12a.getStatusReturnLevel()))
print("getAlarmLed(): " + str(ax12a.getAlarmLed()))
print("getShutdown(): " + str(ax12a.getShutdown()))
print("getTorqueEnable(): " + str(ax12a.getTorqueEnable()))
print("getLed(): " + str(ax12a.getLed()))
print("getCwComplianceMargin(): " + str(ax12a.getCwComplianceMargin()))
print("getCcwComplianceMargin(): " + str(ax12a.getCcwComplianceMargin()))
print("getCwComplianceSlope(): " + str(ax12a.getCwComplianceSlope()))
print("getCcwComplianceSlope(): " + str(ax12a.getCcwComplianceSlope()))
print("getGoalPosition(): " + str(ax12a.getGoalPosition()))
print("getMovingSpeed(): " + str(ax12a.getMovingSpeed()))
print("getTorqueLimit(): " + str(ax12a.getTorqueLimit()))
print("getPresentPosition(): " + str(ax12a.getPresentPosition()))
print("getPresentSpeed(): " + str(ax12a.getPresentSpeed()))
print("getPresentLoad(): " + str(ax12a.getPresentLoad()))
print("getPresentVoltage(): " + str(ax12a.getPresentVoltage()))
print("getPresentTemperature(): " + str(ax12a.getPresentTemperature()))
print("getRegisteredInstruction(): " + str(ax12a.getRegisteredInstruction()))
print("getMoving(): " + str(ax12a.getMoving()))
print("getLock(): " + str(ax12a.getLock()))
print("getPunch(): " + str(ax12a.getPunch()))
