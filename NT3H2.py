# SPDX-FileCopyrightText: 2023 Emil Renner Berthing
# SPDX-FileCopyrightText: 2023 Mikkel Kirkgaard Nielsen
# SPDX-FileCopyrightText: Copyright (c) 2021 Electronic Cats for Electronic Cats
#
# SPDX-License-Identifier: MIT
"""
Util for NT3H2
"""

from busio import I2C


class NT3H2:
    """Class NT3H2."""

    def __init__(self, i2c: I2C, addr: int = 0x55):
        """Function __init__."""
        self._i2c = i2c
        self._addr = addr
        self._buf = bytearray(17)

    def _readpage(self, page: int):
        """Function _readpage."""
        self._buf[0] = page
        self._i2c.writeto_then_readfrom(
            self._addr, self._buf, self._buf, out_end=1, in_start=1
        )

    def readpage(self, page: int):
        """Function read page."""
        assert self._i2c.try_lock()
        self._readpage(page)
        self._i2c.unlock()
        print(
            "Page {:02}:{}".format(
                page, "".join(" {:02x}".format(x) for x in self._buf[1:])
            )
        )

    def set_addr(self, addr: int):
        """Function set address."""
        assert self._i2c.try_lock()
        self._readpage(0x00)
        self._buf[1] = 2 * addr
        self._i2c.writeto(self._addr, self._buf)
        self._addr = addr
        self._i2c.unlock()
