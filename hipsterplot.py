#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2014 Ian Horn <horn.imh@gmail.com> and
#                    Danilo J. S. Bellini <danilo.bellini@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import print_function, division
import math, random, sys
from operator import itemgetter

# Python 2.x and 3.x compatibility
if sys.version_info.major == 2:
    range = xrange
    from future_builtins import map, zip


CHAR_LOOKUP_SYMBOLS = [(0, ' '), # Should be sorted
                       (1, '.'),
                       (2, ':'),
                       #(3, '!'),
                       (4, '|'),
                       #(8, '+'),
                       (float("inf"), '#')]

def charlookup(num_chars):
    """ Character for the given amount of elements in the bin """
    return next(ch for num, ch in CHAR_LOOKUP_SYMBOLS if num_chars <= num)


def bin_generator(data, bin_ends):
    """ Yields a list for each bin """
    max_idx_end = len(bin_ends) - 1
    iends = enumerate(bin_ends)

    idx_end, value_end = next(iends)
    bin_data = []
    for el in sorted(data):
        while el >= value_end and idx_end != max_idx_end:
            yield bin_data
            bin_data = []
            idx_end, value_end = next(iends)
        bin_data.append(el)

    # Finish
    for unused in iends:
        yield bin_data
        bin_data = []
    yield bin_data


def enumerated_reversed(seq):
    """ A version of reversed(enumerate(seq)) that actually works """
    return zip(range(len(seq) - 1, -1, -1), reversed(seq))


def plot(y_vals, x_vals=None, num_x_chars=70, num_y_chars=15):
    """
    Plots the values given by y_vals. The x_vals values are the y indexes, by
    default, unless explicitly given. Pairs (x, y) are matched by the x_vals
    and y_vals indexes, so these must have the same length.

    The num_x_chars and num_y_chars inputs are respectively the width and
    height for the output plot to be printed, given in characters.
    """
    if x_vals is None:
        x_vals = list(range(len(y_vals)))
    elif len(x_vals) != len(y_vals):
        raise ValueError("x_vals and y_vals must have the same length")

    ymin = min(y_vals)
    ymax = max(y_vals)
    xmin = min(x_vals)
    xmax = max(x_vals)

    xbinwidth = (xmax - xmin) / num_x_chars
    y_bin_width = (ymax - ymin) / num_y_chars

    x_bin_ends = [(xmin + (i+1) * xbinwidth, 0) for i in range(num_x_chars)]
    y_bin_ends = [ymin + (i+1) * y_bin_width for i in range(num_y_chars)]

    columns_pairs = bin_generator(zip(x_vals, y_vals), x_bin_ends)
    yloop = lambda *args: [charlookup(len(el)) for el in bin_generator(*args)]
    ygetter = lambda iterable: map(itemgetter(1), iterable)
    columns = (yloop(ygetter(pairs), y_bin_ends) for pairs in columns_pairs)
    rows = list(zip(*columns))

    for idx, row in enumerated_reversed(rows):
        y_bin_mid = y_bin_ends[idx] - y_bin_width * 0.5
        print("{:10.4f} {}".format(y_bin_mid, "".join(row)))


if __name__ == '__main__':
    # Some examples
    ys = [math.cos(x/5.0) for x in range(180)]
    num_x_chars = min(70, len(ys))
    plot(ys, num_x_chars=num_x_chars, num_y_chars=15)

    xs = [50.0*random.random() for x in range(180)]
    ys = [math.cos(x/5.0) for x in xs]
    num_x_chars = min(70, len(ys))
    plot(ys, x_vals=xs, num_x_chars=num_x_chars, num_y_chars=15)

    k = 20
    ys = [random.gauss(0, 0.5) + math.cos(x/5.0/k) for x in range(180*k)]
    num_x_chars = min(160, len(ys))
    plot(ys, num_x_chars=num_x_chars, num_y_chars=25)