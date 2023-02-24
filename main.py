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
    
    def norm(self):
        return f'sqrt({self.x**2 + self.y**2 + self.z**2})'

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
        print(f'||{name}|| = {vector.norm()}')

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

memory = {
    'points': {},
    'vectors': {},
}

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
            '4 points': WIP,
            '2 vecteurs': WIP,
        },
        'Produit Vectoriel': {
            '4 points': WIP,
            '2 vecteurs': WIP,
        },
        'Angle entre vecteurs': {
            '4 points': WIP,
            '2 vecteurs': WIP,
        },
        'Equation parametrique': {
            '2 points': WIP,
            '1 point et 1 vecteur': WIP,
        },
        'Equation de plan': {
            '1 point et 1 vecteur': WIP,
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
        choice = int(input('Action > '))-1
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


if __name__ == '__main__':
    main()