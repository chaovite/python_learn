# This exercise pratices building a class and some simple methods.
# implement a fraction class and overload several python built in methods.
class Fraction:
    def __init__(self, num, den):
        gcd_1    = gcd(num, den)
        self.num = num/gcd_1
        self.den = den/gcd_1
        
    def __str__(self):
        return '%d/%d'%(self.num,self.den)

    def __add__(self, f2):
        num      = self.num*f2.den + self.den*f2.num
        den      = self.den*f2.den
        new_frac = Fraction(num, den)
        return new_frac
    def __eq__(self, f2):
        return self.num*f2.den==self.den*f2.num
    
    def __sub__(self, f2):
        return Fraction(self.num*f2.den-self.den*f2.num, self.den*f2.den)
    
    def __mul__(self, f2):
        return Fraction(self.num*f2.num, self.den*f2.den)

def gcd(n1, n2):
    """Find the greatest common divider"""
    n1 = abs(n1)
    n2 = abs(n2)
    n_small = n1
    n_large = n2
    if n1 > n2:
        n_small = n2
        n_large = n1
    if n_large%n_small == 0:
        return n_small
    else:
        return gcd(n_small, n_large%n_small)

def main():
    myf = Fraction(-2,4)
    print(myf)
    f1 = Fraction(2,4)
    f2 = Fraction(2,3)
    print(f1+f2)
    print(f1==f2)
    print(Fraction(2,3) - Fraction(1,2))

main()


