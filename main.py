VERSION = '1.0.0'

def action(name:str):
    def decorator_action(func):
        def wrapper():
            print('\n'*15)
            print(name)
            print('')
            func()
        return wrapper
    return decorator_action

@action('la function 1')
def function1():
    print('do some stuff')
    input()

mainMenu = {
    'GEOMETRIE' : {
            'sub-cat1': function1
        }
}

def drawCatergory(category:dict):
    for i,name in enumerate(category.keys()):
        print(f'\t{i+1}. {name}')
    print('\n\t0. Go back')

def getValueByIndex(category:dict,index:int):
    return list(category.values())[index]

def main(previousMenu=None,currentMenu=mainMenu):
    while currentMenu != None:
        #tkt c de l'art
        title = f'Math Assistant v{VERSION}' if currentMenu == mainMenu else f'Math Assistant v{VERSION} > {list(previousMenu.keys())[list(previousMenu.values()).index(currentMenu)]}'
        print(title)
        drawCatergory(currentMenu)
        choice = int(input('Action > '))-1
        if choice == -1:
            currentMenu = previousMenu
        else:
            if isinstance(getValueByIndex(currentMenu,choice),dict):
                previousMenu = currentMenu
                currentMenu = getValueByIndex(currentMenu,choice)
            else:
                getValueByIndex(currentMenu,choice)()
        
        print('\n'*15)


if __name__ == '__main__':
    main()