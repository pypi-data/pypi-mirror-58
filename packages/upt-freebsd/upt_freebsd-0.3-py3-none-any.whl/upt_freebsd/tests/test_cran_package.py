# Copyright 2019      Cyril Roelandt
#
# Licensed under the 3-clause BSD license. See the LICENSE file.
import unittest

import upt

from upt_freebsd.upt_freebsd import FreeBSDCranPackage


class TestCranPackage(unittest.TestCase):
    def setUp(self):
        upt_pkg = upt.Package('ellipsis', '0.3.0')
        self.freebsd_pkg = FreeBSDCranPackage(upt_pkg, None)

    def test_directory_name(self):
        self.assertEqual(self.freebsd_pkg.directory_name('ellipsis'),
                         'R-cran-ellipsis')

    def test_jinja2_reqformat(self):
        test_cases = [
            ('testthat', None, 'R-cran-testthat>0:XXX/R-cran-testthat'),
            ('testthat', '', 'R-cran-testthat>0:XXX/R-cran-testthat'),
            ('testthat', '>=1.0', 'R-cran-testthat>=1.0:XXX/R-cran-testthat'),
        ]
        for name, specifier, output in test_cases:
            req = upt.PackageRequirement(name, specifier)
            out = self.freebsd_pkg.jinja2_reqformat(req)
            self.assertEqual(out, output)
