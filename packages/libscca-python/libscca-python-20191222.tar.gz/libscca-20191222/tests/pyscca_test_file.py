#!/usr/bin/env python
#
# Python-bindings file type test script
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

import pyscca


class FileTypeTests(unittest.TestCase):
  """Tests the file type."""

  def test_signal_abort(self):
    """Tests the signal_abort function."""
    scca_file = pyscca.file()

    scca_file.signal_abort()

  def test_open(self):
    """Tests the open function."""
    if not unittest.source:
      return

    scca_file = pyscca.file()

    scca_file.open(unittest.source)

    with self.assertRaises(IOError):
      scca_file.open(unittest.source)

    scca_file.close()

    with self.assertRaises(TypeError):
      scca_file.open(None)

    with self.assertRaises(ValueError):
      scca_file.open(unittest.source, mode="w")

  def test_open_file_object(self):
    """Tests the open_file_object function."""
    if not unittest.source:
      return

    file_object = open(unittest.source, "rb")

    scca_file = pyscca.file()

    scca_file.open_file_object(file_object)

    with self.assertRaises(IOError):
      scca_file.open_file_object(file_object)

    scca_file.close()

    # TODO: change IOError into TypeError
    with self.assertRaises(IOError):
      scca_file.open_file_object(None)

    with self.assertRaises(ValueError):
      scca_file.open_file_object(file_object, mode="w")

  def test_close(self):
    """Tests the close function."""
    if not unittest.source:
      return

    scca_file = pyscca.file()

    with self.assertRaises(IOError):
      scca_file.close()

  def test_open_close(self):
    """Tests the open and close functions."""
    if not unittest.source:
      return

    scca_file = pyscca.file()

    # Test open and close.
    scca_file.open(unittest.source)
    scca_file.close()

    # Test open and close a second time to validate clean up on close.
    scca_file.open(unittest.source)
    scca_file.close()

    file_object = open(unittest.source, "rb")

    # Test open_file_object and close.
    scca_file.open_file_object(file_object)
    scca_file.close()

    # Test open_file_object and close a second time to validate clean up on close.
    scca_file.open_file_object(file_object)
    scca_file.close()

    # Test open_file_object and close and dereferencing file_object.
    scca_file.open_file_object(file_object)
    del file_object
    scca_file.close()


if __name__ == "__main__":
  argument_parser = argparse.ArgumentParser()

  argument_parser.add_argument(
      "source", nargs="?", action="store", metavar="PATH",
      default=None, help="The path of the source file.")

  options, unknown_options = argument_parser.parse_known_args()
  unknown_options.insert(0, sys.argv[0])

  setattr(unittest, "source", options.source)

  unittest.main(argv=unknown_options, verbosity=2)
