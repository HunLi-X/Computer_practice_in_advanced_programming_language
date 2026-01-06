#测试用例，验证numpy库安装是否成功
from numpy import arange
help(arange)

#测试indices = np.arange(len(record.seq) - window_size) + 300
print(arange(10))     #显示[0 1 2 3 4 5 6 7 8 9]
indices =arange(10)+300
print(indices) #显示[300 301 302 303 304 305 306 307 308 309]
print(type(arange(10))) #显示<class 'numpy.ndarray'>
print(type(indices))    #显示<class 'numpy.ndarray'>
print(arange(5,10,2))     #显示[5,7,9]
print(arange(5,10,2)+10)     #显示[15,17,19]
'''
Help on built-in内置 function函数 arange in module numpy:

arange(...)
    arange([start,] stop[, step,], dtype数据类型=None)
    
    Return evenly spaced values within a given interval.
    
    Values are generated within the half-open interval ``[start, stop)``
    (in other words, the interval including `start` but excluding `stop`).
    For integer arguments the function is equivalent to the Python built-in
    `range` function, but returns an ndarray rather than a list.
    
    When using a non-integer step, such as 0.1, the results will often not
    be consistent.  It is better to use `numpy.linspace` for these cases.
    
    Parameters
    ----------
    start : number, optional
        Start of interval.  The interval includes this value.  The default
        start value is 0.
    stop : number
        End of interval.  The interval does not include this value, except
        in some cases where `step` is not an integer and floating point
        round-off affects the length of `out`.
    step : number, optional
        Spacing between values.  For any output `out`, this is the distance
        between two adjacent values, ``out[i+1] - out[i]``.  The default
        step size is 1.  If `step` is specified as a position argument,
        `start` must also be given.
    dtype : dtype
        The type of the output array.  If `dtype` is not given, infer the data
        type from the other input arguments.
    
    Returns
    -------
    arange : ndarray
        Array of evenly spaced values.
    
        For floating point arguments, the length of the result is
        ``ceil((stop - start)/step)``.  Because of floating point overflow,
        this rule may result in the last element of `out` being greater
        than `stop`.
    
    See Also
    --------
    numpy.linspace : Evenly spaced numbers with careful handling of endpoints.
    numpy.ogrid: Arrays of evenly spaced numbers in N-dimensions.
    numpy.mgrid: Grid-shaped arrays of evenly spaced numbers in N-dimensions.
    
    Examples
    --------
    >>> np.arange(3)
    array([0, 1, 2])
    >>> np.arange(3.0)
    array([ 0.,  1.,  2.])
    >>> np.arange(3,7)
    array([3, 4, 5, 6])
    >>> np.arange(3,7,2)
    array([3, 5])

[Finished in 0.5s]
'''
