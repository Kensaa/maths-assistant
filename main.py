from math import acos, pi

VERSION = '1.0.0'

class Point:
    def __init__(self, x=0, y=0, z=0)->None:
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z    

    def __str__(self):
        #return f'({self.x}; {self.y}; {self.z})'
        return '({}; {}; {})'.format(self.x, self.y, self.z)

class Vector:
        
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self
    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
    def mult(self, k:int):
        self.x *= k
        self.y *= k
        self.z *= k
        return self
    
    def normStr(self):
        #return f'sqrt({self.x**2 + self.y**2 + self.z**2})'
        return 'sqrt({})'.format(self.x**2 + self.y**2 + self.z**2)

    def norm(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z
    def cross(self, other):
        return Vector(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )
    def __str__(self):
        #return f'({self.x}; {self.y}; {self.z})'
        return '({}; {}; {})'.format(self.x, self.y, self.z)

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
        return self.num*other.den - other.num*self.den < 0

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

def action(name:str):
    def decorator_action(func):
        def wrapper():
            print('\n'*15)
            #print(f'*** {name} ***')
            print('*** {} ***'.format(name))
            print('')
            func()
            input('Appuyez sur entr??e pour continuer...')
        return wrapper
    return decorator_action
@action('Work In Progress')
def WIP():
    print('NOT IMPLEMENTED')

@action('Voir tous les points')
def showPoints():
    for name,point in memory['points'].items():
        #print(f'{name}{point}')
        print('{}{}'.format(name,point))

@action('Ajouter point(s)')
def addPoints():
    while True:
        name = input('Nom du point > ').strip().upper()
        if name == '':
            break
        if name in memory['points']:
            print('Ce nom est d??j?? utilis??')
            continue
        x = int(input('x > '))
        y = int(input('y > '))
        z = int(input('z > '))
        memory['points'][name] = Point(x,y,z)

@action('Supprimer point')
def deletePoint():
    while True:
        name = input('Nom du point > ').strip().upper()
        if name == '':
            break
        if name not in memory['points']:
            print('Ce point n\'existe pas')
            continue
        del memory['points'][name]


@action('Voir tous les vecteurs')
def showVectors():
    for name,vector in memory['vectors'].items():
        #print(f'{name}{vector}')
        print('{}{}'.format(name,vector))

@action('Voir normes des vecteurs')
def showVectorsNorms():
    for name,vector in memory['vectors'].items():
        #print(f'||{name}|| = {vector.normStr()}')
        print('||{}|| = {}'.format(name,vector.normStr()))

@action('Ajouter vecteur(s) a partir de 2 points existants')
def addVectorsFromExistingPoint():
    while True:
        point1 = input('Nom du premier point > ').strip().upper()
        if point1 == '':
            break
        point2 = input('Nom du deuxi??me point > ').strip().upper()
        if point2 == '':
            break
        if point1 not in memory['points']:
            print('Le premier point n\'existe pas')
            continue
        if point2 not in memory['points']:
            print('Le deuxi??me point n\'existe pas')
            continue
        name = point1+point2
        if name in memory['vectors']:
            print('Ce nom est d??j?? utilis??')
            continue
        p1 = memory['points'][point1]
        p2 = memory['points'][point2]
        memory['vectors'][name] = Vector(p2.x-p1.x, p2.y-p1.y, p2.z-p1.z)

@action('Ajouter vecteur(s) a partir de 2 nouveaux points')
def addVectorsFromNewPoint():
    while True:
        name = input('Nom du vecteur > ').strip().upper()
        if name == '':
            break
        if name in memory['vectors']:
            print('Ce nom est d??j?? utilis??')
            continue
        x1 = int(input('x du premier point > '))
        y1 = int(input('y du premier point > '))
        z1 = int(input('z du premier point > '))
        x2 = int(input('x du deuxi??me point > '))
        y2 = int(input('y du deuxi??me point > '))
        z2 = int(input('z du deuxi??me point > '))
        memory['vectors'][name] = Vector(x2-x1, y2-y1, z2-z1)

@action('Ajouter vecteur(s) a partir de coordonn??es')
def addVectorsFromCoordinates():
    while True:
        name = input('Nom du vecteur > ').strip().upper()
        if name == '':
            break
        if name in memory['vectors']:
            print('Ce nom est d??j?? utilis??')
            continue
        x = int(input('x > '))
        y = int(input('y > '))
        z = int(input('z > '))
        memory['vectors'][name] = Vector(x,y,z)

def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def askPoint():
    while True:
        pAsk = input('Nom du point ou x > ').strip()
        if isNumber(pAsk):
            x = int(pAsk)
            y = int(input('y > '))
            z = int(input('z > '))
            return Point(x,y,z)
        else:
            pAsk = pAsk.upper()
            if pAsk not in memory['points']:
                print('Le point n\'existe pas')
            else:
                return memory['points'][pAsk]

def askVector():
    while True:
        vAsk = input('Nom du vecteur ou x > ').strip()
        if isNumber(vAsk):
            x = int(vAsk)
            y = int(input('y > '))
            z = int(input('z > '))
            return Vector(x,y,z)
        else:
            vAsk = vAsk.upper()
            if vAsk not in memory['vectors']:
                print('Le vecteur n\'existe pas')
            else:
                return memory['vectors'][vAsk]

@action('Produit scalaire avec 4 points')
def dotProduct4Points():
    p1 = askPoint()
    p2 = askPoint()
    p3 = askPoint()
    p4 = askPoint()
    v1 = Vector(p2.x-p1.x, p2.y-p1.y, p2.z-p1.z)
    v2 = Vector(p4.x-p3.x, p4.y-p3.y, p4.z-p3.z)
    #print(f'{v1}.{v2} = {v1.dot(v2)}')
    print('{}{} = {}'.format(v1,v2,v1.dot(v2)))

@action('Produit scalaire avec 2 vecteurs')
def dotProduct2Vectors():
    v1 = askVector()
    v2 = askVector()
    #print(f'{v1}.{v2} = {v1.dot(v2)}')
    print('{}{} = {}'.format(v1,v2,v1.dot(v2)))

@action('Produit vectoriel avec 4 points')
def crossProduct4Points():
    p1 = askPoint()
    p2 = askPoint()
    p3 = askPoint()
    p4 = askPoint()
    v1 = Vector(p2.x-p1.x, p2.y-p1.y, p2.z-p1.z)
    v2 = Vector(p4.x-p3.x, p4.y-p3.y, p4.z-p3.z)
    #print(f'{v1}*{v2} = {v1.cross(v2)}')
    print('{}{} = {}'.format(v1,v2,v1.cross(v2)))

@action('Produit vectoriel avec 2 vecteurs')
def crossProduct2Vectors():
    v1 = askVector()
    v2 = askVector()
    #print(f'{v1}*{v2} = {v1.cross(v2)}')
    print('{}{} = {}'.format(v1,v2,v1.cross(v2)))

@action('Angle entre vecteurs avec 4 points')
def angleBetweenVectors4Points():
    p1 = askPoint()
    p2 = askPoint()
    p3 = askPoint()
    p4 = askPoint()
    v1 = Vector(p2.x-p1.x, p2.y-p1.y, p2.z-p1.z)
    v2 = Vector(p4.x-p3.x, p4.y-p3.y, p4.z-p3.z)
    dot = v1.dot(v2)
    normStr1 = v1.normStr()
    normStr2 = v2.normStr()
    norm1 = v1.norm()
    norm2 = v2.norm()
    cosAngle = dot/(norm1*norm2)
    angle = acos(cosAngle)
    #print(f'cos({v1},{v2}) = {dot}/{normStr1}{normStr2} = {cosAngle}')
    #print(f'Angle entre {v1} et {v2} = {acos(cosAngle)} rad = {angle/pi*180}??')
    print('cos({},{}) = {}/{}{} = {}'.format(v1,v2,dot,normStr1,normStr2,cosAngle))
    print('Angle entre {} et {} = {} rad = {}??'.format(v1,v2,acos(cosAngle),angle/pi*180))

@action('Angle entre vecteurs avec 2 vecteurs')
def angleBetweenVectors2Vectors():
    v1 = askVector()
    v2 = askVector()
    dot = v1.dot(v2)
    normStr1 = v1.normStr()
    normStr2 = v2.normStr()
    norm1 = v1.norm()
    norm2 = v2.norm()
    cosAngle = dot/(norm1*norm2)
    angle = acos(cosAngle)
    #print(f'cos({v1},{v2}) = {dot}/{normStr1}{normStr2} = {cosAngle}')
    #print(f'Angle entre {v1} et {v2} = {acos(cosAngle)} rad = {angle/pi*180}??')
    print('cos({},{}) = {}/{}{} = {}'.format(v1,v2,dot,normStr1,normStr2,cosAngle))
    print('Angle entre {} et {} = {} rad = {}??'.format(v1,v2,acos(cosAngle),angle/pi*180))

@action('Representation parametrique d\'une droite avec 2 points')
def parametricRepresentation2Points():
    p1 = askPoint()
    p2 = askPoint()
    v = Vector(p2.x-p1.x, p2.y-p1.y, p2.z-p1.z)
    #print(f'x = {p1.x} + t*{v.x}')
    #print(f'y = {p1.y} + t*{v.y}')
    #print(f'z = {p1.z} + t*{v.z}')
    print('x = {} + t*{}'.format(p1.x,v.x))
    print('y = {} + t*{}'.format(p1.y,v.y))
    print('z = {} + t*{}'.format(p1.z,v.z))

@action('Representation parametrique d\'une droite avec 1 point et 1 vecteur')
def parametricRepresentationPointVector():
    p = askPoint()
    v = askVector()
    #print(f'x = {p.x} + t*{v.x}')
    #print(f'y = {p.y} + t*{v.y}')
    #print(f'z = {p.z} + t*{v.z}')
    print('x = {} + t*{}'.format(p.x,v.x))
    print('y = {} + t*{}'.format(p.y,v.y))
    print('z = {} + t*{}'.format(p.z,v.z))

@action('Equation cartesienne de plan avec 1 point et 1 vecteur')
def cartesianEquationPointVector():
    p = askPoint()
    v = askVector()
    d = -(p.x*v.x + p.y*v.y + p.z*v.z)
    #print(f'{v.x}x + {v.y}y + {v.z}z + {d} = 0')
    print('{}x + {}y + {}z + {} = 0'.format(v.x,v.y,v.z,d))

mainMenu = {
    'GEOMETRIE' : {
        'Points': {
            'Ajouter point(s)': addPoints,
            'Voir tous les points': showPoints,
            'Supprimer point': deletePoint,
        },
        'Vecteurs': {
            'Ajouter vecteur(s)': {
                '2 points existants': addVectorsFromExistingPoint,
                '2 nouveaux points': addVectorsFromNewPoint,
                'coordonn??es': addVectorsFromCoordinates,
            },
            'Voir tous les vecteurs': showVectors,
            'Voir normes des vecteurs': showVectorsNorms
        },
        'Produit Scalaire': {
            '4 points': dotProduct4Points,
            '2 vecteurs': dotProduct2Vectors,
        },
        'Produit Vectoriel': {
            '4 points': crossProduct4Points,
            '2 vecteurs': crossProduct2Vectors,
        },
        'Angle entre vecteurs': {
            '4 points': angleBetweenVectors4Points,
            '2 vecteurs': angleBetweenVectors2Vectors,
        },
        'Repr??sentation parametrique': {
            '2 points': parametricRepresentation2Points,
            '1 point et 1 vecteur': parametricRepresentationPointVector,
        },
        'Equation cartesienne de plan': {
            '1 point et 1 vecteur': cartesianEquationPointVector,
        }
    }
}

def drawCatergory(category:dict):
    for i,name in enumerate(category.keys()):
        #print(f'\t{i+1}. {name}')
        print('\t{}. {}'.format(i+1,name))
    print('\n\t0. Go back')

def getKeyByIndex(category:dict,index:int):
    return list(category.keys())[index]

def getValueByIndex(category:dict,index:int):
    return list(category.values())[index]




memory = {
    'points': {},
    'vectors': {},
}

#main program
currentPath = []
while True:
    currentMenu = mainMenu
    for path in currentPath:
        currentMenu = currentMenu[path]
    location = 'Menu principal' if len(currentPath) == 0 else currentPath[-1]
    #title = f'Maths Assistant v{VERSION} > {location}'
    title = 'Maths Assistant v{} > {}'.format(VERSION,location)
    print(title)
    drawCatergory(currentMenu)
    inp = input('Action > ')
    if not isNumber(inp):
        print('Action invalide')
        continue
    choice = int(inp)-1
    if choice == -1:
        if len(currentPath) == 0:
            break
        currentPath.pop()
    elif choice > len(currentMenu)-1:
        print('Action invalide')
    else:
        choiceKey = getKeyByIndex(currentMenu,choice)
        choiceValue = getValueByIndex(currentMenu,choice)
        if isinstance(choiceValue, dict):
            currentPath.append(choiceKey)
        else:
            choiceValue()
    print('\n'*5)
    