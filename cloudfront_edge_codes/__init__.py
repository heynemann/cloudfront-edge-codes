#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-edge-codes.
# https://github.com/heynemann/cloudfront-edge-codes

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from cloudfront_edge_codes.version import __version__  # NOQA


# EDGE Codes retrieved from https://forums.aws.amazon.com/thread.jspa?messageID=671690&#671690
# LAT/LONG values retrieved from https://www.world-airport-codes.com
NODES = {
    'IAD': {
        'reference': {
            'name': 'Dulles International Airport',
            'latitude': 38.9445,
            'longitude': -77.4558029,
        },
        'city': 'Ashburn',
        'state': 'Virginia',
        'country': 'United States of America',
    },

    'DFW': {
        'reference': {
            'name': 'Dallas Fort Worth International Airport',
            'latitude': 32.896801,
            'longitude': -97.038002,
        },
        'city': 'Dallas',
        'state': 'Texas',
        'country': 'United States of America',
    },

    'JAX': {
        'reference': {
            'name': 'Jacksonville International Airport',
            'latitude': 30.4941006,
            'longitude': -81.6878967,
        },
        'city': 'Jacksonville',
        'state': 'Florida',
        'country': 'United States of America',
    },

    'LAX': {
        'reference': {
            'name': 'los angeles international airport',
            'latitude': 33.9425011,
            'longitude': -118.4079971,
        },
        'city': 'Los Angeles',
        'state': 'California',
        'country': 'United States of America',
    },

    'MIA': {
        'reference': {
            'name': 'Miami International Airport',
            'latitude': 25.7931995,
            'longitude': -80.2906036,
        },
        'city': 'Miami',
        'state': 'Florida',
        'country': 'United States of America',
    },

    'JFK': {
        'reference': {
            'name': 'John F Kennedy International Airport',
            'latitude': 40.639801,
            'longitude': -73.7789002,
        },
        'city': 'New York City',
        'state': 'New York',
        'country': 'United States of America',
    },

    'EWR': {
        'reference': {
            'name': 'Newark Liberty International Airport',
            'latitude': 40.6925011,
            'longitude': -74.1687012,
        },
        'city': 'Newark',
        'state': 'New Jersey',
        'country': 'United States of America',
    },

    'SFO': {
        'reference': {
            'name': 'San Francisco International Airport',
            'latitude': 37.6189995,
            'longitude': -122.375,
        },
        'city': 'Palo Alto',
        'state': 'California',
        'country': 'United States of America',
    },

    'SEA': {
        'reference': {
            'name': 'Seattle Tacoma International Airport',
            'latitude': 47.4490013,
            'longitude': -122.3089981,
        },
        'city': 'Seattle',
        'state': 'Washington',
        'country': 'United States of America',
    },

    'IND': {
        'reference': {
            'name': 'Indianapolis International Airport',
            'latitude': 39.7173004,
            'longitude': -86.2944031,
        },
        'city': 'South Bend',
        'state': 'Indiana',
        'country': 'United States of America',
    },

    'STL': {
        'reference': {
            'name': 'Lambert St Louis International Airport',
            'latitude': 38.7486992,
            'longitude': -90.3700027,
        },
        'city': 'Saint Louis',
        'state': 'Missouri',
        'country': 'United States of America',
    },

    'AMS': {
        'reference': {
            'name': 'Amsterdam Schiphol Airport',
            'latitude': 52.3086014,
            'longitude': 4.7638898,
        },
        'city': 'Amsterdam',
        'state': '',
        'country': 'Netherlands',
    },

    'DUB': {
        'reference': {
            'name': 'Dublin Airport',
            'latitude': 53.421299,
            'longitude': -6.2700701,
        },
        'city': 'Dublin',
        'state': '',
        'country': 'Ireland',
    },

    'FRA': {
        'reference': {
            'name': 'Frankfurt am Main International Airport',
            'latitude': 50.0264015,
            'longitude': 8.5431299,
        },
        'city': 'Frankfurt',
        'state': '',
        'country': 'Germany',
    },

    'LHR': {
        'reference': {
            'name': 'London Heathrow Airport',
            'latitude': 51.4706001,
            'longitude': -0.461941,
        },
        'city': 'London',
        'state': '',
        'country': 'United Kingdom',
    },

    'MXP': {
        'reference': {
            'name': 'Malpensa International Airport',
            'latitude': 45.6306,
            'longitude': 8.7281103,
        },
        'city': 'Milan',
        'state': '',
        'country': 'Italy',
    },

    'CDG': {
        'reference': {
            'name': 'Charles de Gaulle International Airport',
            'latitude': 49.0127983,
            'longitude': 2.55,
        },
        'city': 'Paris',
        'state': '',
        'country': 'France',
    },

    'ARN': {
        'reference': {
            'name': 'Stockholm-Arlanda Airport',
            'latitude': 59.6519012,
            'longitude': 17.9186001,
        },
        'city': 'Stockholm',
        'state': '',
        'country': 'Sweden',
    },

    'HGK': {
        'reference': {
            'name': 'Hong Kong International Airport',
            'latitude': 22.3288002,
            'longitude': 114.1940002,
        },
        'city': 'Hong Kong',
        'state': '',
        'country': 'Hong Kong',
    },

    'HKG': {  # This is the real code for the airport
        'reference': {
            'name': 'Hong Kong International Airport',
            'latitude': 22.3288002,
            'longitude': 114.1940002,
        },
        'city': 'Hong Kong',
        'state': '',
        'country': 'Hong Kong',
    },

    'NRT': {
        'reference': {
            'name': 'Narita International Airport',
            'latitude': 35.7647018,
            'longitude': 140.3860016,
        },
        'city': 'Osaka',
        'state': '',
        'country': 'Japan',
    },


    'NRT': {
        'reference': {
            'name': 'Narita International Airport',
            'latitude': 35.7647018,
            'longitude': 140.3860016,
        },
        'city': 'Tokyo',
        'state': '',
        'country': 'Japan',
    },

    'SIN': {
        'reference': {
            'name': 'Singapore Changi International Airport',
            'latitude': 1.35019,
            'longitude': 103.9940033,
        },
        'city': 'Singapore',
        'state': '',
        'country': 'Singapore',
    },

    'GRU': {
        'reference': {
            'name': u'Guarulhos - Governador André Franco Montoro International Airport',
            'latitude': -23.4355564,
            'longitude': -46.4730568,
        },
        'city': 'Sao Paulo',
        'state': 'Sao Paulo',
        'country': 'Brazil',
    },

}


def parse(code):
    if not code or len(code) < 4:
        return None

    node_name = code[:3]
    node_number = int(code[3:])
    node = NODES.get(node_name, None)

    if node is None:
        return None

    return_node = {}
    return_node.update(node)
    return_node['code'] = code
    return_node['name'] = node_name
    return_node['number'] = node_number

    return return_node
