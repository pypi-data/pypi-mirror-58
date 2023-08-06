# Copyright 2018      Cyril Roelandt
#
# Licensed under the 3-clause BSD license. See the LICENSE file.
import unittest

import upt

from upt_freebsd.upt_freebsd import FreeBSDBackend


class TestFreeBSDBackend(unittest.TestCase):
    def setUp(self):
        self.freebsd_backend = FreeBSDBackend()

    def test_unhandled_frontend(self):
        upt_pkg = upt.Package('foo', '42')
        upt_pkg.frontend = 'invalid frontend'
        with self.assertRaises(upt.UnhandledFrontendError):
            self.freebsd_backend.create_package(upt_pkg)


if __name__ == '__main__':
    unittest.main()
