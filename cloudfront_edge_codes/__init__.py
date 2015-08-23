#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudfront-edge-codes.
# https://github.com/heynemann/cloudfront-edge-codes

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Bernardo Heynemann <heynemann@gmail.com>

from cloudfront_edge_codes.version import __version__  # NOQA


# LAT/LONG values retrieved from https://www.world-airport-codes.com
NODES = {
    'IAD2': {
        'reference': {
            'name': 'Dulles International Airport',
            'latitude': 38.9445,
            'longitude': -77.4558029,
        },
        'edge_number': 2,
        'city': 'Ashburn',
        'state': 'Virginia',
        'country': 'United States of America',
    },

    'DFW3': {
        'reference': {
            'name': 'Dallas Fort Worth International Airport',
            'latitude': 32.896801,
            'longitude': -97.038002,
        },
        'edge_number': 3,
        'city': 'Dallas',
        'state': 'Texas',
        'country': 'United States of America',
    },

    'JAX1': {
        'reference': {
            'name': 'Jacksonville International Airport',
            'latitude': 30.4941006,
            'longitude': -81.6878967,
        },
        'edge_number': 3,
        'city': 'Jacksonville',
        'state': 'Florida',
        'country': 'United States of America',
    },

    'lax1': {
        'reference': {
            'name': 'los angeles international airport',
            'latitude': 33.9425011,
            'longitude': -118.4079971,
        },
        'edge_number': 1,
        'city': 'Los Angeles',
        'state': 'California',
        'country': 'United States of America',
    },

    'LAX3': {
        'reference': {
            'name': 'Los Angeles International Airport',
            'latitude': 33.9425011,
            'longitude': -118.4079971,
        },
        'edge_number': 3,
        'city': 'Los Angeles',
        'state': 'California',
        'country': 'United States of America',
    },

    'MIA3': {
        'reference': {
            'name': 'Miami International Airport',
            'latitude': 25.7931995,
            'longitude': -80.2906036,
        },
        'edge_number': 3,
        'city': 'Miami',
        'state': 'Florida',
        'country': 'United States of America',
    },

    'JFK1': {
        'reference': {
            'name': 'John F Kennedy International Airport',
            'latitude': 40.639801,
            'longitude': -73.7789002,
        },
        'edge_number': 1,
        'city': 'New York City',
        'state': 'New York',
        'country': 'United States of America',
    },

    'JFK5': {
        'reference': {
            'name': 'John F Kennedy International Airport',
            'latitude': 40.639801,
            'longitude': -73.7789002,
        },
        'edge_number': 5,
        'city': 'New York City',
        'state': 'New York',
        'country': 'United States of America',
    },

    'EWR2': {
        'reference': {
            'name': 'Newark Liberty International Airport',
            'latitude': 40.6925011,
            'longitude': -74.1687012,
        },
        'edge_number': 2,
        'city': 'Newark',
        'state': 'New Jersey',
        'country': 'United States of America',
    },

    'SFO4': {
        'reference': {
            'name': 'San Francisco International Airport',
            'latitude': 37.6189995,
            'longitude': -122.375,
        },
        'edge_number': 4,
        'city': 'Palo Alto',
        'state': 'California',
        'country': 'United States of America',
    },

    'SFO5': {
        'reference': {
            'name': 'San Francisco International Airport',
            'latitude': 37.6189995,
            'longitude': -122.375,
        },
        'edge_number': 5,
        'city': 'San Jose',
        'state': 'California',
        'country': 'United States of America',
    },

    'SEA4': {
        'reference': {
            'name': 'Seattle Tacoma International Airport',
            'latitude': 47.4490013,
            'longitude': -122.3089981,
        },
        'edge_number': 4,
        'city': 'Seattle',
        'state': 'Washington',
        'country': 'United States of America',
    },

    'IND6': {
        'reference': {
            'name': 'Indianapolis International Airport',
            'latitude': 39.7173004,
            'longitude': -86.2944031,
        },
        'edge_number': 6,
        'city': 'South Bend',
        'state': 'Indiana',
        'country': 'United States of America',
    },

    'STL2': {
        'reference': {
            'name': 'Lambert St Louis International Airport',
            'latitude': 38.7486992,
            'longitude': -90.3700027,
        },
        'edge_number': 2,
        'city': 'Saint Louis',
        'state': 'Missouri',
        'country': 'United States of America',
    },

    'AMS1': {
        'reference': {
            'name': 'Amsterdam Schiphol Airport',
            'latitude': 52.3086014,
            'longitude': 4.7638898,
        },
        'edge_number': 1,
        'city': 'Amsterdam',
        'state': '',
        'country': 'Netherlands',
    },

    'DUB2': {
        'reference': {
            'name': 'Dublin Airport',
            'latitude': 53.421299,
            'longitude': -6.2700701,
        },
        'edge_number': 2,
        'city': 'Dublin',
        'state': '',
        'country': 'Ireland',
    },

    'FRA2': {
        'reference': {
            'name': 'Frankfurt am Main International Airport',
            'latitude': 50.0264015,
            'longitude': 8.5431299,
        },
        'edge_number': 2,
        'city': 'Frankfurt',
        'state': '',
        'country': 'Germany',
    },

    'LHR3': {
        'reference': {
            'name': 'London Heathrow Airport',
            'latitude': 51.4706001,
            'longitude': -0.461941,
        },
        'edge_number': 3,
        'city': 'London',
        'state': '',
        'country': 'United Kingdom',
    },

    'MXP4': {
        'reference': {
            'name': 'Malpensa International Airport',
            'latitude': 45.6306,
            'longitude': 8.7281103,
        },
        'edge_number': 4,
        'city': 'Milan',
        'state': '',
        'country': 'Italy',
    },

    'CDG3': {
        'reference': {
            'name': 'Charles de Gaulle International Airport',
            'latitude': 49.0127983,
            'longitude': 2.55,
        },
        'edge_number': 3,
        'city': 'Paris',
        'state': '',
        'country': 'France',
    },

    'ARN1': {
        'reference': {
            'name': 'Stockholm-Arlanda Airport',
            'latitude': 59.6519012,
            'longitude': 17.9186001,
        },
        'edge_number': 1,
        'city': 'Stockholm',
        'state': '',
        'country': 'Sweden',
    },

    'HGK1': {
        'reference': {
            'name': 'Hong Kong International Airport',
            'latitude': 22.3288002,
            'longitude': 114.1940002,
        },
        'edge_number': 1,
        'city': 'Hong Kong',
        'state': '',
        'country': 'Hong Kong',
    },

    'HKG1': {  # This is the real code for the airport
        'reference': {
            'name': 'Hong Kong International Airport',
            'latitude': 22.3288002,
            'longitude': 114.1940002,
        },
        'edge_number': 1,
        'city': 'Hong Kong',
        'state': '',
        'country': 'Hong Kong',
    },

    'NRT52': {
        'reference': {
            'name': 'Narita International Airport',
            'latitude': 35.7647018,
            'longitude': 140.3860016,
        },
        'edge_number': 52,
        'city': 'Osaka',
        'state': '',
        'country': 'Japan',
    },


    'NRT4': {
        'reference': {
            'name': 'Narita International Airport',
            'latitude': 35.7647018,
            'longitude': 140.3860016,
        },
        'edge_number': 4,
        'city': 'Tokyo',
        'state': '',
        'country': 'Japan',
    },

    'SIN2': {
        'reference': {
            'name': 'Singapore Changi International Airport',
            'latitude': 1.35019,
            'longitude': 103.9940033,
        },
        'edge_number': 2,
        'city': 'Singapore',
        'state': '',
        'country': 'Singapore',
    },

    'GRU1': {
        'reference': {
            'name': u'Guarulhos - Governador André Franco Montoro International Airport',
            'latitude': -23.4355564,
            'longitude': -46.4730568,
        },
        'edge_number': 1,
        'city': 'Sao Paulo',
        'state': 'Sao Paulo',
        'country': 'Brazil',
    },

}


def parse(code):
    node = NODES.get(code, None)

    if node is None:
        return None

    return_node = {}
    node.update(return_node)
    return_node['code'] = code

    return return_node
