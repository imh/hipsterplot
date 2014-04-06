import math

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

def plot(y_vals, num_xchars, num_ychars):
    xvals = range(len(y_vals))

    num_points = len(y_vals)

    ymin = min(y_vals)
    ymax = max(y_vals)
    xmin = 0.0
    xmax = max(len(y_vals)-1.0, 0.0)

    #figure out the boundaries between each bin on x and y
    xbinwidth = (xmax - xmin) / num_xchars
    y_bin_width = (ymax - ymin) / num_ychars

    x_bin_ends = [xmin + (i+1.0) * xbinwidth for i in xrange(num_xchars)]
    y_bin_ends = [ymin + (i+0.0) * y_bin_width for i in xrange(num_ychars)]
    y_bin_ends.reverse()

    #allocate the bins
    chars = [[' '] * num_ychars] * num_xchars
    columns = []

    i = 0
    j = 0
    x_bin_end = x_bin_ends[0]
    ys = []
    while (i < num_points):
        x = xvals[i]
        if (j == len(x_bin_ends) or x < x_bin_ends[j]):
            ys.append(y_vals[i])
            i += 1
        else:
            column = [' '] * num_ychars
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
                    # chars[j][l] = charlookup(num_bin_ys)
                    column[l] = charlookup(num_bin_ys)
                    num_bin_ys = 0
                    l += 1
            l_ = min(l, len(y_bin_ends)-1)
            column[l_] = charlookup(num_bin_ys)
            columns.append(column)
            ys = []
            j += 1
    column = [' '] * num_ychars
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
            # chars[j][l] = charlookup(num_bin_ys)
            column[l] = charlookup(num_bin_ys)
            num_bin_ys = 0
            l += 1
    l_ = min(l, len(y_bin_ends)-1)
    column[l_] = charlookup(num_bin_ys)
    columns.append(column)
    ys = []
    j += 1

    for row, y_bin_end in enumerate(y_bin_ends):
        strout = ""
        y_bin_mid = y_bin_end + y_bin_width * 0.5
        strout += "{:10.4f}".format(y_bin_mid) + ' '
        for column in xrange(len(x_bin_ends)):
            strout += columns[column][row]
        # strout = ""
        # for column in row:
        #     strout += column
        print strout

if __name__ == '__main__':
    ys = [math.cos(x/5.0) for x in xrange(180)]
    num_x_chars = min(70, len(ys))
    plot(ys, num_x_chars, 15)
