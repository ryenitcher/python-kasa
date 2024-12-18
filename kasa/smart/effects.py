"""Module for light strip light effects."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import cast

from ..interfaces.lighteffect import LightEffect as LightEffectInterface


class SmartLightEffect(LightEffectInterface, ABC):
    """Abstract interface for smart light effects.

    This interface extends lighteffect interface to add brightness controls.
    """

    @abstractmethod
    async def set_brightness(
        self, brightness: int, *, transition: int | None = None
    ) -> dict:
        """Set effect brightness."""

    @property
    @abstractmethod
    def brightness(self) -> int:
        """Return effect brightness."""

    @property
    @abstractmethod
    def is_active(self) -> bool:
        """Return True if effect is active."""


EFFECT_AURORA = {
    "custom": 0,
    "id": "TapoStrip_1MClvV18i15Jq3bvJVf0eP",
    "brightness": 100,
    "name": "Aurora",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [
        [120, 100, 100],
        [240, 100, 100],
        [260, 100, 100],
        [280, 100, 100],
    ],
    "type": "sequence",
    "duration": 0,
    "transition": 1500,
    "direction": 4,
    "spread": 7,
    "repeat_times": 0,
    "sequence": [[120, 100, 100], [240, 100, 100], [260, 100, 100], [280, 100, 100]],
}
EFFECT_BUBBLING_CAULDRON = {
    "custom": 0,
    "id": "TapoStrip_6DlumDwO2NdfHppy50vJtu",
    "brightness": 100,
    "name": "Bubbling Cauldron",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [[100, 100, 100], [270, 100, 100]],
    "type": "random",
    "hue_range": [100, 270],
    "saturation_range": [80, 100],
    "brightness_range": [50, 100],
    "duration": 0,
    "transition": 200,
    "init_states": [[270, 100, 100]],
    "fadeoff": 1000,
    "random_seed": 24,
    "backgrounds": [[270, 40, 50]],
}
EFFECT_CANDY_CANE = {
    "custom": 0,
    "id": "TapoStrip_6Dy0Nc45vlhFPEzG021Pe9",
    "brightness": 100,
    "name": "Candy Cane",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [[0, 0, 100], [0, 81, 100]],
    "type": "sequence",
    "duration": 700,
    "transition": 500,
    "direction": 1,
    "spread": 1,
    "repeat_times": 0,
    "sequence": [
        [0, 0, 100],
        [0, 0, 100],
        [360, 81, 100],
        [0, 0, 100],
        [0, 0, 100],
        [360, 81, 100],
        [360, 81, 100],
        [0, 0, 100],
        [0, 0, 100],
        [360, 81, 100],
        [360, 81, 100],
        [360, 81, 100],
        [360, 81, 100],
        [0, 0, 100],
        [0, 0, 100],
        [360, 81, 100],
    ],
}
EFFECT_CHRISTMAS = {
    "custom": 0,
    "id": "TapoStrip_5zkiG6avJ1IbhjiZbRlWvh",
    "brightness": 100,
    "name": "Christmas",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [[136, 98, 100], [350, 97, 100]],
    "type": "random",
    "hue_range": [136, 146],
    "saturation_range": [90, 100],
    "brightness_range": [50, 100],
    "duration": 5000,
    "transition": 0,
    "init_states": [[136, 0, 100]],
    "fadeoff": 2000,
    "random_seed": 100,
    "backgrounds": [[136, 98, 75], [136, 0, 0], [350, 0, 100], [350, 97, 94]],
}
EFFECT_FLICKER = {
    "custom": 0,
    "id": "TapoStrip_4HVKmMc6vEzjm36jXaGwMs",
    "brightness": 100,
    "name": "Flicker",
    "enable": 1,
    "segments": [1],
    "expansion_strategy": 1,
    "display_colors": [[30, 81, 100], [40, 100, 100]],
    "type": "random",
    "hue_range": [30, 40],
    "saturation_range": [100, 100],
    "brightness_range": [50, 100],
    "duration": 0,
    "transition": 0,
    "transition_range": [375, 500],
    "init_states": [[30, 81, 80]],
}
EFFECT_GRANDMAS_CHRISTMAS_LIGHTS = {
    "custom": 0,
    "id": "TapoStrip_3Gk6CmXOXbjCiwz9iD543C",
    "brightness": 100,
    "name": "Grandma's Christmas Lights",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [[30, 100, 100], [240, 100, 100], [130, 100, 100], [0, 100, 100]],
    "type": "sequence",
    "duration": 5000,
    "transition": 100,
    "direction": 1,
    "spread": 1,
    "repeat_times": 0,
    "sequence": [
        [30, 100, 100],
        [30, 0, 0],
        [30, 0, 0],
        [240, 100, 100],
        [240, 0, 0],
        [240, 0, 0],
        [240, 0, 100],
        [240, 0, 0],
        [240, 0, 0],
        [130, 100, 100],
        [130, 0, 0],
        [130, 0, 0],
        [0, 100, 100],
        [0, 0, 0],
        [0, 0, 0],
    ],
}
EFFECT_HANUKKAH = {
    "custom": 0,
    "id": "TapoStrip_2YTk4wramLKv5XZ9KFDVYm",
    "brightness": 100,
    "name": "Hanukkah",
    "enable": 1,
    "segments": [1],
    "expansion_strategy": 1,
    "display_colors": [[200, 100, 100]],
    "type": "random",
    "hue_range": [200, 210],
    "saturation_range": [0, 100],
    "brightness_range": [50, 100],
    "duration": 1500,
    "transition": 0,
    "transition_range": [400, 500],
    "init_states": [[35, 81, 80]],
}
EFFECT_HAUNTED_MANSION = {
    "custom": 0,
    "id": "TapoStrip_4rJ6JwC7I9st3tQ8j4lwlI",
    "brightness": 100,
    "name": "Haunted Mansion",
    "enable": 1,
    "segments": [80],
    "expansion_strategy": 2,
    "display_colors": [[44, 9, 100]],
    "type": "random",
    "hue_range": [45, 45],
    "saturation_range": [10, 10],
    "brightness_range": [0, 80],
    "duration": 0,
    "transition": 0,
    "transition_range": [50, 1500],
    "init_states": [[45, 10, 100]],
    "fadeoff": 200,
    "random_seed": 1,
    "backgrounds": [[45, 10, 100]],
}
EFFECT_ICICLE = {
    "custom": 0,
    "id": "TapoStrip_7UcYLeJbiaxVIXCxr21tpx",
    "brightness": 100,
    "name": "Icicle",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [[190, 100, 100]],
    "type": "sequence",
    "duration": 0,
    "transition": 400,
    "direction": 4,
    "spread": 3,
    "repeat_times": 0,
    "sequence": [
        [190, 100, 70],
        [190, 100, 70],
        [190, 30, 50],
        [190, 100, 70],
        [190, 100, 70],
    ],
}
EFFECT_LIGHTNING = {
    "custom": 0,
    "id": "TapoStrip_7OGzfSfnOdhoO2ri4gOHWn",
    "brightness": 100,
    "name": "Lightning",
    "enable": 1,
    "segments": [7],
    "expansion_strategy": 1,
    "display_colors": [[210, 9, 100], [200, 50, 100], [200, 100, 100]],
    "type": "random",
    "hue_range": [240, 240],
    "saturation_range": [10, 11],
    "brightness_range": [90, 100],
    "duration": 0,
    "transition": 50,
    "init_states": [[240, 30, 100]],
    "fadeoff": 150,
    "random_seed": 50,
    "backgrounds": [[200, 100, 100], [200, 50, 10], [210, 10, 50], [240, 10, 0]],
}
EFFECT_OCEAN = {
    "custom": 0,
    "id": "TapoStrip_0fOleCdwSgR0nfjkReeYfw",
    "brightness": 100,
    "name": "Ocean",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [[198, 84, 100]],
    "type": "sequence",
    "duration": 0,
    "transition": 2000,
    "direction": 3,
    "spread": 16,
    "repeat_times": 0,
    "sequence": [[198, 84, 30], [198, 70, 30], [198, 10, 30]],
}
EFFECT_RAINBOW = {
    "custom": 0,
    "id": "TapoStrip_7CC5y4lsL8pETYvmz7UOpQ",
    "brightness": 100,
    "name": "Rainbow",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [
        [0, 100, 100],
        [100, 100, 100],
        [200, 100, 100],
        [300, 100, 100],
    ],
    "type": "sequence",
    "duration": 0,
    "transition": 1500,
    "direction": 1,
    "spread": 12,
    "repeat_times": 0,
    "sequence": [[0, 100, 100], [100, 100, 100], [200, 100, 100], [300, 100, 100]],
}
EFFECT_RAINDROP = {
    "custom": 0,
    "id": "TapoStrip_1t2nWlTBkV8KXBZ0TWvBjs",
    "brightness": 100,
    "name": "Raindrop",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [[200, 9, 100], [200, 19, 100]],
    "type": "random",
    "hue_range": [200, 200],
    "saturation_range": [10, 20],
    "brightness_range": [10, 30],
    "duration": 0,
    "transition": 1000,
    "init_states": [[200, 40, 100]],
    "fadeoff": 1000,
    "random_seed": 24,
    "backgrounds": [[200, 40, 0]],
}
EFFECT_SPRING = {
    "custom": 0,
    "id": "TapoStrip_1nL6GqZ5soOxj71YDJOlZL",
    "brightness": 100,
    "name": "Spring",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [[0, 30, 100], [130, 100, 100]],
    "type": "random",
    "hue_range": [0, 90],
    "saturation_range": [30, 100],
    "brightness_range": [90, 100],
    "duration": 600,
    "transition": 0,
    "transition_range": [2000, 6000],
    "init_states": [[80, 30, 100]],
    "fadeoff": 1000,
    "random_seed": 20,
    "backgrounds": [[130, 100, 40]],
}
EFFECT_SUNRISE = {
    "custom": 0,
    "id": "TapoStrip_1OVSyXIsDxrt4j7OxyRvqi",
    "brightness": 100,
    "name": "Sunrise",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 2,
    "display_colors": [[0, 0, 100], [30, 95, 100], [0, 100, 100]],
    "type": "pulse",
    "duration": 600,
    "transition": 60000,
    "direction": 1,
    "spread": 1,
    "repeat_times": 1,
    "run_time": 0,
    "sequence": [
        [0, 100, 5],
        [0, 100, 5],
        [10, 100, 6],
        [15, 100, 7],
        [20, 100, 8],
        [20, 100, 10],
        [30, 100, 12],
        [30, 95, 15],
        [30, 90, 20],
        [30, 80, 25],
        [30, 75, 30],
        [30, 70, 40],
        [30, 60, 50],
        [30, 50, 60],
        [30, 20, 70],
        [30, 0, 100],
    ],
    "trans_sequence": [],
}
EFFECT_SUNSET = {
    "custom": 0,
    "id": "TapoStrip_5NiN0Y8GAUD78p4neKk9EL",
    "brightness": 100,
    "name": "Sunset",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 2,
    "display_colors": [[0, 100, 100], [30, 95, 100], [0, 0, 100]],
    "type": "pulse",
    "duration": 600,
    "transition": 60000,
    "direction": 1,
    "spread": 1,
    "repeat_times": 1,
    "run_time": 0,
    "sequence": [
        [30, 0, 100],
        [30, 20, 100],
        [30, 50, 99],
        [30, 60, 98],
        [30, 70, 97],
        [30, 75, 95],
        [30, 80, 93],
        [30, 90, 90],
        [30, 95, 85],
        [30, 100, 80],
        [20, 100, 70],
        [20, 100, 60],
        [15, 100, 50],
        [10, 100, 40],
        [0, 100, 30],
        [0, 100, 0],
    ],
    "trans_sequence": [],
}
EFFECT_VALENTINES = {
    "custom": 0,
    "id": "TapoStrip_2q1Vio9sSjHmaC7JS9d30l",
    "brightness": 100,
    "name": "Valentines",
    "enable": 1,
    "segments": [0],
    "expansion_strategy": 1,
    "display_colors": [[339, 19, 100], [19, 50, 100], [0, 100, 100], [339, 40, 100]],
    "type": "random",
    "hue_range": [340, 340],
    "saturation_range": [30, 40],
    "brightness_range": [90, 100],
    "duration": 600,
    "transition": 2000,
    "init_states": [[340, 30, 100]],
    "fadeoff": 3000,
    "random_seed": 100,
    "backgrounds": [[340, 20, 50], [20, 50, 50], [0, 100, 50]],
}
EFFECTS_LIST = [
    EFFECT_AURORA,
    EFFECT_BUBBLING_CAULDRON,
    EFFECT_CANDY_CANE,
    EFFECT_CHRISTMAS,
    EFFECT_FLICKER,
    EFFECT_GRANDMAS_CHRISTMAS_LIGHTS,
    EFFECT_HANUKKAH,
    EFFECT_HAUNTED_MANSION,
    EFFECT_ICICLE,
    EFFECT_LIGHTNING,
    EFFECT_OCEAN,
    EFFECT_RAINBOW,
    EFFECT_RAINDROP,
    EFFECT_SPRING,
    EFFECT_SUNRISE,
    EFFECT_SUNSET,
    EFFECT_VALENTINES,
]

EFFECT_NAMES: list[str] = [cast(str, effect["name"]) for effect in EFFECTS_LIST]
EFFECT_MAPPING = {effect["name"]: effect for effect in EFFECTS_LIST}
