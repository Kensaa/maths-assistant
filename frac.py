class Number:
    def __init__(self,num:int,den=1):
        assert den != 0, "denominator is 0"
        self.num = num
        self.den = den
    
    def simplify(self):
        #simplify fraction
        return self
    
    def __eq__(self, other) -> bool:
        if isinstance(other,int):
            other = Number(other)
        return self.num*other.den == self.den*other.num

    def __lt__(self, other) -> bool:
        if isinstance(other,int):
            other = Number(other)
        return self.num*other.den - other.num*self.den < 0

    def __gt__(self, other) -> bool:
        if isinstance(other,int):
            other = Number(other)
        return self.num*other.den - other.num*self.den > 0

    def __le__(self, other) -> bool:
        if isinstance(other,int):
            other = Number(other)
        return self.num*other.den - other.num*self.den <= 0
    
    def __ge__(self, other) -> bool:
        if isinstance(other,int):
            other = Number(other)
        return self.num*other.den - other.num*self.den >= 0
    
    def __ne__(self, other) -> bool:
        if isinstance(other,int):
            other = Number(other)
        return self.num*other.den != self.den*other.num
    
    def __add__(self, other):
        if isinstance(other,int):
            other = Number(other)
        return Number(self.num*other.den+other.num*self.den,self.den*other.den).simplify()
    
    def __sub__(self, other):
        if isinstance(other,int):
            other = Number(other)
        return Number(self.num*other.den-other.num*self.den,self.den*other.den).simplify()
    
    def __mul__(self, other):
        if isinstance(other,int):
            other = Number(other)
        return Number(self.num*other.num, self.den*other.den).simplify()
    
    def __truediv__(self, other):
        if isinstance(other,int):
            other = Number(other)
        return Number(self.num*other.den,self.den*other.num).simplify()
    
    def __floordiv__(self, other):
        return self.__truediv__(other)
    
    def __pow__(self, other):
        if isinstance(other,int):
            other = Number(other)
        assert other.den != 1, 'denominator isn\'t 1'
        return Number(self.num**other.num,self.den**other.num).simplify()
    
    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return '{}/{}'.format(self.num,self.den)
        
    def __repr__(self) -> str:
        return self.__str__()


if __name__ == '__main__':
    n1 = Number(4)
    n2 = Number(8)
    assert n1*n2 == 32
    assert n2/n1 == 2
    assert n1+n2 == 12
    assert n2-n1 == 4
    n3 = Number(1,2)
    n4 = Number(1,3)
    assert n3+n4 == Number(5,6)
    assert n3-n4 == Number(1,6)

    assert n3 > n4
    assert not n3 == n4
    assert n3 != n4

    assert str(n3) == '1/2'
    assert str(n1) == '4'