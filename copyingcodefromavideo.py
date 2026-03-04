character = input('Which character do you wish to output? ')
f = open('characters.txt','r')
end_of_file = False

while not end_of_file:
    name = f.readline().strip()
    health = f.readline().strip()
    stamina= f.readline().strip()
    hunger= f.readline().strip()

    if character == name:
        print(name)
        print('Health: ', health)
        print('Stamina: ', stamina)
        print('Hunger: ', hunger)
    if name == '':
        end_of_file = True
f.close()
        
    
