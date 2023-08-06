motorengine-async is based and inspired on [motorengine](https://github.com/heynemann/motorengine) to provide asyncio instead of `future` concept from `tornado`.
===========

**Notice: Need Python 3.7+** Using asyncio(async/await) in python3.7+ to replace callback method for sake of asynchronous style. For instance, the `return_future` decorator from `tornado`(v5.1 below) has been revised and adapted to `tornado`(v6.0+).

[![Build Status](https://travis-ci.org/heynemann/motorengine.png?branch=master)](https://travis-ci.org/heynemann/motorengine)
[![PyPi version](https://img.shields.io/pypi/v/motorengine.svg)](https://pypi.python.org/pypi/motorengine/)
[![Coverage Status](https://coveralls.io/repos/heynemann/motorengine/badge.png?branch=master)](https://coveralls.io/r/heynemann/motorengine?branch=master)

motorengine is a port of the incredible mongoengine mapper, using Motor for asynchronous access to mongo.

Find out more by reading [motorengine documentation](http://motorengine.readthedocs.org/en/latest/).
