# The MIT License (MIT)
#
# Copyright (c) 2014 Ian Horn <horn.imh@gmail.com>
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

import math
import random

def charlookup(num_chars):
    if num_chars <= 0:
        return ' '
    if num_chars <= 1:
        return '.'
    if num_chars <= 2:
        return ':'
    # if num_chars <= 3:
    #     return '!'
    if num_chars <= 4:
        return '|'
    # if num_chars <= 8:
    #     return '+'
    return '#'

def yloop(ys, num_y_chars, y_bin_ends):
    column = [' '] * num_y_chars
    ys.sort()
    ys.reverse()
    k = 0
    l = 0
    num_bin_ys = 0
    while (k < len(ys)):
        y = ys[k]
        if (l == len(y_bin_ends) or y >= y_bin_ends[l]):
            num_bin_ys += 1
            k += 1
        else:
            column[l] = charlookup(num_bin_ys)
            num_bin_ys = 0
            l += 1
    l_ = min(l, len(y_bin_ends)-1)
    column[l_] = charlookup(num_bin_ys)
    return column


def plot(y_vals, x_vals=None, num_x_chars=70, num_y_chars=15):
    if x_vals is None:
        x_vals = range(len(y_vals))
    else:
        if len(x_vals) != len(y_vals):
            raise Exception("x_vals and y_vals must be the same length")
        xy = list(zip(x_vals, y_vals))
        xy.sort(key=(lambda x: x[0]))
        _xy = zip(*xy)
        x_vals = list(_xy[0])
        y_vals = list(_xy[1])
    num_points = len(y_vals)

    ymin = min(y_vals)
    ymax = max(y_vals)
    xmin = min(x_vals)
    xmax = max(x_vals)

    xbinwidth = (xmax - xmin) / num_x_chars
    y_bin_width = (ymax - ymin) / num_y_chars

    x_bin_ends = [xmin + (i+1.0) * xbinwidth for i in xrange(num_x_chars)]
    y_bin_ends = [ymin + (i-1.0) * y_bin_width for i in xrange(num_y_chars,0,-1)]

    columns = [] #NOTE: could allocate the thing all at once, if performance were a consideration, but column[i][j]=foo set column[:][j] for some reason
    i = 0
    j = 0
    ys = []
    while (i < num_points):
        x = x_vals[i]
        if (j == len(x_bin_ends) or x < x_bin_ends[j]):
            ys.append(y_vals[i])
            i += 1
        else:
            columns.append(yloop(ys, num_y_chars, y_bin_ends))
            ys = []
            j += 1

    columns.append(yloop(ys, num_y_chars, y_bin_ends))

    for row, y_bin_end in enumerate(y_bin_ends):
        strout = ""
        y_bin_mid = y_bin_end + y_bin_width * 0.5
        strout += "{:10.4f}".format(y_bin_mid) + ' '
        for column in xrange(len(x_bin_ends)):
            strout += columns[column][row]
        print strout

if __name__ == '__main__':
    ys = [math.cos(x/5.0) for x in xrange(180)]
    num_x_chars = min(70, len(ys))
    plot(ys, num_x_chars=num_x_chars, num_y_chars=15)

    xs = [50.0*random.random() for x in xrange(180)]
    ys = [math.cos(x/5.0) for x in xs]
    num_x_chars = min(70, len(ys))
    plot(ys, x_vals=xs, num_x_chars=num_x_chars, num_y_chars=15)

    k = 20
    ys = [random.gauss(0, 0.5) + math.cos(x/5.0/k) for x in xrange(180*k)]
    num_x_chars = min(160, len(ys))
    plot(ys, num_x_chars=num_x_chars, num_y_chars=25)
