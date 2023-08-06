#!/usr/bin/env python
#
# Python-bindings volume type test script
#
# Copyright (C) 2011-2019, Joachim Metz <joachim.metz@gmail.com>
#
# Refer to AUTHORS for acknowledgements.
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import os
import sys
import unittest

import pyvshadow


class VolumeTypeTests(unittest.TestCase):
  """Tests the volume type."""

  def test_signal_abort(self):
    """Tests the signal_abort function."""
    vshadow_volume = pyvshadow.volume()

    vshadow_volume.signal_abort()

  def test_open(self):
    """Tests the open function."""
    if not unittest.source or unittest.offset != 0:
      raise unittest.SkipTest("missing source")

    vshadow_volume = pyvshadow.volume()

    vshadow_volume.open(unittest.source)

    with self.assertRaises(IOError):
      vshadow_volume.open(unittest.source)

    vshadow_volume.close()

    with self.assertRaises(TypeError):
      vshadow_volume.open(None)

    with self.assertRaises(ValueError):
      vshadow_volume.open(unittest.source, mode="w")

  def test_open_file_object(self):
    """Tests the open_file_object function."""
    if not unittest.source or unittest.offset != 0:
      raise unittest.SkipTest("missing source")

    file_object = open(unittest.source, "rb")

    vshadow_volume = pyvshadow.volume()

    vshadow_volume.open_file_object(file_object)

    with self.assertRaises(IOError):
      vshadow_volume.open_file_object(file_object)

    vshadow_volume.close()

    # TODO: change IOError into TypeError
    with self.assertRaises(IOError):
      vshadow_volume.open_file_object(None)

    with self.assertRaises(ValueError):
      vshadow_volume.open_file_object(file_object, mode="w")

  def test_close(self):
    """Tests the close function."""
    vshadow_volume = pyvshadow.volume()

    with self.assertRaises(IOError):
      vshadow_volume.close()

  def test_open_close(self):
    """Tests the open and close functions."""
    if not unittest.source or unittest.offset != 0:
      raise unittest.SkipTest("missing source")

    vshadow_volume = pyvshadow.volume()

    # Test open and close.
    vshadow_volume.open(unittest.source)
    vshadow_volume.close()

    # Test open and close a second time to validate clean up on close.
    vshadow_volume.open(unittest.source)
    vshadow_volume.close()

    file_object = open(unittest.source, "rb")

    # Test open_file_object and close.
    vshadow_volume.open_file_object(file_object)
    vshadow_volume.close()

    # Test open_file_object and close a second time to validate clean up on close.
    vshadow_volume.open_file_object(file_object)
    vshadow_volume.close()

    # Test open_file_object and close and dereferencing file_object.
    vshadow_volume.open_file_object(file_object)
    del file_object
    vshadow_volume.close()

  def test_get_number_of_stores(self):
    """Tests the get_number_of_stores function."""
    if not unittest.source or unittest.offset != 0:
      raise unittest.SkipTest("missing source")

    vshadow_volume = pyvshadow.volume()

    vshadow_volume.open(unittest.source)

    number_of_stores = vshadow_volume.get_number_of_stores()
    self.assertIsNotNone(number_of_stores)

    vshadow_volume.close()

  def test_get_store(self):
    """Tests the get_store function."""
    if not unittest.source or unittest.offset != 0:
      raise unittest.SkipTest("missing source")

    vshadow_volume = pyvshadow.volume()

    vshadow_volume.open(unittest.source)

    if vshadow_volume.number_of_stores > 0:
      vshadow_store = vshadow_volume.get_store(
          vshadow_volume.number_of_stores - 1)
      self.assertIsNotNone(vshadow_store)

      with self.assertRaises(IOError):
        vshadow_volume.get_store(-1)

    vshadow_volume.close()

  def test_number_of_stores(self):
    """Tests the number_of_stores property."""
    if not unittest.source or unittest.offset != 0:
      raise unittest.SkipTest("missing source")

    vshadow_volume = pyvshadow.volume()

    vshadow_volume.open(unittest.source)

    self.assertIsNotNone(vshadow_volume.number_of_stores)

    vshadow_volume.close()

  def test_stores(self):
    """Tests the stores property."""
    if not unittest.source or unittest.offset != 0:
      raise unittest.SkipTest("missing source")

    vshadow_volume = pyvshadow.volume()

    vshadow_volume.open(unittest.source)

    number_of_stores = vshadow_volume.get_number_of_stores()
    if number_of_stores > 0:
      self.assertIsNotNone(vshadow_volume.stores)

    vshadow_volume.close()


if __name__ == "__main__":
  argument_parser = argparse.ArgumentParser()

  argument_parser.add_argument(
      "-o", "--offset", dest="offset", action="store", default=0,
      type=int, help="offset of the source file.")

  argument_parser.add_argument(
      "source", nargs="?", action="store", metavar="PATH",
      default=None, help="path of the source file.")

  options, unknown_options = argument_parser.parse_known_args()
  unknown_options.insert(0, sys.argv[0])

  setattr(unittest, "offset", options.offset)
  setattr(unittest, "source", options.source)

  unittest.main(argv=unknown_options, verbosity=2)
