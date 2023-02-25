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
        return f'({self.x}; {self.y}; {self.z})'

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
        return f'sqrt({self.x**2 + self.y**2 + self.z**2})'

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
        return f'({self.x}; {self.y}; {self.z})'

def action(name:str):
    def decorator_action(func):
        def wrapper():
            print('\n'*15)
            print(f'*** {name} ***')
            print('')
            func()
            input('Appuyez sur entrée pour continuer...')
        return wrapper
    return decorator_action
@action('Work In Progress')
def WIP():
    print('NOT IMPLEMENTED')

@action('Voir tous les points')
def showPoints():
    for name,point in memory['points'].items():
        print(f'{name}{point}')

@action('Ajouter point(s)')
def addPoints():
    while True:
        name = input('Nom du point > ').strip().upper()
        if name == '':
            break
        if name in memory['points']:
            print('Ce nom est déjà utilisé')
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
        print(f'{name}{vector}')

@action('Voir normes des vecteurs')
def showVectorsNorms():
    for name,vector in memory['vectors'].items():
        print(f'||{name}|| = {vector.normStr()}')

@action('Ajouter vecteur(s) a partir de 2 points existants')
def addVectorsFromExistingPoint():
    while True:
        point1 = input('Nom du premier point > ').strip().upper()
        if point1 == '':
            break
        point2 = input('Nom du deuxième point > ').strip().upper()
        if point2 == '':
            break
        if point1 not in memory['points']:
            print('Le premier point n\'existe pas')
            continue
        if point2 not in memory['points']:
            print('Le deuxième point n\'existe pas')
            continue
        name = point1+point2
        if name in memory['vectors']:
            print('Ce nom est déjà utilisé')
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
            print('Ce nom est déjà utilisé')
            continue
        x1 = int(input('x du premier point > '))
        y1 = int(input('y du premier point > '))
        z1 = int(input('z du premier point > '))
        x2 = int(input('x du deuxième point > '))
        y2 = int(input('y du deuxième point > '))
        z2 = int(input('z du deuxième point > '))
        memory['vectors'][name] = Vector(x2-x1, y2-y1, z2-z1)

@action('Ajouter vecteur(s) a partir de coordonnées')
def addVectorsFromCoordinates():
    while True:
        name = input('Nom du vecteur > ').strip().upper()
        if name == '':
            break
        if name in memory['vectors']:
            print('Ce nom est déjà utilisé')
            continue
        x = int(input('x > '))
        y = int(input('y > '))
        z = int(input('z > '))
        memory['vectors'][name] = Vector(x,y,z)

def askPoint():
    while True:
        pAsk = input('Nom du point ou x > ')
        if pAsk.isnumeric():
            x = int(pAsk)
            y = int(input('y > '))
            z = int(input('z > '))
            return Point(x,y,z)
        else:
            pAsk = pAsk.strip().upper()
            if pAsk not in memory['points']:
                print('Le point n\'existe pas')
            else:
                return memory['points'][pAsk]

def askVector():
    while True:
        vAsk = input('Nom du vecteur ou x > ')
        if vAsk.isnumeric():
            x = int(vAsk)
            y = int(input('y > '))
            z = int(input('z > '))
            return Vector(x,y,z)
        else:
            vAsk = vAsk.strip().upper()
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
    print(f'{v1}.{v2} = {v1.dot(v2)}')

@action('Produit scalaire avec 2 vecteurs')
def dotProduct2Vectors():
    v1 = askVector()
    v2 = askVector()
    print(f'{v1}.{v2} = {v1.dot(v2)}')

@action('Produit vectoriel avec 4 points')
def crossProduct4Points():
    p1 = askPoint()
    p2 = askPoint()
    p3 = askPoint()
    p4 = askPoint()
    v1 = Vector(p2.x-p1.x, p2.y-p1.y, p2.z-p1.z)
    v2 = Vector(p4.x-p3.x, p4.y-p3.y, p4.z-p3.z)
    print(f'{v1}*{v2} = {v1.cross(v2)}')

@action('Produit vectoriel avec 2 vecteurs')
def crossProduct2Vectors():
    v1 = askVector()
    v2 = askVector()
    print(f'{v1}*{v2} = {v1.cross(v2)}')

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
    print(f'cos({v1},{v2}) = {dot}/{normStr1}{normStr2} = {cosAngle}')
    print(f'Angle entre {v1} et {v2} = {acos(cosAngle)} rad = {angle/pi*180}°')

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
    print(f'cos({v1},{v2}) = {dot}/{normStr1}{normStr2} = {cosAngle}')
    print(f'Angle entre {v1} et {v2} = {acos(cosAngle)} rad = {angle/pi*180}°')

@action('Representation parametrique d\'une droite avec 2 points')
def parametricRepresentation2Points():
    p1 = askPoint()
    p2 = askPoint()
    v = Vector(p2.x-p1.x, p2.y-p1.y, p2.z-p1.z)
    print(f'x = {p1.x} + t*{v.x}')
    print(f'y = {p1.y} + t*{v.y}')
    print(f'z = {p1.z} + t*{v.z}')

@action('Representation parametrique d\'une droite avec 1 point et 1 vecteur')
def parametricRepresentationPointVector():
    p = askPoint()
    v = askVector()
    print(f'x = {p.x} + t*{v.x}')
    print(f'y = {p.y} + t*{v.y}')
    print(f'z = {p.z} + t*{v.z}')

@action('Equation cartesienne de plan avec 1 point et 1 vecteur')
def cartesianEquationPointVector():
    p = askPoint()
    v = askVector()
    d = -(p.x*v.x + p.y*v.y + p.z*v.z)
    print(f'{v.x}x + {v.y}y + {v.z}z + {d} = 0')

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
                'coordonnées': addVectorsFromCoordinates,
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
        'Représentation parametrique': {
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
        print(f'\t{i+1}. {name}')
    print('\n\t0. Go back')

def getKeyByIndex(category:dict,index:int):
    return list(category.keys())[index]

def getValueByIndex(category:dict,index:int):
    return list(category.values())[index]

def main():
    currentPath = []
    while True:
        currentMenu = mainMenu
        for path in currentPath:
            currentMenu = currentMenu[path]
        location = 'Menu principal' if len(currentPath) == 0 else currentPath[-1]
        title = f'Maths Assistant v{VERSION} > {location}'
        print(title)
        drawCatergory(currentMenu)
        inp = input('Action > ')
        if not inp.isnumeric():
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
        
        print('\n'*15)

memory = {
    'points': {},
    'vectors': {},
}

if __name__ == '__main__':
    main()