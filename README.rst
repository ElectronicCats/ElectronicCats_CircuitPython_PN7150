ElectronicCats_CircuitPython_PN7150
============


.. image:: https://readthedocs.org/projects/electroniccats-circuitpython-pn7150/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/pn7150/en/latest/
    :alt: Documentation Status


.. image:: https://github.com/ElectronicCats/Electroniccats_CircuitPython_PN7150/workflows/Build%20CI/badge.svg
    :target: https://github.com/ElectronicCats/Electroniccats_CircuitPython_PN7150/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

library for I2C access to the PN7150 RFID/Near Field Communication chip


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

.. todo:: Remove the above note if PyPI version is/will be available at time of release.

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/electroniccats-circuitpython-pn7150/>`_.
To install for current user:

.. code-block:: shell

    pip3 install electroniccats-circuitpython-pn7150

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install electroniccats-circuitpython-pn7150

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-pn7150



Usage Example
=============

This example demonstrates the library with the  PN7150
`BomberCat <https://electroniccats.com/store/bombercat/>`_ and
`HunterCat NFC <https://electroniccats.com/store/hunter-cat-nfc/>`_.

.. code-block:: python


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/ElectronicCats/Electroniccats_CircuitPython_PN7150/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

