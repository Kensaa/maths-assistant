VERSION = '1.0.0'

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

#POINT
@action('Voir tous les points')
def showPoints():
    for name,coords in memory['points'].items():
        print(f'{name} = {coords}')

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
        memory['points'][name] = (x,y,z)

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

memory = {
    'points': {},
    'vectors': {},
}

mainMenu = {
    'GEOMETRIE' : {
        'Points': {
            'Voir tous les points': showPoints,
            'Ajouter point(s)': addPoints,
            'Supprimer point': deletePoint,
        },
        'Vecteurs': {
            'Voir tous les vecteurs': WIP,
            'Voir normes des vecteurs': WIP,
            'Ajouter vecteur(s)': {
                '2 points existants': WIP,
                '2 nouveaux points': WIP,
                'coordonnées': WIP,
            }
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
        #tkt c de l'art
        location = 'Menu principal' if len(currentPath) == 0 else currentPath[-1]
        title = f'Maths Assistant v{VERSION} > {location}'
        print(title)
        drawCatergory(currentMenu)
        choice = int(input('Action > '))-1
        choiceKey = getKeyByIndex(currentMenu,choice)
        choiceValue = getValueByIndex(currentMenu,choice)
        if choice == -1:
            if len(currentPath) == 0:
                break
            currentPath.pop()
        elif isinstance(choiceValue, dict):
                currentPath.append(choiceKey)
        else:
            choiceValue()
        
        print('\n'*15)


if __name__ == '__main__':
    main()