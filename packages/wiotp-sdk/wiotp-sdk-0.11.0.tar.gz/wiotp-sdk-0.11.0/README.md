# Python for IBM Watson IoT Platform

[![Build Status](https://travis-ci.org/ibm-watson-iot/iot-python.svg?branch=master)](https://travis-ci.org/ibm-watson-iot/iot-python)
[![Coverage Status](https://coveralls.io/repos/github/ibm-watson-iot/iot-python/badge.svg?branch=master)](https://coveralls.io/github/ibm-watson-iot/iot-python?branch=master)
[![GitHub issues](https://img.shields.io/github/issues/ibm-watson-iot/iot-python.svg)](https://github.com/ibm-watson-iot/iot-python/issues)
[![GitHub](https://img.shields.io/github/license/ibm-watson-iot/iot-python.svg)](https://github.com/ibm-watson-iot/iot-python/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/wiotp-sdk.svg)](https://pypi.org/project/wiotp-sdk/)
[![Downloads](https://pepy.tech/badge/ibmiotf)](https://pepy.tech/project/ibmiotf)
[![Downloads](https://pepy.tech/badge/wiotp-sdk)](https://pepy.tech/project/wiotp-sdk)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Python module for interacting with the [IBM Watson IoT Platform](https://internetofthings.ibmcloud.com).

-  [Python 3.7](https://www.python.org/downloads/release/python-373/)  (recommended)
-  [Python 2.7](https://www.python.org/downloads/release/python-2716/)

Note: Support for MQTT with TLS requires at least Python v2.7.9 and openssl v1.0.1


## Dependencies

-  [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt)
-  [iso8601](https://pypi.python.org/pypi/iso8601)
-  [pytz](https://pypi.python.org/pypi/pytz)
-  [requests](https://pypi.python.org/pypi/requests)


## Installation

Install the [latest version](https://pypi.org/project/wiotp-sdk/) of the library with pip

```
# pip install wiotp-sdk
```


## Uninstall

Uninstalling the module is simple.

```
# pip uninstall wiotp-sdk
```

## Legacy ibmiotf Module

Version `0.4.0` of the old [ibmiotf](https://pypi.python.org/pypi/ibmiotf) pre-release is still available, if you do not wish to upgrade to the new version, we have no plans to remove this from pypi at this time, however it will not be getting any updates.


## Documentation

https://ibm-watson-iot.github.io/iot-python/


## Supported Features

- **Device Connectivity**: Connect your device(s) to Watson IoT Platform with ease using this library
- **Gateway Connectivity**: Connect your gateway(s) to Watson IoT Platform with ease using this library
- **Application connectivity**: Connect your application(s) to Watson IoT Platform with ease using this library
- **Watson IoT API**: Support for the interacting with the Watson IoT Platform through REST APIs
- **SSL/TLS**: By default, this library connects your devices, gateways and applications securely to Watson IoT Platform registered service. Ports `8883` (default) and `443` support secure connections using TLS with the MQTT and HTTP protocol. Support for MQTT with TLS requires at least Python v2.7.9 or v3.4, and openssl v1.0.1
- **Device Management for Device**: Connects your device(s) as managed device(s) to Watson IoT Platform.
- **Device Management for Gateway**: Connects your gateway(s) as managed device(s) to Watson IoT Platform.
- **Device Management Extensions**: Provides support for custom device management actions.
- **Scalable Applications**: Supports load balancing of MQTT subscriptions over multiple application instances.
- **Auto Reconnect**: All clients support automatic reconnect to the Platform in the event of a network interruption.
- **Websockets**: Support device/gateway/application connectivity to Watson IoT Platform using WebSocket


## Unsupported Features
- **Client side Certificate based authentication**: [Client side Certificate based authentication](https://console.ng.bluemix.net/docs/services/IoT/reference/security/RM_security.html)n

