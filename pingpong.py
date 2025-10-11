import pygame
pygame.init()

scene_lebar = 600
scene_tinggi = 600
scene_judul = "pingpong"
gambar_latar = "galaxy.jpg"
gambar_pemain = "paddle.png"
gambar_bola = "fish.png"
GAME_ON = True
GAME_OVER = False
FPS = pygame.time.Clock()

scene = pygame.display.set_mode((scene_lebar, scene_tinggi))
latar = pygame.transform.scale(pygame.image.load(gambar_latar),
    (scene_lebar, scene_tinggi))


class SpriteSaya(pygame.sprite.Sprite):
    def __init__(self, gambar, x, y, lebar, tinggi, kecepatan):
        super().__init__()
        self.lebar = lebar
        self.tinggi = tinggi
        self.kecepatan = kecepatan
        self.gambar = pygame.transform.scale(pygame.image.load(gambar), 
                                             (self.lebar, self.tinggi))
        self.rect = self.gambar.get_rect()
        self.rect.x = x
        self.rect.y = y

    def tampil(self):
        scene.blit(self.gambar, (self.rect.x, self.rect.y))

class Pemain(SpriteSaya):
    def kendali_kiri(self):
        tombol = pygame.key.get_pressed()
        if tombol[pygame.K_w]:
            self.rect.y -= self.kecepatan
        if tombol[pygame.K_s]:
            self.rect.y += self.kecepatan

    def kendali_kanan(self):
        tombol = pygame.key.get_pressed()
        if tombol[pygame.K_i]:
            self.rect.y -= self.kecepatan
        if tombol[pygame.K_k]:
            self.rect.y += self.kecepatan

p1 = Pemain(gambar_pemain, 20, 20, 100, 200, 10)
p2 = Pemain(gambar_pemain, 500, 20, 100, 200, 10)
bola = SpriteSaya(gambar_bola, 250, 250, 50, 50, 10)

while GAME_ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_ON = False
    if GAME_OVER == False:
        scene.blit(latar, (0, 0))
        p1.tampil()
        p2.tampil()
        bola.tampil()
        p1.kendali_kiri()
        p2.kendali_kanan()
    FPS.tick(60)
    pygame.display.update()