from settings import *
import pytweening as tween


class Item(pg.sprite.Sprite):

    def __init__(self, game, position, type):
        self._layer = ITEM_LAYER
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = game.items_images[type]
        self.game = game
        self.rect = self.image.get_rect()
        self.type = type
        self.position = position
        self.rect.center = position
        self.tween = tween.easeInOutSine
        self.step = 0
        self.direction = 1

    def update(self):
        offset = ITEM_BOB_RANGE * (self.tween(self.step / ITEM_BOB_RANGE) - 0.5)
        self.rect.centery = self.position.y + offset * self.direction
        self.step += ITEM_BOB_SPEED
        if self.step > ITEM_BOB_RANGE:
            self.step = 0
            self.direction *= -1
