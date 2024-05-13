#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
from typing import Any, Dict, Mapping, Sequence
from unittest.mock import Mock, patch

import utils


class TestAccessNestedMap(unittest.TestCase):
    """unittest for access_nested_map function"""

    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ) -> None:
        """Base test cases"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
