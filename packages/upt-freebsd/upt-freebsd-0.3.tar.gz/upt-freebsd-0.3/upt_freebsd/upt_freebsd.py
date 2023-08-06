# Copyright 2018      Cyril Roelandt
#
# Licensed under the 3-clause BSD license. See the LICENSE file.
import glob
import logging
import os
import subprocess
import sys

import jinja2
import upt


DEFAULT_PORTSDIR = '/usr/ports'
logger = logging.getLogger('upt')


class FreeBSDPackage(object):
    default_maintainer = 'XXX'
    pkgnameprefix = ''  # PKGNAMEPREFIX in the FreeBSD ports

    def __init__(self, upt_pkg, output_dir):
        self.upt_pkg = upt_pkg
        self.summary = self._fix_summary(upt_pkg.summary)
        if output_dir is None:
            self.output_dir = os.getcwd()
        else:
            self.output_dir = os.path.expanduser(output_dir)

    def create(self):
        self._setup_jinja2()
        self._create_output_directory()
        self._create_makefile()
        self._create_pkg_descr()
        self._create_distinfo()

    def _setup_jinja2(self):
        self.env = jinja2.Environment(
            loader=jinja2.PackageLoader('upt_freebsd', 'templates'),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )
        self.env.filters['reqformat'] = self.jinja2_reqformat

    @staticmethod
    def _fix_summary(summary):
        while summary.endswith('.') or summary.endswith(' '):
            summary = summary[:-1]
        if not summary:
            return summary
        if summary[0].islower():
            summary = summary[0].upper() + summary[1:]
        return summary

    def directory_name(self, pkgname):
        """Return the name of the directory where the port shall live.

        Example: if the user enters the following command:

            $ upt package -f pypi -b freebsd -o /usr/ports/www requests

        Then "directory_name('requests')" will be called and shall return:

            'py-requests'

        And the following directory will be created:

            /usr/ports/www/py-requests
        """
        return f'{self.pkgnameprefix}{pkgname}'

    def _create_output_directory(self):
        """Creates the directory layout required to port upt_pkg."""
        self.output_dir = os.path.join(self.output_dir,
                                       self.directory_name(self.upt_pkg.name))
        logger.info(f'Creating {self.output_dir}')
        try:
            os.makedirs(self.output_dir)
        except PermissionError:
            sys.exit(f'Cannot create {self.output_dir}: permission denied.')
        except FileExistsError:
            sys.exit(f'Cannot create {self.output_dir}: already exists.')

    def _create_makefile(self):
        makefile_path = os.path.join(self.output_dir, 'Makefile')
        logger.info(f'Creating {makefile_path}')
        with open(makefile_path, 'w', encoding='utf-8') as f:
            template = self.env.get_template(self.template)
            f.write(template.render(pkg=self))

    def _create_pkg_descr(self):
        pkg_descr_path = os.path.join(self.output_dir, 'pkg-descr')
        logger.info(f'Creating {pkg_descr_path}')
        with open(pkg_descr_path, 'w', encoding='utf-8') as f:
            template = self.env.get_template('pkg-descr')
            f.write(template.render(pkg=self))

    def _create_distinfo(self):
        path = os.path.join(self.output_dir, 'distinfo')
        logger.info(f'Creating {path}')
        try:
            subprocess.check_call(['make', '-C', self.output_dir, 'makesum'])
        except Exception:
            logger.warning(f'make makesum failed. Not generating {path}')

    def __getattribute__(self, name):
        if name in ['homepage', 'version']:
            return self.upt_pkg.__getattribute__(name)
        else:
            return object.__getattribute__(self, name)

    @property
    def categories(self):
        valid_freebsd_categories = [
            'accessibility', 'arabic', 'archivers', 'astro',
            'audio', 'base', 'benchmarks', 'biology',
            'cad', 'chinese', 'comms', 'converters',
            'databases', 'deskutils', 'devel', 'dns',
            'editors', 'emulators', 'finance', 'french',
            'ftp', 'games', 'german', 'graphics',
            'hebrew', 'hungarian', 'irc', 'japanese',
            'java', 'Keywords', 'korean', 'lang',
            'mail', 'math', 'misc', 'multimedia',
            'net', 'net-im', 'net-mgmt', 'net-p2p',
            'news', 'palm', 'polish', 'ports-mgmt',
            'portuguese', 'print', 'russian', 'science',
            'security', 'shells', 'sysutils', 'Templates',
            'textproc', 'Tools', 'ukrainian', 'vietnamese',
            'www', 'x11', 'x11-clocks', 'x11-drivers',
            'x11-fm', 'x11-fonts', 'x11-servers', 'x11-themes',
            'x11-toolkits', 'x11-wm',
        ]
        try:
            _, main_category, _ = self.output_dir.rsplit('/', 2)
            if main_category not in valid_freebsd_categories:
                raise ValueError
        except ValueError:
            main_category = 'XXX'

        try:
            return [main_category, self.language_category]
        except AttributeError:
            return [main_category]

    @staticmethod
    def _find_category(directory_name):
        ports_dir = os.getenv('PORTSDIR', DEFAULT_PORTSDIR)
        try:
            category = glob.glob(os.path.join(ports_dir, '*', directory_name))
            return category[0].rsplit('/', 2)[-2]
        except IndexError:
            return 'XXX'

    def jinja2_reqformat(self, req):
        formatted = f'{self.pkgnameprefix}{req.name}{req.specifier or ">0"}'
        formatted += f':{self._find_category(self.directory_name(req.name))}/'
        formatted += f'{self.pkgnameprefix}{req.name}'
        return formatted

    @property
    def licenses(self):
        spdx2freebsd = {
            'AGPL-3.0': 'AGPLv3',
            'Artistic-1.0': 'ART10',
            'Artistic-2.0': 'ART20',
            'Apache-1.0': 'APACHE10',
            'Apache-1.1': 'APACHE11',
            'Apache-2.0': 'APACHE20',
            'BSL-1.0': 'BSL',
            'BSD-2-Clause': 'BSD2CLAUSE',
            'BSD-3-Clause': 'BSD3CLAUSE',
            'BSD-4-Clause': 'BSD4CLAUSE',
            'ClArtistic': 'ClArtistic',
            'CC0-1.0': 'CC0-1.0',
            'CC-BY-NC-SA-2.0': 'CC-BY-NC-SA-2.0',
            'CC-BY-NC-SA-2.5': 'CC-BY-NC-SA-2.5',
            'CC-BY-NC-SA-3.0': 'CC-BY-NC-SA-3.0',
            'CC-BY-NC-SA-4.0': 'CC-BY-NC-SA-4.0',
            'CC-BY-ND-3.0': 'CC-BY-ND-3.0',
            'CC-BY-SA-2.5': 'CC-BY-SA-2.5',
            'CC-BY-3.0': 'CC-BY-3.0',
            'CC-BY-SA-3.0': 'CC-BY-SA-3.0',
            'CC-BY-4.0': 'CC-BY-4.0',
            'CC-BY-SA-4.0': 'CC-BY-4.0',
            'CDDL-1.0': 'CDDL',
            'EPL-1.0': 'EPL',
            'EPL-2.0': 'EPL',
            'GFDL-1.2': 'GFDL',
            'GFDL-1.3': 'GFDL',
            'GPL-1.0': 'GPLv1',
            'GPL-1.0+': 'GPLv1+',
            'GPL-2.0': 'GPLv2',
            'GPL-2.0+': 'GPLv2+',
            'GPL-3.0': 'GPLv3',
            'GPL-3.0+': 'GPLv3+',
            'ISC': 'ISCL',
            'LGPL-2.0': 'LGPL20',
            'LGPL-2.0+': 'LGPL20+',
            'LGPL-2.1': 'LGPL21',
            'LGPL-2.1+': 'LGPL21+',
            'LGPL-3.0': 'LGPL3',
            'LGPL-3.0+': 'LGPL3+',
            'LPPL-1.2': 'LPPL12',
            'LPPL-1.3c': 'LPPL13c',
            'MIT': 'MIT',
            'MPL-1.0': 'MPL10',
            'MPL-1.1': 'MPL11',
            'MPL-2.0': 'MPL20',
            'NCSA': 'NSCA',
            'OFL-1.1': 'OFL11',
            'OpenSSL': 'OpenSSL',
            'PHP-3.01': 'PHP301',
            'PostgreSQL': 'PostgreSQL',
            'Python-2.0': 'PSFL',
            'Ruby': 'RUBY',
            'WTFPL': 'WTFPL',
            'Zlib': 'ZLIB',
            'ZPL-2.1': 'ZPL21'
        }

        return ' '.join([spdx2freebsd.get(upt_license.spdx_identifier, 'XXX')
                         for upt_license in self.upt_pkg.licenses])

    @property
    def maintainer(self):
        # TODO: use ~/.porttools if it exists.
        return self.default_maintainer

    @property
    def portname(self):
        return self.upt_pkg.name

    def _depends(self, phase):
        return self.upt_pkg.requirements.get(phase, [])

    @property
    def build_depends(self):
        return self._depends('build')

    @property
    def run_depends(self):
        return self._depends('run')

    @property
    def test_depends(self):
        return self._depends('test')


class FreeBSDCranPackage(FreeBSDPackage):
    template = 'cran.mk'
    pkgnameprefix = 'R-cran-'


class FreeBSDPerlPackage(FreeBSDPackage):
    template = 'perl.mk'
    default_maintainer = 'perl@FreeBSD.org'
    master_sites = 'CPAN'
    language_category = 'perl5'
    pkgnameprefix = 'p5-'


class FreeBSDPythonPackage(FreeBSDPackage):
    template = 'python.mk'
    default_maintainer = 'python@FreeBSD.org'
    master_sites = 'CHEESESHOP'
    language_category = 'python'
    pkgnameprefix = '${PYTHON_PKGNAMEPREFIX}'

    def directory_name(self, pkgname):
        return f'py-{pkgname}'

    def jinja2_reqformat(self, req):
        formatted = super().jinja2_reqformat(req)
        formatted = formatted.replace(self.pkgnameprefix, 'py-')
        formatted = formatted.replace('py-', self.pkgnameprefix, 1)
        return formatted + '@${PY_FLAVOR}'


class FreeBSDRubyPackage(FreeBSDPackage):
    template = 'ruby.mk'
    default_maintainer = 'ruby@FreeBSD.org'
    master_sites = 'RG'
    language_category = 'rubygems'
    pkgnameprefix = 'rubygem-'


class FreeBSDBackend(upt.Backend):
    name = 'freebsd'

    def create_package(self, upt_pkg, output=None):
        pkg_classes = {
            'cran': FreeBSDCranPackage,
            'cpan': FreeBSDPerlPackage,
            'pypi': FreeBSDPythonPackage,
            'rubygems': FreeBSDRubyPackage,
        }

        try:
            pkg_cls = pkg_classes[upt_pkg.frontend]
        except KeyError:
            raise upt.UnhandledFrontendError(self.name, upt_pkg.frontend)

        freebsd_pkg = pkg_cls(upt_pkg, output)
        freebsd_pkg.create()
