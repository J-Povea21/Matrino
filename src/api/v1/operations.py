import sage.all as sage

def add(a: float, b: float) -> float:
    return float(sage.RealNumber(a) + sage.RealNumber(b))

def subtract(a: float, b: float) -> float:
    return float(sage.RealNumber(a) - sage.RealNumber(b))

def multiply(a: float, b: float) -> float:
    return float(sage.RealNumber(a) * sage.RealNumber(b))

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    
    return float(sage.RealNumber(a) / sage.RealNumber(b))