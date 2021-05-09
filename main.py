import pygame
import random

pygame.init()

class Bird:
    def __init__(self):
        self.direction = random.choice(['ltr','rtl'])
        if self.direction == 'ltr':
            self.x = -50
        elif self.direction == 'rtl':
            self.x = game.width +50
        self.y = random.randint(0, game.height/2)
    def show(self):
        if self.direction == 'ltr':
            game.display.blit(self.image, [self.x,self.y])
        elif self.direction == 'rtl':
            game.display.blit(pygame.transform.flip(self.image, True, False), [self.x,self.y])

    def fly(self):
        if self.direction == 'ltr':
            self.x += self.speed
        elif self.direction == 'rtl':
            self.x -= self.speed

class Duck(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.image = pygame.image.load('Jalase11/images/duck.png')
        self.speed = 4.5
        self.rect = self.image.get_rect()
    
class Pige(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.image = pygame.image.load('Jalase11/images/stork.png')
        self.speed = 5
        self.rect = self.image.get_rect()

class Donkey(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('Jalase11/images/donkey.png'), (48,48))
        self.speed = 6.5
        self.rect = self.image.get_rect()

class Cloud(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('Jalase11/images/cloud.png'), (350,176))
        self.speed = 1.25
        self.rect = self.image.get_rect()
class Gun:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.image = pygame.image.load('Jalase11/images/shooter.png')
        self.sound = pygame.mixer.Sound('Jalase11/sounds/shotgun.wav')
        self.rect = self.image.get_rect()
        self.cart = 10
        self.amm = 5
    def show(self):
        game.display.blit(self.image, [self.x,self.y])

    def fire(self):
        self.sound.play()
        self.amm -= 1
        print('Amm = ',self.amm)
        print('Score = ',game.score)

class Game:
    def __init__(self):
        self.width = 852
        self.height = 480
        self.display = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load('Jalase11/images/background.jpg')
        self.fps = 30
        self.score = 0
    def play(self):
        pygame.mouse.set_visible(False)
        my_gun = Gun()
        duck = Duck()
        pige = Pige()
        donkey = Donkey()
        cloud = Cloud()
        ducks = []
        piges = []
        donkeys = []
        clouds = []
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    my_gun.x = pygame.mouse.get_pos()[0]
                    my_gun.y = pygame.mouse.get_pos()[1]
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if my_gun.amm > 0:
                        my_gun.rect.update(my_gun.x, my_gun.y, 32, 32)

                        for duck in ducks:
                            duck.rect.update(duck.x, duck.y, 48, 48)
                            if my_gun.rect.colliderect(duck.rect) :
                                my_gun.amm += 3
                                self.score += 1
                                ducks.remove(duck)

                        for pige in piges:
                            pige.rect.update(pige.x, pige.y, 64, 64)
                            if  my_gun.rect.colliderect(pige.rect):
                                my_gun.amm += 2
                                self.score += 1
                                piges.remove(pige)

                        for donkey in donkeys:
                            donkey.rect.update(donkey.x, donkey.y, 48, 48)
                            if  my_gun.rect.colliderect(donkey.rect):
                                my_gun.amm += 10
                                self.score += 5
                                donkeys.remove(donkey)

                        my_gun.fire()
                        
                    else:
                        print('Game over')

            if random.random() < 0.006:
                ducks.append(Duck())
            if random.random() < 0.01:
                piges.append(Pige())
            if random.random() < 0.0015:
                donkeys.append(Donkey())
            if random.random() < 0.01:
                clouds.append(Cloud())

            for duck in ducks:
                duck.fly()
            for pige in piges:
                pige.fly()
            for donkey in donkeys:
                donkey.fly()
            for cloud  in clouds:
                cloud.fly()
            self.display.blit(self.background, [0,0])
            my_gun.show()

            for duck in ducks:
                duck.show()
            for pige in piges:
                pige.show()
            for donkey in donkeys:
                donkey.show()
            for cloud in clouds:
                cloud.show()
            pygame.display.update()
            self.clock.tick(self.fps)
if __name__ == "__main__" :
    game = Game()
    game.play()