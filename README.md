# ha-constant-modifier
This is a custom integration for Home Assistant that can be used to modify, patch or overwrite constants in other components.

## Installation
To install, place the constant_modifier in your Home Assistant configuration directory under the custom_components folder

## Configuration
Add to `configuration.yaml` the HA core component modules and any constants you need to modify. For example

```
constant_modifier:
  zhaquirks.xiaomi:
    MotionCluster.reset_s: 5 # default 70
    OccupancyCluster.reset_s: 180 # default 600
```

## Note
This integration was forked from original component by [@puddly](https://github.com/puddly), which does not seem to be maintained anymore. The main purpose for me to modify it for latest HA versions is to modify ZHA device constants, such as Aqara/Xiaomi occupancy timeout and motion reset timeout, which otherwise cannot be modified easily through the ZHA integration. This is discussed in length in HA community forum post [Xiaomi Human / Body / Motion Sensor - Timeout](https://community.home-assistant.io/t/xiaomi-human-body-motion-sensor-timeout/23398/481)


## Credits
Original version was authored by [@puddly](https://github.com/puddly).
