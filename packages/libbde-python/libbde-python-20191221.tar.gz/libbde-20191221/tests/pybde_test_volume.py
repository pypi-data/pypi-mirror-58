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

import pybde


class VolumeTypeTests(unittest.TestCase):
  """Tests the volume type."""

  def test_signal_abort(self):
    """Tests the signal_abort function."""
    bde_volume = pybde.volume()

    bde_volume.signal_abort()

  def test_open(self):
    """Tests the open function."""
    if not unittest.source:
      return

    bde_volume = pybde.volume()

    if unittest.password:
      bde_volume.set_password(unittest.password)
    if unittest.recovery_password:
      bde_volume.set_recovery_password(
          unittest.recovery_password)

    bde_volume.open(unittest.source)

    with self.assertRaises(IOError):
      bde_volume.open(unittest.source)

    bde_volume.close()

    with self.assertRaises(TypeError):
      bde_volume.open(None)

    with self.assertRaises(ValueError):
      bde_volume.open(unittest.source, mode="w")

  def test_open_file_object(self):
    """Tests the open_file_object function."""
    if not unittest.source:
      return

    file_object = open(unittest.source, "rb")

    bde_volume = pybde.volume()

    if unittest.password:
      bde_volume.set_password(unittest.password)
    if unittest.recovery_password:
      bde_volume.set_recovery_password(
          unittest.recovery_password)

    bde_volume.open_file_object(file_object)

    # TODO: fix
    # with self.assertRaises(IOError):
    #   bde_volume.open_file_object(file_object)

    bde_volume.close()

    # TODO: change IOError into TypeError
    with self.assertRaises(IOError):
      bde_volume.open_file_object(None)

    with self.assertRaises(ValueError):
      bde_volume.open_file_object(file_object, mode="w")

  def test_close(self):
    """Tests the close function."""
    if not unittest.source:
      return

    bde_volume = pybde.volume()

    # TODO: fix
    # with self.assertRaises(IOError):
    #   bde_volume.close()

  def test_open_close(self):
    """Tests the open and close functions."""
    if not unittest.source:
      return

    bde_volume = pybde.volume()

    if unittest.password:
      bde_volume.set_password(unittest.password)
    if unittest.recovery_password:
      bde_volume.set_recovery_password(
          unittest.recovery_password)

    # Test open and close.
    bde_volume.open(unittest.source)
    bde_volume.close()

    # Test open and close a second time to validate clean up on close.
    bde_volume.open(unittest.source)
    bde_volume.close()

    file_object = open(unittest.source, "rb")

    # Test open_file_object and close.
    bde_volume.open_file_object(file_object)
    bde_volume.close()

    # Test open_file_object and close a second time to validate clean up on close.
    bde_volume.open_file_object(file_object)
    bde_volume.close()

    # Test open_file_object and close and dereferencing file_object.
    bde_volume.open_file_object(file_object)
    del file_object
    bde_volume.close()

  def test_read_buffer(self):
    """Tests the read_buffer function."""
    if not unittest.source:
      return

    bde_volume = pybde.volume()

    if unittest.password:
      bde_volume.set_password(unittest.password)
    if unittest.recovery_password:
      bde_volume.set_recovery_password(
          unittest.recovery_password)

    bde_volume.open(unittest.source)

    file_size = bde_volume.get_size()

    # Test normal read.
    data = bde_volume.read_buffer(size=4096)

    self.assertIsNotNone(data)
    self.assertEqual(len(data), min(file_size, 4096))

    if file_size < 4096:
      data = bde_volume.read_buffer()

      self.assertIsNotNone(data)
      self.assertEqual(len(data), file_size)

    # Test read beyond file size.
    if file_size > 16:
      bde_volume.seek_offset(-16, os.SEEK_END)

      data = bde_volume.read_buffer(size=4096)

      self.assertIsNotNone(data)
      self.assertEqual(len(data), 16)

    with self.assertRaises(ValueError):
      bde_volume.read_buffer(size=-1)

    bde_volume.close()

    # Test the read without open.
    with self.assertRaises(IOError):
      bde_volume.read_buffer(size=4096)

  def test_read_buffer_file_object(self):
    """Tests the read_buffer function on a file-like object."""
    if not unittest.source:
      return

    file_object = open(unittest.source, "rb")

    bde_volume = pybde.volume()

    if unittest.password:
      bde_volume.set_password(unittest.password)
    if unittest.recovery_password:
      bde_volume.set_recovery_password(
          unittest.recovery_password)

    bde_volume.open_file_object(file_object)

    file_size = bde_volume.get_size()

    # Test normal read.
    data = bde_volume.read_buffer(size=4096)

    self.assertIsNotNone(data)
    self.assertEqual(len(data), min(file_size, 4096))

    bde_volume.close()

  def test_read_buffer_at_offset(self):
    """Tests the read_buffer_at_offset function."""
    if not unittest.source:
      return

    bde_volume = pybde.volume()

    if unittest.password:
      bde_volume.set_password(unittest.password)
    if unittest.recovery_password:
      bde_volume.set_recovery_password(
          unittest.recovery_password)

    bde_volume.open(unittest.source)

    file_size = bde_volume.get_size()

    # Test normal read.
    data = bde_volume.read_buffer_at_offset(4096, 0)

    self.assertIsNotNone(data)
    self.assertEqual(len(data), min(file_size, 4096))

    # Test read beyond file size.
    if file_size > 16:
      data = bde_volume.read_buffer_at_offset(4096, file_size - 16)

      self.assertIsNotNone(data)
      self.assertEqual(len(data), 16)

    with self.assertRaises(ValueError):
      bde_volume.read_buffer_at_offset(-1, 0)

    with self.assertRaises(ValueError):
      bde_volume.read_buffer_at_offset(4096, -1)

    bde_volume.close()

    # Test the read without open.
    with self.assertRaises(IOError):
      bde_volume.read_buffer_at_offset(4096, 0)

  def test_seek_offset(self):
    """Tests the seek_offset function."""
    if not unittest.source:
      return

    bde_volume = pybde.volume()

    if unittest.password:
      bde_volume.set_password(unittest.password)
    if unittest.recovery_password:
      bde_volume.set_recovery_password(
          unittest.recovery_password)

    bde_volume.open(unittest.source)

    file_size = bde_volume.get_size()

    bde_volume.seek_offset(16, os.SEEK_SET)

    offset = bde_volume.get_offset()
    self.assertEqual(offset, 16)

    bde_volume.seek_offset(16, os.SEEK_CUR)

    offset = bde_volume.get_offset()
    self.assertEqual(offset, 32)

    bde_volume.seek_offset(-16, os.SEEK_CUR)

    offset = bde_volume.get_offset()
    self.assertEqual(offset, 16)

    bde_volume.seek_offset(-16, os.SEEK_END)

    offset = bde_volume.get_offset()
    self.assertEqual(offset, file_size - 16)

    bde_volume.seek_offset(16, os.SEEK_END)

    offset = bde_volume.get_offset()
    self.assertEqual(offset, file_size + 16)

    # TODO: change IOError into ValueError
    with self.assertRaises(IOError):
      bde_volume.seek_offset(-1, os.SEEK_SET)

    # TODO: change IOError into ValueError
    with self.assertRaises(IOError):
      bde_volume.seek_offset(-32 - file_size, os.SEEK_CUR)

    # TODO: change IOError into ValueError
    with self.assertRaises(IOError):
      bde_volume.seek_offset(-32 - file_size, os.SEEK_END)

    # TODO: change IOError into ValueError
    with self.assertRaises(IOError):
      bde_volume.seek_offset(0, -1)

    bde_volume.close()

    # Test the seek without open.
    with self.assertRaises(IOError):
      bde_volume.seek_offset(16, os.SEEK_SET)


if __name__ == "__main__":
  argument_parser = argparse.ArgumentParser()

  argument_parser.add_argument(
      "source", nargs="?", action="store", metavar="PATH",
      default=None, help="The path of the source file.")

  argument_parser.add_argument(        
      "-p", dest="password", action="store", metavar="PASSWORD",      
      default=None, help="The password.")     
      
  argument_parser.add_argument(       
      "-r", dest="recovery_password", action="store", metavar="PASSWORD",     
      default=None, help="The recovery password.")

  options, unknown_options = argument_parser.parse_known_args()
  unknown_options.insert(0, sys.argv[0])

  setattr(unittest, "password", options.password)
  setattr(unittest, "source", options.source)
  setattr(unittest, "recovery_password", options.recovery_password)

  unittest.main(argv=unknown_options, verbosity=2)
