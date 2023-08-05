import RPi.GPIO as GPIO
import datetime
import json
from pirc522 import RFID as PIRC522
from pelops.mythreading import LoggerThread
from copreus.baseclasses.adriver import ADriver
from copreus.baseclasses.apolling import APolling
from copreus.schema.rfid import get_schema


class RFID(ADriver, APolling):
    """Driver for the RFID_RC522 sensor with spi connectivity. /rfid/state is a json structure e.g.
    {"uid": "116:4:126:1", "present": "TRUE", "trigger":"POLLING|EVENT", "timestamp": "2009-11-10T23:00:00.0Z"}

    The driver entry in the yaml file consists of:
      * ADriver entries
      * APolling entries

    Example:
    driver:
        type: rfid
        pins:
            pin_rst: 25
            pin_irq: 13
            pin_cs: 17  # optional - only necessary if spi-bus 1 or 2
        spi:
            bus: 0
            device: 1
            maxspeed: 1000000
        topics-pub:
            uid: /rfid/uid
            present: /rfid/preset
            state: /rfid/state
        topics-sub:
            poll-now: /rfid/pollnow
        mqtt-translations:
            present-true: TRUE
            present-false: FALSE
            poll-now: True
        poll-interval: 5
        use-irq: TRUE  # register event handling to pin_irq
        pub-pattern: ONREAD  # ONREAD (everytime the sensor has been read), ONCHANGE (only if a new value for any field has been detected)
    """

    _rfid = None

    _pin_rst = None
    _pin_irq = None
    _pin_cs = None
    _spi_bus = None
    _spi_device = None
    _spi_speed = None

    _pub_on_change = None

    _register_event = None
    _event_thread = None
    _stop_event_handler = None
    _stop_irq = None

    _last_state = None

    def __init__(self, config, mqtt_client=None, logger=None, stdout_log_level=None, no_gui=None,
                 manage_monitoring_agent=True):
        ADriver.__init__(self, config, mqtt_client, logger, logger_name=self.__class__.__name__,
                         stdout_log_level=stdout_log_level, no_gui=no_gui,
                         manage_monitoring_agent=manage_monitoring_agent)
        APolling.__init__(self, self._config, self._mqtt_client, self._logger)

        self._pin_rst = self._config["pins"]["pin_rst"]
        self._pin_irq = self._config["pins"]["pin_irq"]
        try:
            self._pin_cs = self._config["pins"]["pin_cs"]
        except KeyError:
            self._pin_cs = 0

        self._spi_bus = self._config["spi"]["bus"]
        self._spi_device = self._config["spi"]["device"]
        self._spi_speed = self._config["spi"]["maxspeed"]

        self._pub_on_change = False
        if self._config["pub-pattern"] == "ONCHANGE":
            self._pub_on_change = True

        GPIO.setmode(GPIO.BCM)
        self._rfid = PIRC522(bus=self._spi_bus, device=self._spi_device, speed=self._spi_speed, pin_rst=self._pin_rst,
                             pin_ce=self._pin_cs, pin_irq=self._pin_irq, pin_mode=GPIO.BCM)

        self._register_event = False
        if self._config["use-irq"]:
            self._register_event = True
            self._stop_irq = self._rfid.irq
            self._stop_event_handler = False
            self._event_thread = LoggerThread(target=self._event_handler, name="rfid-event-handler", logger=self._logger)

        if ((self._poll_interval == 0 and not self._register_event) or
            (self._poll_interval > 0 and self._register_event)):
           raise ValueError("poll_interval and register_event are mutually exclusive - use either polling or irq.")

        self._last_state = self._get_state_template()
        self._last_state["uid"] = "-1"

    def _get_state_template(self):
        return {
            "uid": "",
            "present": self._mqtt_translations["present-false"].decode('UTF-8'),
            "trigger": None,
            "timestamp": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        }

    def _read_rfid(self, trigger):
        self._logger.info("RFID._read_rfid - start")
        result = self._get_state_template()
        (error, data) = self._rfid.request()
        if not (error or data is None):
            self._logger.info("RFID._read_rfid.request success. data: {}".format(data))

            (error, uid) = self._rfid.anticoll()
            if not (error or uid is None):
                self._logger.info("RFID._read_rfid.anticoll success.uid: {}".format(uid))
                result["present"] = self._mqtt_translations["present-true"].decode('UTF-8')
                result["uid"] = "{}:{}:{}:{}".format(uid[0],uid[1],uid[2],uid[3])
        result["trigger"] = trigger
        if self._publish_now(result):
            self._publish(result)
        self._logger.info("RFID._read_rfid - stopped")

    def _publish_now(self, state):
        if not self._pub_on_change:
            return True
        if state["uid"] == self._last_state["uid"] and state["present"] == self._last_state["present"]:
            self._logger.debug("RFID._publish_now - skip pub. no change detected.")
            return False
        return True

    def _publish(self, state):
        self._logger.info("RFID._publish state:{}".format(state))
        self._publish_value(self._topics_pub["state"], json.dumps(state))
        self._publish_value(self._topics_pub["uid"], state["uid"])
        self._publish_value(self._topics_pub["present"], state["present"])
        self._last_state = state

    def _poll_device(self):
        """APolling._poll_device"""
        self._logger.info("RFID._poll_device -> read rfid")
        self._rfid.init()
        self._read_rfid("POLLING")

    def _event_handler(self):
        self._logger.info("RFID._event_handler - start")
        while not self._stop_event_handler:
            self._rfid.wait_for_tag()
            if not self._stop_event_handler:
                self._logger.info("RFID._event_handler -> read rfid")
                self._read_rfid("EVENT")
        self._logger.info("RFID._event_handler - stopped")

    def _driver_start(self):
        """ADriver._driver_start"""
        self._start_polling()
        if self._register_event:
            self._stop_event_handler = False
            self._event_thread.start()

    def _driver_stop(self):
        """ADriver._driver_stop"""
        if self._register_event:
            self._stop_event_handler = True
            self._stop_irq.set()
            self._event_thread.join()
        self._stop_polling()
        self._rfid.cleanup()

    @classmethod
    def _get_schema(cls):
        return get_schema()

    def _runtime_information(self):
        return {}

    def _config_information(self):
        return {}
