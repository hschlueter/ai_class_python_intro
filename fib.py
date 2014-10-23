def fibbonacci(n):
    """
    The n-th Fibbonacci number is the sum of the previous two fibbonacci
    numbers where the first and second Fibbonacci number are 1.

    :math: F_n = F_{n-1} + F_{n-2}

    Examples:
    ---------
    >>> fibbonacci(1)
    1
    >>> fibbonacci(2)
    1
    >>> fibbonacci(3)
    2
    >>> fibbonacci(4)
    3
    >>> fibbonacci(5)
    5
    >>> fibbonacci(6)
    8

    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)
