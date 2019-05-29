#  Role Playing Game
import random
import sys
from pygame import mixer
from time import sleep
mixer.init()


class NPC:
    def __init__(self, lvl, quest_step, progress):
        self.lvl = lvl
        self.quest_step = quest_step
        self.progress = progress

    def quest(self, other):
        if self.quest_step == 0:
            print('Welcome, JoJo! My name is GRAND_MASTER_80LVL. Yes, this is my real name, I\'m not joking', '\n',
                  'I\'ll help you to improve your stats, just follow my directions')
            print('Bring me 5 Murlock\'s head', ' I\'ll give you 100 exp and 50 basic health points instead')
            self.quest_step = 1
        if (self.quest_step == 1) and (self.progress < 5):
            print('Not enough heads:', 'You\'ve got {}'.join(str(Grand_master_80lvl.progress)))
        if (self.progress >= 5) and (self.quest_step == 1):
            print('10q, Jotaro, you\'re really great hero!', ' Here is your reward')
            self.quest_step = 2
            self.progress = 0
            other.exp += 100
            other.hp += 50
        if self.quest_step == 2:
            print('I need 3 Orc\'s fang;', 'Reward: 200 exp and 20 basic damage')
            self.quest_step = 3
        if (self.quest_step == 3) and (self.progress < 3):
            print('Not enough fangs', 'You\'ve got {}'.join(str(Grand_master_80lvl.progress)))
        if (self.progress >= 3) and (self.quest_step == 3):
            print('10q, Jotaro, you\'re really great hero!', ' Here is your reward')
            self.quest_step = 4
            self.progress = 0
            other.exp += 200
            other.dmg += 20
        if self.quest_step == 4:
            print('I already see a great warrior in you, Jotaro! But it\'s not the end.', '\n',
                  'You should kill 3 wizards, be careful their magic may hurt you much. ',
                  'Reward: 300 exp and 150 health point')
            self.quest_step = 5
        if (self.quest_step == 5) and (self.progress < 3):
            print('Not enough kills', 'You\'ve got {}'.join(str(Grand_master_80lvl.progress)))
        if (self.quest_step == 5) and (self.progress >= 3):
            print('10q, Jotaro, you\'re really great hero!', ' Here is your reward')
            other.exp += 300
            other.hp += 150
            self.quest_step = 6
            self.progress = 0
        if self.quest_step == 6:
            print('We have come a long way together, JoJo. That\'s your penultimate task: '
                  ' Kill two dangerous monsters - Spider and Dragon'
                  '; Reward: 400 exp and 60 basic damage')
            self.quest_step = 7
        if (self.quest_step == 7) and (self.progress < 2):
            print('Not enough kills', 'You\'ve got {}'.join(str(Grand_master_80lvl.progress)))
        if (self.quest_step == 7) and (self.progress >= 2):
            print('10q, Jotaro, you\'re really great hero!', ' Here is your reward')
            other.exp += 400
            other.dmg += 60
            self.quest_step = 8
            self.progress = 0
        if self.quest_step == 8:
            print('Level 9 requiered for next quest. Go kill someone')
        if (self.quest_step == 8) and (other.lvl == 9):
            print('Now, you\'re ready. I hope. Anyway, It has to be done. Find and kill Dio. ')
            self.progress = 0
            self.quest_step = 9
        if (self.quest_step == 9) and (self.progress == 1):
            print('Good job. Your friends didn\'t die for nothing, they would be proud of you!')
            self.quest_step = 10
            self.progress = 0
            print('Well, I should tell you truth. There is another bad guy. Reeealy bad guy. His name is... DEKAN', '\n'
                  , 'I\'m not gonna force you to do it, but.. You know, someone must do it. Talk to me one more time '
                    'when you are ready')
        if (self.quest_step == 9) and (self.progress == 0):
            print('There is no way back. Go do what you have to!')
        if (self.quest_step == 10) and (self.progress == 1):
            print('This is the time. You are ready. Now you\'ll receive power of Gods. Use it wisely, Jotaro ')
            other = Hero(100000, 7777, 1, 1, 777, 0)
            self.progress = 0
            self.quest_step = 11
        if (self.quest_step == 11) and (self.progress == 1):
            print('Everything written is a fiction, respect your teachers and dekan',
                  '\n', 'The End')
            sys.exit()
        if (self.progress == 0) and (self.quest_step == 11):
            print('What are u waiting for? Show him who\'s daddy! ')


class Character(NPC):
    def __init__(self, hp, dmg, defense, crit_chance, lvl):
        super().__init__(lvl, 0, 0)
        self.hp = hp
        self.dmg = dmg
        self.defense = defense
        self.crit_chance = crit_chance
        self.lvl = lvl

    def __sub__(monster, hero):
        if monster.hp > 0:
            print('Ход моба')
            krit = random.randint(0, round(1 / monster.crit_chance))
            if krit == round(1 / monster.crit_chance):
                print('Critical damage!1!')
                hero.hp = hero.hp - 2*(2 * monster.dmg * (1 - hero.defense))
            else:
                hero.hp = hero.hp - 2*(monster.dmg * (1 - hero.defense))
            print('Хп героя: ', round(hero.hp, 1))
        if hero.hp > 0:
            print('Ход героя')
            krit = random.randint(0, round(1 / hero.crit_chance))
            if krit == round(1 / hero.crit_chance):
                print('Critical damage!1!')
                monster.hp = monster.hp - 2*(2 * hero.dmg * (1 - monster.defense))
            else:
                monster.hp = monster.hp - 2*(hero.dmg * (1 - monster.defense))
            print('Хп моба: ', round(monster.hp, 1))


class Hero(Character):
    def __init__(self, hp, dmg, defense, crit_chance, lvl, exp):
        super().__init__(hp, dmg, defense, crit_chance, lvl)
        self.exp = exp

    def experience(self, recived_exp):
        self.exp += recived_exp

    def __sub__(hero, monster):
                if hero.hp > 0:
                    print('Ход героя')
                    krit = random.randint(0, round(1 / hero.crit_chance))
                    if krit == round(1 / hero.crit_chance):
                        print('Critical damage!1!')
                        monster.hp = monster.hp - 2*(2 * hero.dmg * (1 - monster.defense))
                    else:
                        monster.hp = monster.hp - 2*(hero.dmg * (1 - monster.defense))
                    print('Здоровье моба: ', round(monster.hp, 1))

                if monster.hp > 0:
                    print('Ход моба')
                    krit = random.randint(0, round(1 / monster.crit_chance))
                    if krit == round(1 / monster.crit_chance):
                        print('Critical damage!1!')
                        hero.hp = hero.hp - 2*(2 * monster.dmg * (1 - hero.defense))
                    else:
                        hero.hp = hero.hp - 2*(monster.dmg * (1 - hero.defense))
                    print('Здоровье героя: ', round(hero.hp, 1))


def statistics(someone):
    print('Health ', round(someone.hp), '; Damage', round(someone.dmg), '; Defense', round(someone.defense, 2),
          '; Critical damage chance', round(someone.crit_chance, 2),
          '; Level ', round(someone.lvl), '\n', '---------------------------------------------------------------------')


def sound(filename):
    music = mixer.Sound(filename)
    music.set_volume(0.07)
    music.play(30)


def fight(hero, monster):
    go = 1
    while go:
            print('Хп моба', round(monster.hp), '\n', 'Хп ДжоДжо', round(hero.hp))
            if hero.lvl >= monster.lvl:  # First move
                while (hero.hp > 0) and (monster.hp > 0):
                    hero - monster
                    #sleep(1.2)
            else:
                while (hero.hp > 0) and (monster.hp > 0):
                    monster - hero
                    #sleep(1.2)
            if monster.hp <= 0:
                hero.exp = hero.exp+(monster.lvl*10)
                print('JoJo won')
                print('Experience :', JoJo.exp, 'of ', JoJo.lvl*100)
                go = 0
            elif hero.hp <= 0:
                print('Monster won', '\n', 'YOU DIED')
                go = 0
                sys.exit()


Grand_master_80lvl = NPC(80, 0, 0)
JoJo = Hero(100, 10, 0.1, 0.1, 1, 0)
Murlock = Character(30, 5, 0.05, 0.05, 1)
Orc = Character(130, 14, 0.2, 0.2, 2)
Wizard = Character(150, 50, 0.2, 0.4, 4)
Spider = Character(450, 70, 0.4, 0.6, 6)
Dragon = Character(600, 140, 0.6, 0.5, 8)
Dio = Character(1400, 140, 0.8, 0.9, 9)
DEKAN = Character(9999, 999, 0.9, 1, 666)


inputting = 1

rules1 = '''HeeeeeeLLo, My Friend!
This is my SUPER-MEGA-INTERESTING-AWESOME-RPG!!
Here you can fight, fight and fight. And also fight. And in time when you don't fight you can fight
Voooot tak vot
By the way, look all commands - just type commands
Hope you'll have fun
*Playing music from JoJo's Bizzare Adventure anime* 
'''

commands = '''
fight Someone   - Fight (Murlock, Orc, Spider etc) 
heal            - Heal 50% hp(You've got only 2 potions on the start, be careful)
stop or end     - End the game
stats           - JoJo's stats
monsters        - Monsters' stats
quest           - See current quest
'''

game_theme = sound('Jojo_song.ogg')

Jojo_potions = 2

print(rules1)

k = 0
while inputting:
    inp = str(input())
    if JoJo.exp >= JoJo.lvl*100:
        JoJo.exp = 0
        Jojo_potions += 1
        print('+ 1 health potion')
        z = 0
        if JoJo.lvl < 9:
            JoJo.lvl += 1
            k = JoJo.lvl
            if Grand_master_80lvl.quest_step > 1:
                JoJo = Hero(k*100+50, k*10, k*0.1, k*0.1, k*1, 0)
            if Grand_master_80lvl.quest_step > 3:
                JoJo = Hero(k*100 + 50, k*10+20, k*0.1, k*0.1, k*1, 0)
            if Grand_master_80lvl.quest_step > 5:
                JoJo = Hero(k*100 + 200, k*10+20, k*0.1, k*0.1, k*1, 0)
            if (Grand_master_80lvl.quest_step == 0) or (Grand_master_80lvl.quest_step == 1):
                JoJo = Hero(k * 100, k * 10, k * 0.1, k * 0.1, k * 1, 0)
        elif z == 0:
            print('You are UNBREAKABLE like a Diamond!!!'
                  'In fact, you\'re just max lvl')
            z = 1
    if (inp == 'end') or (inp == 'stop'):
        print('See you later!')
        inputting = 0
    if inp == 'fight Murlock':
        Murlock = Character(30, 5, 0.05, 0.05, 1)
        fight(JoJo, Murlock)
        if Grand_master_80lvl.quest_step == 1:
            Grand_master_80lvl.progress += 1
    if inp == 'fight Orc':
        Orc = Character(50, 7, 0.1, 0.2, 2)
        fight(JoJo, Orc)
        if Grand_master_80lvl.quest_step == 3:
            Grand_master_80lvl.progress += 1
    if inp == 'fight Spider':
        Spider = Character(450, 70, 0.4, 0.6, 6)
        fight(JoJo, Spider)
        if Grand_master_80lvl.quest_step == 7:
            Grand_master_80lvl.progress += 1
    if inp == 'fight Wizard':
        Wizard = Character(150, 50, 0.2, 0.4, 4)
        fight(JoJo, Wizard)
        if Grand_master_80lvl.quest_step == 5:
            Grand_master_80lvl.progress += 1
    if inp == 'fight Dragon':
        Dragon = Character(600, 140, 0.6, 0.7, 8)
        fight(JoJo, Dragon)
        if Grand_master_80lvl.quest_step == 7:
            Grand_master_80lvl.progress += 1
    if inp == 'fight Dio':
        Dio = Character(1400, 140, 0.8, 0.9, 9)
        fight(JoJo, Dio)
        if Grand_master_80lvl.quest_step == 9:
            Grand_master_80lvl.progress += 1
    if inp == 'fight DEKAN':
        print('it\'s a beautiful day outside')
        sleep(1.5)
        print('birds are singing, flowers are blooming')
        sleep(1.5)
        print('on days like this, kids like you...')
        sleep(1.5)
        print('s h o u l d ')
        sleep(1.5)
        print('b e')
        sleep(1.5)
        print('b u r n i n g')
        sleep(1.5)
        print('i n')
        sleep(1.5)
        print('h e l l')
        sleep(5)
        if Grand_master_80lvl.quest_step == 11:
            JoJo = Hero(100000, 777, 1, 1, 777, 0)
        DEKAN = Character(9999, 999, 0.9, 1, 666)
        fight(JoJo, DEKAN)
        if Grand_master_80lvl.quest_step == 11:
            Grand_master_80lvl.progress += 1
    if inp == 'heal':
        if Jojo_potions > 0:
            JoJo.hp += JoJo.lvl*50
            Jojo_potions -= 1
            print(round(JoJo.hp))
        else:
            print('No potion')
    if (inp == 'COMMANDS') or (inp == 'commands'):
        print(commands)
    if inp == 'jojo stats' or inp == 'stats':
        print('JoJo\'s stats')
        statistics(JoJo)
    if inp == 'monsters':
        Murlock = Character(30, 5, 0.05, 0.05, 1)
        Orc = Character(50, 7, 0.1, 0.2, 2)
        Wizard = Character(150, 50, 0.2, 0.4, 4)
        Spider = Character(450, 70, 0.4, 0.6, 6)
        Dragon = Character(600, 100, 0.6, 0.7, 8)
        Dio = Character(1400, 140, 0.8, 0.9, 9)
        DEKAN = Character(9999, 999, 0.9, 1, 666)
        print('Murlock stats')
        statistics(Murlock)
        print('Orc stats ')
        statistics(Orc)
        print('Wizard stats ')
        statistics(Wizard)
        print('Spider stats ')
        statistics(Spider)
        print('Dragon stats ')
        statistics(Dragon)
        print('Dio stats ')
        statistics(Dio)
        print('DEKAN stats ')
        statistics(DEKAN)
    if inp == 'quest':
        if (Grand_master_80lvl.quest_step == 10) and (Grand_master_80lvl.progress == 0):
            Grand_master_80lvl.progress = 1
        Grand_master_80lvl.quest(JoJo)
    #if inp == 'WTF':
    #    fight(JoJo, JoJo)
    #if inp == 'gg':
    #    k = 0
    #    while k != 100:
    #        Orc = Character(50, 7, 0.1, 0.2, 2)
    #        fight(JoJo, Orc)
    #        k += 1
