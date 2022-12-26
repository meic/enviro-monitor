import board
import adafruit_dht


class DHT22:
    def __init__(self, pin=board.D4, use_pulseio=False):
        # you can pass DHT22 use_pulseio=False if you wouldn't like to use
        # pulseio.
        # This may be necessary on a Linux single board computer like the
        #  Raspberry Pi, but it will not work in CircuitPython.
        self.dht_device = adafruit_dht.DHT22(pin, use_pulseio=use_pulseio)

    def get_reading(self):
        try:
            return self.dht_device.temperature, self.dht_device.humidity
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep
            # going
            print(error.args[0])
            return None, None


if __name__ == "__main__":
    dht22 = DHT22()
    print(dht22.get_reading())
