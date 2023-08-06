import logging
import struct
import time
from datetime import datetime

from bluepy import btle

from .decorators import with_connect

_LOGGER = logging.getLogger(__name__)

UUID_UNITS = 'EBE0CCBE-7A0A-4B0C-8A1A-6FF2997DA3A6'     # 0x00 - F, 0x01 - C    READ WRITE
UUID_HISTORY = 'EBE0CCBC-7A0A-4B0C-8A1A-6FF2997DA3A6'   # Last idx 152          READ NOTIFY
UUID_TIME = 'EBE0CCB7-7A0A-4B0C-8A1A-6FF2997DA3A6'      # 5 bytes               READ WRITE
UUID_DATA = 'EBE0CCC1-7A0A-4B0C-8A1A-6FF2997DA3A6'      # 3 bytes               READ NOTIFY
UUID_BATTERY = 'EBE0CCC4-7A0A-4B0C-8A1A-6FF2997DA3A6'   # 1 byte                READ


class Lywsd02Client:
    UNITS = {
        b'\x01': 'F',
        b'\xff': 'C',
    }
    UNITS_CODES = {
        'C': b'\xff',
        'F': b'\x01',
    }

    def __init__(self, mac, notification_timeout=5.0, data_request_timeout=15.0):
        self._mac = mac
        self._peripheral = btle.Peripheral()
        self._notification_timeout = notification_timeout
        self._request_timeout = data_request_timeout
        self._temperature = None
        self._humidity = None
        self._last_request = None

    @staticmethod
    def parse_humidity(value):
        return int(value)

    @property
    def temperature(self):
        self._get_sensor_data()
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = struct.unpack('h', value)[0] / 100

    @property
    def humidity(self):
        self._get_sensor_data()
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value

    @property
    @with_connect
    def units(self):
        ch = self._peripheral.getCharacteristics(uuid=UUID_UNITS)[0]
        value = ch.read()
        return self.UNITS[value]

    @units.setter
    @with_connect
    def units(self, value):
        if value.upper() not in self.UNITS_CODES.keys():
            raise ValueError('Units value must be one of %s' % self.UNITS_CODES.keys())

        ch = self._peripheral.getCharacteristics(uuid=UUID_UNITS)[0]
        ch.write(self.UNITS_CODES[value.upper()], withResponse=True)

    @property
    @with_connect
    def battery(self):
        ch = self._peripheral.getCharacteristics(uuid=UUID_BATTERY)[0]
        value = ch.read()
        return ord(value)

    @property
    @with_connect
    def time(self):
        ch = self._peripheral.getCharacteristics(uuid=UUID_TIME)[0]
        value = ch.read()
        ts = struct.unpack('I', value[:4])[0]
        tz_offset = value[4]
        return datetime.fromtimestamp(ts), tz_offset

    @time.setter
    @with_connect
    def time(self, dt: datetime):
        tz_offset = time.localtime().tm_hour - time.gmtime().tm_hour

        data = struct.pack('Ib', int(dt.timestamp()), tz_offset)
        ch = self._peripheral.getCharacteristics(uuid=UUID_TIME)[0]
        ch.write(data, withResponse=True)

    @with_connect
    def _get_sensor_data(self):
        now = datetime.now().timestamp()
        if self._last_request and now - self._last_request < self._request_timeout:
            return

        self._subscribe(UUID_DATA)

        while True:
            if self._peripheral.waitForNotifications(self._notification_timeout):
                break

    @with_connect
    def get_history_data(self):
        data_received = False
        self._subscribe(UUID_HISTORY)

        while True:
            if self._peripheral.waitForNotifications(self._notification_timeout):
                data_received = True
                continue
            if data_received:
                break

    def handleNotification(self, handle, data):
        if handle == 0x3c:
            self._process_sensor_data(data)
        if handle == 0x37:
            self._process_history_data(data)
        if handle == 0x4b:
            self._process_sensor_data(data)

    def _subscribe(self, uuid):
        self._peripheral.setDelegate(self)
        ch = self._peripheral.getCharacteristics(uuid=uuid)[0]
        desc = ch.getDescriptors(forUUID=0x2902)[0]

        desc.write(0x01.to_bytes(2, byteorder="little"), withResponse=True)

    def _process_sensor_data(self, data):
        temp_bytes = data[:2]
        humid_bytes = data[2]

        self.temperature = temp_bytes
        self.humidity = humid_bytes

        self._last_request = datetime.now().timestamp()

    def _process_history_data(self, data):
        # TODO: Process history data
        print(data)
