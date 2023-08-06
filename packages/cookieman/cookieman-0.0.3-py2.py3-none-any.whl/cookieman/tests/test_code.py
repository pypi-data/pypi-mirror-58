import re

import unittest_resources.testing as base


class Mixin:
    """Package mixin."""

    meta_module = 'cookieman'
    meta_module_pattern = re.compile(r'^([^t]*|t(?!ests?\.))+$')
    meta_resource_pattern = re.compile(r'^([^t]*|t(?!ests?))+\.py$')


class TypingTestCase(Mixin, base.TypingTestCase):
    """TestCase checking :module:`mypy`."""


class CodeStyleTestCase(Mixin, base.CodeStyleTestCase):
    """TestCase checking :module:`pycodestyle`."""


class DocStyleTestCase(Mixin, base.DocStyleTestCase):
    """TestCase checking :module:`pydocstyle`."""


class MaintainabilityIndexTestCase(Mixin, base.MaintainabilityIndexTestCase):
    """TestCase checking :module:`radon` maintainability index."""


class CodeComplexityTestCase(Mixin, base.CodeComplexityTestCase):
    """TestCase checking :module:`radon` code complexity."""

    max_class_complexity = 6
    max_function_complexity = 9
