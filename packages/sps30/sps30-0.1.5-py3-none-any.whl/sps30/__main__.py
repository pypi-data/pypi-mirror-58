# __main__.py

from .sps30 import SPS30
from importlib import resources
from time import sleep
import sys

def main():
    sps = SPS30()

    sps.device_reset()
    sleep(1)

    if sps.read_article_code() == sps.ARTICLE_CODE_ERROR:
        raise Exception("ARTICLE CODE CRC ERROR!")
    else:
        print("ARTICLE CODE: " + str(sps.read_article_code()))

    if sps.read_device_serial() == sps.SERIAL_NUMBER_ERROR:
        raise Exception("SERIAL NUMBER CRC ERROR!")
    else:
        print("DEVICE SERIAL: " + str(sps.read_device_serial()))

    sps.start_measurement()

    while not sps.read_data_ready_flag():
#        print("New Measurement is not available!")
        sleep(0.1)
        if sps.read_data_ready_flag() == sps.DATA_READY_FLAG_ERROR:
            raise Exception("DATA-READY FLAG CRC ERROR!")

    if sps.read_measured_values() == sps.MEASURED_VALUES_ERROR:
        raise Exception("MEASURED VALUES CRC ERROR!")
    else:
        print ("PM1.0 Value in µg/m3: " + str(sps.dict_values['pm1p0']))
        print ("PM2.5 Value in µg/m3: " + str(sps.dict_values['pm2p5']))
        print ("PM4.0 Value in µg/m3: " + str(sps.dict_values['pm4p0']))
        print ("PM10.0 Value in µg/m3: " + str(sps.dict_values['pm10p0']))
        print ("NC0.5 Value in 1/cm3: " + str(sps.dict_values['nc0p5']))    # NC: Number of Concentration
        print ("NC1.0 Value in 1/cm3: " + str(sps.dict_values['nc1p0']))
        print ("NC2.5 Value in 1/cm3: " + str(sps.dict_values['nc2p5']))
        print ("NC4.0 Value in 1/cm3: " + str(sps.dict_values['nc4p0']))
        print ("NC10.0 Value in 1/cm3: " + str(sps.dict_values['nc10p0']))
        print ("Typical Particle Size in µm: " + str(sps.dict_values['typical']))

    sps.stop_measurement()


if __name__ == "__main__":
    main()
