from sensor.exception import SensorException
import sys
import sensor.logger


try:
    print(2/0)
except Exception as e:
    print(SensorException(e, sys))