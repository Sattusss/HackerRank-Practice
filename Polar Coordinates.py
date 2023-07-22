import math

def polarCoordinates(complexNumber):
    return (abs(complexNumber), math.atan2(complexNumber.imag, complexNumber.real))

if __name__ == '__main__':
    complexNumber = complex(input().strip())
    print(*polarCoordinates(complexNumber), sep='\n')
