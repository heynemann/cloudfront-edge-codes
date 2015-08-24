# cloudfront-edge-codes

Cloudfront Edge Codes is a translator that returns information on the edge node based on its code.

## Where does this info come from?

I got the informaton from two different places:

* Edge nodes from this post at the [aws forums](https://forums.aws.amazon.com/thread.jspa?messageID=671690&#671690);
* Airport codes and geolocation from [this website](https://www.world-airport-codes.com/).

## Installing

    $ pip install cloudfront-edge-codes

## Usage

Using it is very simple:

```Python
    In [1]: from cloudfront_edge_codes import parse

    In [2]: edge_code = "IAD2"

    In [7]: print(parse(edge_code))
        {'city': 'Ashburn',
         'code': 'IAD2',
         'country': 'United States of America',
         'name': 'IAD',
         'number': 2,
         'reference': {'latitude': 38.9445,
                       'longitude': -77.4558029,
                       'name': 'Dulles International Airport'},
         'state': 'Virginia'}
```

## Which edge codes are supported?

You can verify that yourself with:

```Python
    In [1]: from cloudfront_edge_codes import NODES

    In [2]: print(sorted(NODES.keys()))
        ['AMS',
         'ARN',
         'CDG',
         'DFW',
         'DUB',
         'EWR',
         'FRA',
         'GRU',
         'HGK',
         'HKG',
         'IAD',
         'IND',
         'JAX',
         'JFK',
         'LAX',
         'LHR',
         'MIA',
         'MXP',
         'NRT',
         'SEA',
         'SFO',
         'SIN',
         'STL']
```

## There's a node missing!

Since I found it very hard to find an up-to-date list of edge codes from Amazon, I think this is as good as it gets.

If you find some code that's not here, do not hesitate to send a Pull Request adding it and we'll release a new version ASAP.

## Licensing

The MIT License (MIT)

Copyright (c) 2015 Bernardo Heynemann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
