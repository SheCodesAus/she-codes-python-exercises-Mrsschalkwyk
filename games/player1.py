# player_name= 'manual'
# player_attack = 10
# player_heal = 16
# health = 100

# player = ['manual', 10 , 16, 100]

# print(player[2])
# player[1]= 11

player = {'name': 'manual', 'attack' : 10, 'heal':16, 'health':100}
monster = {'name':'max', 'attack':12, 'health':100}
game_running = True

while game_running == True:

    print('Please select action')
    print('1) Attack')
    print('2) Heal')
    player_choice =input()

    if player_choice == '1':
        monster['health'] = monster['health'] - player['attack']
        if monster['health'] <=0:
         pass

        else:
            player['health']= player['health'] - monster['attack']
            if player['health'] <=0:
                passwinget install --id Microsoft.Powershell --source winget
winget install --id Microsoft.Powershell.Preview --source winget


        print(monster['health'])
        print(player['health'])


    elif player_choice == '2':
        print('Heal player')
    else:
        print('invalid input')    

    if player['health'] <= 0 or monster['health'] <=0:
        game_running=False    