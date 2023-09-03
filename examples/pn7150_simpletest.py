# SPDX-FileCopyrightText: 2023 Emil Renner Berthing
# SPDX-FileCopyrightText: 2023 Mikkel Kirkgaard Nielsen
# SPDX-FileCopyrightText: Copyright (c) 2021 Electronic Cats for Electronic Cats
#
# SPDX-License-Identifier: MIT

from time import sleep
import board
from busio import I2C
from PN7150 import PN7150

# Regular 100kHz I2C
# i2c = board.I2C()
i2c = I2C(board.SCL, board.SDA, frequency=400000)

nfc = PN7150(i2c, board.IRQ, board.VEN)

assert nfc.connect()
print("Connected.")

assert nfc.mode_rw()
print("Switched to read/write mode.")

while True:
    assert nfc.start_discovery_rw()

    print("Waiting for card..")
    card = nfc.wait_for_card()

    # Read sectors starting at 4 reading 4 sectors at a time
    for i in range(4, 24, 4):
        sector = nfc.tag_cmd(b"\x30" + i.to_bytes(1, "big"))
        print(
            "Sector {0:02d}:".format(i),
            ":".join("{:02x}".format(x) for x in sector),
            "".join([chr(x) if 128 > x > 31 else "." for x in sector]),
        )

    assert nfc.stop_discovery()

    print("ID: {}".format(card.nfcid1()))

    sleep(0.5)
