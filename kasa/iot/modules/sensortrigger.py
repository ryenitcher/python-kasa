"""Implementation of the Smart Control module found in some dimmers."""

from __future__ import annotations

import logging
from enum import Enum

from ...exceptions import KasaException
from ...feature import Feature
from ..iotmodule import IotModule

_LOGGER = logging.getLogger(__name__)


class SensorTrigger(IotModule):
    """Implements the sensor trigger (Smart Control) module."""

    def _initialize_features(self) -> None:
        """Initialize features after the initial update."""
        # Only add features if the device supports the module
        if "get_default_manual_action" not in self.data:
            return

        self._add_feature(
            Feature(
                device=self._device,
                container=self,
                id="trigger_hysteresis_off",
                name="Off Hysteresis",
                icon="mdi:motion-sensor",
                attribute_getter="hysteresis_off",
                attribute_setter=None,
                type=Feature.Type.Switch,
                category=Feature.Category.Config,
            )
        )

        self._add_feature(
            Feature(
                device=self._device,
                container=self,
                id="trigger_hysteresis_on",
                name="On Hysteresis",
                icon="mdi:motion-sensor",
                attribute_getter="hysteresis_on",
                attribute_setter=None,
                type=Feature.Type.Switch,
                category=Feature.Category.Config,
            )
        )

    def query(self) -> dict:
        """Request PIR configuration."""
        return self.query_for_command("get_default_manual_action")

    @property
    def config(self) -> dict:
        """Return current configuration."""
        return self.data["get_default_manual_action"]
    
    @property
    def hysteresis_off(self) -> dict[str, int]:
        return {
            'offToT': self.offToT,
            'offToS': self.offToS,
            'offToM': self.offToM,
        }

    @property
    def offToT(self) -> int:
        """Return the hysteresis period following a time(?) activation."""
        return int(self.config["offToT"])

    async def set_offToT(self, offset: int) -> dict:
        """Set the hysteresis period, in seconds, following a time(?) activation."""
        return await self.call("set_default_manual_action", {"offToT": int(offset)})

    @property
    def offToM(self) -> int:
        """Return the hysteresis period following a motion(?) activation."""
        return int(self.config["offToM"])

    async def set_offToM(self, offset: int) -> dict:
        """Set the hysteresis period, in seconds, following a motion(?) activation."""
        return await self.call("set_default_manual_action", {"offToM": int(offset)})

    @property
    def offToS(self) -> int:
        """Return the hysteresis period following a switch (manual) activation."""
        return int(self.config["offToS"])

    async def set_offToS(self, offset: int) -> dict:
        """Set the hysteresis period, in seconds, following a switch (manual) activation."""
        return await self.call("set_default_manual_action", {"offToM": int(offset)})
    
    @property
    def hysteresis_on(self) -> dict[str, int]:
        return {
            'onToT': self.onToT,
            'onToS': self.onToS,
            'onToM': self.onToM,
        }

    @property
    def onToT(self) -> int:
        """Return the hysteresis period following a time(?) deactivation."""
        return int(self.config["onToT"])

    async def set_onToT(self, offset: int) -> dict:
        """Set the hysteresis period, in seconds, following a time(?) deactivation."""
        return await self.call("set_default_manual_action", {"onToT": int(offset)})

    @property
    def onToM(self) -> int:
        """Return the hysteresis period following a motion(?) deactivation."""
        return int(self.config["onToM"])

    async def set_onToM(self, offset: int) -> dict:
        """Set the hysteresis period, in seconds, following a motion(?) deactivation."""
        return await self.call("set_default_manual_action", {"onToM": int(offset)})

    @property
    def onToS(self) -> int:
        """Return the hysteresis period following a switch (manual) deactivation."""
        return int(self.config["onToS"])

    async def set_onToS(self, offset: int) -> dict:
        """Set the hysteresis period, in seconds, following a switch (manual) deactivation."""
        return await self.call("set_default_manual_action", {"onToM": int(offset)})


