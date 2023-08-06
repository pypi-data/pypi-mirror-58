# __main__.py

from .sht20 import SHT20
from importlib import resources
from time import sleep

def main():
    sht = SHT20()

    sht.sht20_init(sht.TEMP_RES_14bit)

    temp = sht.read_temp()
    humid = sht.read_humid()

#   or

    data = sht.read_all()
    temp = data[0]
    humid = data[1]

    print("Temperature (Celcius): " + str(temp))
    print("Humidity (%RH): " + str(humid))

if __name__ == "__main__":
    main()
