from math import gcd

def LCM(a, b): 
    return a // gcd(a, b) * b

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        lcm_result = 1
        for i in range(2, n+1):
            lcm_result = LCM(lcm_result, i)
        print(lcm_result)
