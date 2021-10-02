#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init
from pybuilder.core import init

use_plugin('python.core')
use_plugin('python.unittest')
use_plugin('python.flake8')
use_plugin('python.coverage')
use_plugin('python.distutils')
use_plugin('pypi:pybuilder_radon')
use_plugin('pypi:pybuilder_bandit')
use_plugin('pypi:pybuilder_anybadge')

name = 'tfirmx'
version = '0.1.0'
default_task = [
    'clean',
    'analyze',
    'publish',
    'radon',
    'bandit',
    'anybadge'
]


@init
def set_properties(project):
    project.set_property('unittest_module_glob', 'test_*.py')
    project.set_property('coverage_break_build', False)
    project.set_property('flake8_max_line_length', 120)
    project.set_property('flake8_verbose_output', True)
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_include_scripts', True)
    project.set_property('flake8_include_test_sources', True)
    project.depends_on_requirements('requirements.txt')
    project.depends_on_requirements('requirements-build.txt')
    project.set_property('anybadge_add_to_readme', True)
    project.set_property('distutils_console_scripts', ['tfirmx = tfirmx.cli:main'])
    project.set_property('anybadge_use_shields', True)
