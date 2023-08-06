# Copyright 2018      Cyril Roelandt
#
# Licensed under the 3-clause BSD license. See the LICENSE file.
import os
import tempfile
import unittest
from unittest import mock

import upt

from upt_freebsd.upt_freebsd import FreeBSDPackage


class TestDirectoryCreation(unittest.TestCase):
    def setUp(self):
        self.upt_pkg = upt.Package('foo', '42')

    def test_directory_name(self):
        freebsd_pkg = FreeBSDPackage(self.upt_pkg, None)
        self.assertEqual(freebsd_pkg.directory_name('foo'), 'foo')

    @mock.patch('os.getcwd')
    @mock.patch('os.makedirs')
    def test_create_directory_no_output(self, m_mkdir, m_cwd):
        m_cwd.return_value = '/cwd'
        freebsd_pkg = FreeBSDPackage(self.upt_pkg, None)
        freebsd_pkg._create_output_directory()
        m_mkdir.assert_called_with('/cwd/foo')

    @mock.patch('os.makedirs')
    def test_create_directory_output(self, m_mkdir):
        freebsd_pkg = FreeBSDPackage(self.upt_pkg, '/path/to/dir')
        freebsd_pkg._create_output_directory()
        m_mkdir.assert_called_with('/path/to/dir/foo')

    @mock.patch('os.path.expanduser')
    @mock.patch('os.makedirs')
    def test_create_directory_output_tilde(self, m_mkdir, m_expand):
        m_expand.return_value = '/home/user/ports'
        freebsd_pkg = FreeBSDPackage(self.upt_pkg, '~/ports')
        freebsd_pkg._create_output_directory()
        m_mkdir.assert_called_with('/home/user/ports/foo')

    @mock.patch('os.makedirs', side_effect=PermissionError)
    def test_create_directories_permission_error(self, m_makedirs):
        freebsd_pkg = FreeBSDPackage(self.upt_pkg, '~/ports')
        with self.assertRaises(SystemExit):
            freebsd_pkg._create_output_directory()

    @mock.patch('os.makedirs', side_effect=FileExistsError)
    def test_create_directories_file_exists(self, m_makedirs):
        freebsd_pkg = FreeBSDPackage(self.upt_pkg, '~/ports')
        with self.assertRaises(SystemExit):
            freebsd_pkg._create_output_directory()


class TestFreeBSDPackage(unittest.TestCase):
    def setUp(self):
        self.upt_pkg = upt.Package('foo', '42',
                                   summary='Summary',
                                   homepage='homepage')
        self.freebsd_pkg = FreeBSDPackage(self.upt_pkg, None)

    def test_portname(self):
        self.assertEqual(self.freebsd_pkg.portname, 'foo')

    def test_jinja2_reqformat(self):
        req = upt.PackageRequirement('foo', '>=1.0')
        out = self.freebsd_pkg.jinja2_reqformat(req)
        self.assertEqual(out, 'foo>=1.0:XXX/foo')

    def test_jinja2_reqformat_no_specifier(self):
        req = upt.PackageRequirement('foo', '')
        out = self.freebsd_pkg.jinja2_reqformat(req)
        self.assertEqual(out, 'foo>0:XXX/foo')

    def test_categories(self):
        self.freebsd_pkg.output_dir = '/usr/ports/ports-mgmt/py-upt-freebsd'
        self.freebsd_pkg.language_category = 'language'
        self.assertListEqual(self.freebsd_pkg.categories,
                             ['ports-mgmt', 'language'])

    def test_categories_invalid_category(self):
        self.freebsd_pkg.output_dir = '/usr/ports/invalid/py-upt-freebsd'
        self.freebsd_pkg.language_category = 'language'
        self.assertListEqual(self.freebsd_pkg.categories, ['XXX', 'language'])

    def test_categories_no_language_category(self):
        self.freebsd_pkg.output_dir = '/usr/ports/sysutils/py-upt-freebsd'
        self.assertListEqual(self.freebsd_pkg.categories, ['sysutils'])

    def test_attributes(self):
        self.assertEqual(self.upt_pkg.version, self.freebsd_pkg.version)
        self.assertEqual(self.upt_pkg.homepage, self.freebsd_pkg.homepage)


class TestFreeBSDPackageLicenses(unittest.TestCase):
    def setUp(self):
        self.upt_pkg = upt.Package('foo', '42')
        self.freebsd_pkg = FreeBSDPackage(self.upt_pkg, None)

    def test_no_licenses(self):
        self.freebsd_pkg.upt_pkg.licenses = []
        self.assertEqual(self.freebsd_pkg.licenses, '')

    def test_one_license(self):
        self.freebsd_pkg.upt_pkg.licenses = [
            upt.licenses.BSDThreeClauseLicense()
        ]
        self.assertEqual(self.freebsd_pkg.licenses, 'BSD3CLAUSE')

    def test_unknown_license(self):
        self.freebsd_pkg.upt_pkg.licenses = [upt.licenses.UnknownLicense()]
        self.assertEqual(self.freebsd_pkg.licenses, 'XXX')

    def test_multiple_licenses(self):
        self.freebsd_pkg.upt_pkg.licenses = [
            upt.licenses.BSDTwoClauseLicense(),
            upt.licenses.BSDThreeClauseLicense()
        ]
        self.assertEqual(self.freebsd_pkg.licenses, 'BSD2CLAUSE BSD3CLAUSE')

    def test_fix_summary(self):
        test_cases = [
            ('', ''),
            ('Perfect summary', 'Perfect summary'),
            ('Dot at the end.', 'Dot at the end'),
            ('starts with lowercase letter', 'Starts with lowercase letter'),
            ('Dots at the end...', 'Dots at the end'),
            ('Spaces at the end    ', 'Spaces at the end'),
            ('Dots and spaces at the end ...', 'Dots and spaces at the end'),
            ('lowercase and dot.', 'Lowercase and dot'),
        ]
        for input_, output in test_cases:
            self.assertEqual(FreeBSDPackage._fix_summary(input_), output)


class TestFreeBSDCategoryFinder(unittest.TestCase):
    def setUp(self):
        self.fake_usr_ports = tempfile.TemporaryDirectory()
        self.user_ports_dir = tempfile.TemporaryDirectory()
        os.makedirs(os.path.join(self.fake_usr_ports.name, 'www/py-requests'))
        os.makedirs(os.path.join(self.user_ports_dir.name, 'yyy/py-requests'))
        self.upt_pkg = upt.Package('foo', '42')
        self.freebsd_pkg = FreeBSDPackage(self.upt_pkg, None)

    def tearDown(self):
        # Explicitly cleanup after ourselves. This is not necessary (the
        # directories would get cleaned up anyway), but this prevents annoying
        # warning messages from showing up on the screen.
        self.fake_usr_ports.cleanup()
        self.user_ports_dir.cleanup()

    @mock.patch.dict(os.environ, {}, clear=True)
    def test_find_category_no_env_var(self):
        # - $PORTSDIR is not set
        # - A ports tree exists in the default location (/usr/ports)
        with mock.patch('upt_freebsd.upt_freebsd.DEFAULT_PORTSDIR',
                        self.fake_usr_ports.name):
            self.assertEqual(self.freebsd_pkg._find_category('py-requests'),
                             'www')

    @mock.patch.dict(os.environ, {}, clear=True)
    def test_find_category_no_env_var_no_ports_tree(self):
        # - $PORTSDIR is not set
        # - There is no port tree in the default location
        with mock.patch('upt_freebsd.upt_freebsd.DEFAULT_PORTSDIR',
                        '/does/not/exist'):
            self.assertEqual(self.freebsd_pkg._find_category('py-requests'),
                             'XXX')

    def test_find_category_env_var_set(self):
        # - $PORTSDIR is set and points to a valid ports tree
        fake_environ = {'PORTSDIR': self.user_ports_dir.name}
        with mock.patch.dict(os.environ, fake_environ):
            self.assertEqual(self.freebsd_pkg._find_category('py-requests'),
                             'yyy')

    def test_find_category_env_var_set_no_ports_tree(self):
        # - $PORTSDIR is set and points to a directory that does not exist
        fake_environ = {'PORTSDIR': '/does/not/exist'}
        with mock.patch.dict(os.environ, fake_environ):
            self.assertEqual(self.freebsd_pkg._find_category('py-requests'),
                             'XXX')


if __name__ == '__main__':
    unittest.main()
