class PlayerCharacter:
    membership = True #Class Object Attribute
    def __init__(self,name,age):
        self.name = name #attributes
        self.age  = age
    def shout(self):
        print(f'My Name is {self.name} And Age is {self.age}')
        print(f'My Membership is {PlayerCharacter.membership}')


player1 = PlayerCharacter('Sreehari',34)
player2 = PlayerCharacter('Jyostna',25)

print('Player1 :')
player1.shout()
print('Player2 :')
player2.shout()

PlayerCharacter.membership  = False

print('Player1 :')
player1.shout()
print('Player2 :')
player2.shout()


player1.membership  = True

print('Player1 :')
player1.shout()
print('Player2 :')
player2.shout()