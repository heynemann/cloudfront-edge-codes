#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-edge-codes.
# https://github.com/heynemann/cloudfront-edge-codes

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from preggy import expect

from cloudfront_edge_codes import parse, NODES
from tests.base import TestCase


class ParseEdgeCodeTestCase(TestCase):
    def test_can_parse_code(self):
        result = parse("IAD2")
        expect(result).not_to_be_null()
        expect(result).to_be_instance_of(dict)

    def test_returns_null_if_invalid_code(self):
        result = parse("WTF4")
        expect(result).to_be_null()

        result = parse("")
        expect(result).to_be_null()

        result = parse("IAD")
        expect(result).to_be_null()


def can_validate_code(code, node_name, node_index):
    parsed_code = parse(code)
    expect(parsed_code).not_to_be_null()
    expect(parsed_code).to_be_instance_of(dict)
    expect(parsed_code['code']).to_equal(code)
    expect(parsed_code['name']).to_equal(node_name)
    expect(parsed_code['number']).to_equal(node_index)
    expect(parsed_code).to_include('reference')
    expect(parsed_code).to_include('city')
    expect(parsed_code).to_include('state')
    expect(parsed_code).to_include('country')


def test_can_return_all_codes():
    for node_name in NODES.keys():
        for node_index in range(50):
            yield can_validate_code, "%s%d" % (node_name, node_index), node_name, node_index
