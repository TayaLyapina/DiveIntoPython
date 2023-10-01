def get_dict(my_dict, key, default_value='None'):
    """
    >>> get_dict({1: 'one', 2: 'two', 3: 'three'}, 1, 1)
    'one'
    >>> get_dict({1: 'one', 2: 'two', 3: 'three'}, 'a')
    'None'
    >>> get_dict({1: 'one', 2: 'two', 3: 'three'}, 'two', 'Not Found')
    'Not Found'
    """
    try:
        return my_dict[key]
    except KeyError:
        return default_value
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)