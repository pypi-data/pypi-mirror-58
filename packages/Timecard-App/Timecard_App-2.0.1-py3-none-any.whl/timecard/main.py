#!/usr/bin/env python3

"""Timecard
Author(s): Jason C. McDonald

Track time spent.
"""

import logging

from timecard.interface import interface

logging.basicConfig(level=logging.INFO)


def startUI():
    return interface.run()
