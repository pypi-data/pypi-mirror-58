"""Support for Dynalite channels as lights."""

from .dynalitebase import DynaliteChannelBaseDevice
from .const import ATTR_BRIGHTNESS


class DynaliteChannelLightDevice(DynaliteChannelBaseDevice):
    """Representation of a Dynalite Channel as a Home Assistant Light."""

    def __init__(
        self, area, area_name, channel, name, type, master_area, bridge, device
    ):
        """Initialize the light."""
        self._level = 0
        super().__init__(
            area, area_name, channel, name, type, master_area, bridge, device
        )

    @property
    def category(self):
        """Return the category of the entity: light, switch, or cover."""
        return "light"

    @property
    def brightness(self):
        """Return the brightness of this light between 0..255."""
        return self._level * 255

    @property
    def is_on(self):
        """Return true if device is on."""
        return self._level > 0

    def update_level(self, actual_level, target_level):
        """Update the current level."""
        self._level = actual_level

    async def async_turn_on(self, **kwargs):
        """Turn light on."""
        if ATTR_BRIGHTNESS in kwargs:
            brightness = kwargs[ATTR_BRIGHTNESS] / 255.0
            self._device.turnOn(brightness=brightness)
        else:
            self._device.turnOn()

    async def async_turn_off(self, **kwargs):
        """Turn light off."""
        self._device.turnOff()
