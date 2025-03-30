# ha-constant-modifier

[![GitHub Release][releases-shield]][releases]
[![Issues][issues-shield]][issues]
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![License][license-shield]](LICENSE)
![python badge][python-shield]

This is a custom integration for Home Assistant that can be used to modify, patch or overwrite constants in other components.
It cannot be setup via UI, but requires configuration via your configuration.yaml file.

## Installation via HACS (recommended)

Use this button to add the repository to your HACS custom repositories:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.][hacs-repo-badge]][hacs-install]

Or use following procedure for HACS 2.0 or later to add the custom repository:
1. Open the [HACS](https://hacs.xyz) panel in your Home Assistant frontend.
1. Click the three dots in the top-right corner and select "Custom Repositories."
1. Add a new custom repository via the Popup dialog:
   - **Repository URL:** `https://github.com/thomluther/ha-constant-modifier`
   - **Type:** Integration
1. Click "Add" and verify that the `HA constant modifier` repository was added to the list.
1. Close the Popup dialog and verify that `HA constant modifier` integration is now listed in the Home Assistant Community Store.
1. You cannot install the integration via the Home Assistant UI, but you need to configure it as described below

### Installation Notes
- It was observed that when adding the repository to HACS via the button, an error may occur although it was added. You may check if you can find HA constant modifier listed as possible HACS integration to be installed. If not, try to add the repository again.
- After adding the custom repository and installing the integration under HACS, you must restart Home Assistant to pick up the changes in your custom integration folder
   - HA 2024.02 will report the required restart automatically under problems
- After HA restart, you can configure the integration through your `configuration.yaml` file.


## Manual Installation

1. Using the tool of choice to open the directory (folder) for your HA configuration (where your `configuration.yaml` is located, e.g. `/homeassistant`)
1. If you do not have a `custom_components` directory (folder) there, you need to create it
1. In the `custom_components` directory (folder) create a new folder called `constant_modifier`
1. Download _all_ the files from the `custom_components/constant_modifier/` directory (folder) in this repository
1. Place the files you downloaded in the new directory (folder) you created
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "HA constant modifier"
1. Even if listed, you cannot configure the integration via the UI but need to configure it through your `configuration.yaml` file.


## Configuration

Open your Home Assistant `configuration.yaml` file and add the HA component modules and any constants you want to modify. For example:

```yaml
constant_modifier:
  zhaquirks.xiaomi:
    MotionCluster.reset_s: 5 # default 70
    OccupancyCluster.reset_s: 180 # default 600
```

## Note

This integration was forked from [original component](https://github.com/puddly/ha-constant-modifier), which does not seem to be maintained anymore. The main purpose for me to modify it for latest HA versions is to modify ZHA device constants, such as Aqara/Xiaomi occupancy timeout and motion reset timeout, which otherwise cannot be modified easily through the ZHA integration. This is discussed in length in HA community forum post [Xiaomi Human / Body / Motion Sensor - Timeout](https://community.home-assistant.io/t/xiaomi-human-body-motion-sensor-timeout/23398/481)


## Attribution

[Original version of ha-constant-modifier](https://github.com/puddly/ha-constant-modifier) was authored by [@puddly](https://github.com/puddly).


## Showing Your Appreciation

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)][buy-me-coffee]

If you like this project, please give it a star on [GitHub][ha-constant-modifier]
***

[ha-constant-modifier]: https://github.com/thomluther/ha-constant-modifier
[hacs-repo-badge]: https://my.home-assistant.io/badges/hacs_repository.svg
[hacs-install]: https://my.home-assistant.io/redirect/hacs_repository/?owner=thomluther&repository=https%3A%2F%2Fgithub.com%2Fthomluther%2Fha-constant-modifier&category=Integration
[buy-me-coffee]: https://www.buymeacoffee.com/thomasluthe
[license-shield]: https://img.shields.io/badge/Licence-MIT-orange
[license]: https://github.com/thomluther/ha-anker-solix/blob/main/LICENSE
[python-shield]: https://img.shields.io/badge/Made%20with-Python-orange
[releases]: https://github.com/thomluther/ha-constant-modifier/releases
[releases-shield]: https://img.shields.io/github/release/thomluther/ha-constant-modifier.svg?style=for-the-badge
[issues]: https://github.com/thomluther/ha-constant-modifier/issues
[issues-shield]: https://img.shields.io/github/issues/thomluther/ha-constant-modifier.svg?style=for-the-badge
