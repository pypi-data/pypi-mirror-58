### About

This is an addon for [qToggleServer](https://github.com/qtoggle/qtoggleserver).

It provides Dallas DS18B20 temperature sensor support for qToggleServer.


### Install

Install using pip:

    pip install qtoggleserver-dallastemp


### Usage

##### `qtoggleserver.conf:`
``` javascript
...
ports = [
    ...
    {
        driver = "qtoggleserver.dallastemp.ports.Temperature"
        address = "28-00000B247706"
        peripheral_name = "livingroom"
    }
    ...
]
...
```
