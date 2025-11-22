from outline import *
from button import *
import pygame
import os

pygame.init()
clock = pygame.time.Clock()

info = pygame.display.Info()
w = info.current_w
h = info.current_h
pygame.display.set_caption("Jeopardy")
window = pygame.display.set_mode([w, h], pygame.FULLSCREEN)

names = {
    0:['"Megalithic"', 10],
    1:[r"Göbekli Tepe", 5],
    2:["Pyrimads", 30],
    3:["Machu Picchu", 0]
}

def test():
    global running
    running = False
def test2(num):
    global cards, chosen
    if cards[num - 1] == "assets\\card":
        for x in range(16):
            cards[x] = "assets\\card"
        chosen[num - 1] = True
        cards[num - 1] = f"assets\\{num}"
        Set()
    elif cards[num - 1] != "assets\\card":
        cards[num - 1] = "assets\\card"
        Set()
    
Exit = button("assets\\exit", test, 0, 1270, 34, 6, 0, None)
font = pygame.font.SysFont(None, 100)
font2 = pygame.font.SysFont(None, 60)
font3 = pygame.font.SysFont(None, 45)
font4 = pygame.font.SysFont(None, 30)

cards = []
chosen = []
for x in range(16):
    cards.append("assets\\card")
    chosen.append(False)

Buttons = []
def Set():
    global cards, Buttons
    Buttons = []
    for y in range(4):
        for x in range(4):
            index = (y * 4) + x
            Buttons.append(button(cards[index], test2, 0, 125 + (270 * y) + (646 / 6), 140 + (140 * x) + (360 / 6), 3, 0, (y * 4) + x + 1))#card(125 + (270 * y), 120 + (140 * x), 3))
Set()

pygame.mixer.music.load(os.path.realpath("assets\\Theme song.mp3"))
pygame.mixer.music.play(-1)
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    window.fill((25, 98, 176))

    Exit.draw(window)
    for B in Buttons:
        B.draw(window)

    for x in range(4):
        window.blit(render(names[x][0], font3, (255, 255, 255), (0, 0, 0), 4), ((125 + 270 * x) + names[x][1], 100))

    for y in range(4):
        for x in range(4):
            index = (y * 4) + x
            if cards[index] == "assets\\card":
                num = str(x * 100 + 100)
                num2 = 0
                if chosen[(y * 4) + x] == 1:
                    num = "0"
                    num2 = 30
                window.blit(render(num, font2, (255, 255, 255), (0, 0, 0), 4), ((125 + 270 * y) + 60 + num2, (140 + 140 * x) + 50))#(125 + (270 * y) + 60, 120 + (140 * x) + 60 - 5))

    window.blit(render("Jeopardy", font, (255, 255, 255), (0, 0, 0), 6), (center(w, "Jeopardy", 100), 20))
    window.blit(render(r"Copyright© Music", font4, (255, 255, 255), (0, 0, 0), 3), (0, 0))
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
