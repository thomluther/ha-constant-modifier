"""Home Assistant constant modifier."""

import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.importlib import async_import_module
from homeassistant.helpers.typing import ConfigType

LOGGER = logging.getLogger(__package__)
DOMAIN = "constant_modifier"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the constant_modifier component.

    Patches constants specified as key/value pairs.
    For example:

    constant_modifier:
      # `MAX_PENDING_MSG` is a top-level constant
      homeassistant.components.websocket_api.http.MAX_PENDING_MSG: 4096

      homeassistant.components.websocket_api.http:
        MAX_PENDING_MSG: 4096  # `MAX_PENDING_MSG` is a top-level constant

      zhaquirks.xiaomi:
        MotionCluster.reset_s: 5  # `MotionCluster` is a class with a `reset_s` attr
    """

    for module_name, replacements in config[DOMAIN].items():
        # Old-style "module.ATTR: value" is replaced with "module: ATTR: value"
        if not isinstance(replacements, dict):
            value = replacements
            module_name, constant = module_name.rsplit(".", 1)
            replacements = {constant: value}

        for path, value in replacements.items():
            *attrs, attr = path.split(".")
            try:
                obj = await async_import_module(hass, module_name)
            except ModuleNotFoundError as err:
                LOGGER.error("Defined module '%s' not found: %s", module_name, err)
                continue

            # get object before last qualifier
            for a in attrs:
                if not (obj := getattr(obj, a, None)):
                    LOGGER.error(
                        "Defined object '%s' of path '%s' not found in module '%s'",
                        a,
                        path,
                        module_name,
                    )
                    break
            else:
                # only executed if the inner loop did NOT break
                # change attribute in object
                if old_value := getattr(obj, attr, None):
                    setattr(obj, attr, value)
                    LOGGER.warning(
                        "Patched %s, %s = %s (was %s)", module_name, path, value, old_value
                    )
                else:
                    LOGGER.error(
                        "Defined attribute '%s' not found in module '%s'", attr, module_name
                    )

    return True
