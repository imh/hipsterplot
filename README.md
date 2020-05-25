hipsterplot
===========

[![PyPI](https://img.shields.io/pypi/v/hipsterplot)](https://pypi.org/project/hipsterplot/)
[![PyPI - License](https://img.shields.io/pypi/l/hipsterplot)](https://opensource.org/licenses/MIT)

because matplotlib is too mainstream <sup><sup>(or you broke it like I did)</sup></sup>. Also good while debugging numerical code.

-----------------------------------

A python script for command line plotting. 

`pip install hipsterplot` is all you need.

Can plot a list of y values \[ys\] which works for evenly spaced points, or pairs of lists (\[xs\], \[ys\]) which works for heterogeneous x-spacing, or disorder in the x's (scatterplots).

In a given 'pixel', the plotted character depends how many data points map to it, so it can look good on densities.

for example:

![alt tag](http://i.imgur.com/uTySFPA.png)

also looks good on noisy data and plots of non-functions:

![alt tag](http://i.imgur.com/cedrFqR.png)

More examples in the main function of hipsterplot.py.
