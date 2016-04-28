#!/usr/bin/env python3
# coding: utf-8
# Lab 7 - Server API
# François Chalifour

humans = {
    1: {
        'name': 'Mud Pack',
        'age': 28
    },
    2: {
        'name': 'Able Crown',
        'age': 42
    },
    3: {
        'name': 'Marina Thonder',
        'age': 20
    }
}

human_not_found = {
    "error": {
        "code": 404,
        "message": "ID not found"
    }
}

commands = {
    'add': lambda val, op: val + op,
    'sub': lambda val, op: val - op,
    'mul': lambda val, op: val * op,
    'div': lambda val, op: val // op
}

resource_not_found = {
    "error": {
        "code": 404,
        "message": "Resource not found"
    }
}

missing_params = {
    "error": {
        "code": 404,
        "message": "Missing params"
    }
}

wrong_values = {
    "error": {
        "code": 404,
        "message": "Wrong values"
    }
}
