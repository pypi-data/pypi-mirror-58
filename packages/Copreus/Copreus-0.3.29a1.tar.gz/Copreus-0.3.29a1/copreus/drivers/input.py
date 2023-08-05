import RPi.GPIO as GPIO
from copreus.baseclasses.adriver import ADriver
from copreus.baseclasses.aevents import AEvents
from copreus.schema.input import get_schema


class Input(ADriver, AEvents):
    """Generic driver that waits for events on the given input pin.

    The driver entry in the yaml file consists of:
      * ADriver entries
        * topics_pub:
          * button_pressed - mqtt-translations.button_pressed
          * button_state - mqtt-translations.button_state-open and mqtt-translations.button_state-closed
      * Input entries
        * pin: gpio pin

    Example:
    driver:
        type: input
        pin:  21
        topics-pub:
            button_pressed: /test/button/pressed
            button_state:   /test/button/state
        mqtt-translations:
            button_pressed: PRESSED
            button_state-open: OPEN
            button_state-closed: CLOSED

    """

    _pin = -1  # gpio pin id

    def __init__(self, config, mqtt_client=None, logger=None, stdout_log_level=None, no_gui=None,
                 manage_monitoring_agent=True):
        ADriver.__init__(self, config, mqtt_client, logger, logger_name=self.__class__.__name__,
                         stdout_log_level=stdout_log_level, no_gui=no_gui,
                         manage_monitoring_agent=manage_monitoring_agent)
        AEvents.__init__(self, self._config, self._logger)

        self._pin = self._config["pin"]
        self._add_event(self._pin, self._callback_pin)
        self._ui_commands["gpio_state"] = self._cmd_gpio_state

    def _cmd_gpio_state(self, args):
        """gpio_state - displays if the gpio is closed or open: GPIO_STATE"""
        state = GPIO.input(self._pin)
        if not state:
            print("[{}] gpio {} is closed".format(self._name, self._pin))
        else:
            print("[{}] gpio {} is open".format(self._name, self._pin))

    def _callback_pin(self, channel):
        """Event handler for gpio pin 'pin'. Publishes to the topics 'button_state' and 'button_pressed'."""
        state = GPIO.input(self._pin)
        self._logger.info("Input._callback_pin - received event. pin state: {}.".format(state))
        if not state:
            self._publish_value(self._topics_pub["button_pressed"], self._mqtt_translations["button_pressed"])
            self._publish_value(self._topics_pub["button_state"], self._mqtt_translations["button_state-closed"])
        else:
            self._publish_value(self._topics_pub["button_state"], self._mqtt_translations["button_state-open"])

    def _driver_start(self):
        """ADriver._driver_start"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self._register_events()

    def _driver_stop(self):
        """ADriver._driver_stop"""
        self._unregister_events()
        GPIO.cleanup(self._pin)

    @classmethod
    def _get_schema(cls):
        return get_schema()

    def _runtime_information(self):
        return {}

    def _config_information(self):
        return {}


def standalone():
    """Calls the static method Input.standalone()."""
    Input.standalone()


if __name__ == "__main__":
    Input.standalone()
