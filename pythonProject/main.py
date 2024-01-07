import pygame
import sys
import math
import random


pygame.init()


def fereastra_joc():

    minigame_width, minigame_height = 800, 600
    minigame_screen = pygame.display.set_mode((minigame_width, minigame_height))
    pygame.display.set_caption("Joculet")


    pygame.mixer.music.stop()
    pygame.mixer.music.load("tetris-theme.mp3")
    pygame.mixer.music.play(-1)


    green = (0, 255, 0)
    red = (255, 0, 0)
    background = (0, 173, 239)
    button_color = (255, 215, 0)
    text_color = (0, 173, 239)

    font = pygame.font.Font(None, 24)

    def draw_button(rect, color, text):
        button_text = font.render(text, True, text_color)
        text_rect = button_text.get_rect(center=rect.center)
        pygame.draw.rect(minigame_screen, color, rect)
        pygame.draw.rect(minigame_screen, text_color, rect, 2)
        minigame_screen.blit(button_text, text_rect.topleft)

    back_to_menu_rect = pygame.Rect(10, 10, 150, 50)


    player_size = 50
    player_x = minigame_width // 2 - player_size // 2
    player_y = minigame_height - player_size - 10


    num_enemies = 10
    enemies = [{"x": random.randint(0, minigame_width - player_size), "y": 0} for _ in range(num_enemies)]
    enemy_size = 50
    enemy_speed = 5


    clock = pygame.time.Clock()

    player_speed = 5

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if back_to_menu_rect.collidepoint(mouse_x, mouse_y):
                    pygame.mixer.music.stop()
                    return


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < minigame_width - player_size:
            player_x += player_speed


        for enemy in enemies:
            enemy["y"] += enemy_speed


            if (
                player_x < enemy["x"] + enemy_size
                and player_x + player_size > enemy["x"]
                and player_y < enemy["y"] + enemy_size
                and player_y + player_size > enemy["y"]
            ):
                print("Ai pierdut!")
                return


            if enemy["y"] > minigame_height:
                enemy["x"] = random.randint(0, minigame_width - enemy_size)
                enemy["y"] = 0


        minigame_screen.fill(background)


        pygame.draw.rect(minigame_screen, green, (player_x, player_y, player_size, player_size))
        for enemy in enemies:
            pygame.draw.rect(minigame_screen, red, (enemy["x"], enemy["y"], enemy_size, enemy_size))
        draw_button(back_to_menu_rect, button_color, "INAPOI LA MENIU")


        pygame.display.flip()


        clock.tick(60)


def fereastra_scalare():

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Scalarea")

    pygame.mixer.music.load('Menu-Theme.mp3')
    pygame.mixer.music.play(-1);

    green = (0, 255, 0)
    button_color = (255, 215, 0)
    text_color = (0, 173, 239)

    font = pygame.font.Font(None, 24)

    def draw_button(rect, color, text):
        button_text = font.render(text, True, text_color)
        text_rect = button_text.get_rect(center=rect.center)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, text_color, rect, 2)
        screen.blit(button_text, text_rect.topleft)

    back_to_menu_rect = pygame.Rect(10, 10, 150, 50)


    square_size = 100
    square = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    pygame.draw.rect(square, green, (0, 0, square_size, square_size))

    square_rect = square.get_rect(center=(width // 2, height // 2))


    clock = pygame.time.Clock()

    pulsate_speed = 0.01
    pulsate_amplitude = 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if back_to_menu_rect.collidepoint(mouse_x, mouse_y):
                    pygame.mixer.music.stop()
                    return


        screen.fill((0, 173, 239))


        pulsate_factor = math.sin(pygame.time.get_ticks() * pulsate_speed)
        pulsated_size = int(square_size + pulsate_factor * pulsate_amplitude)


        pulsating_square = pygame.Surface((pulsated_size, pulsated_size), pygame.SRCALPHA)
        pygame.draw.rect(pulsating_square, green, (0, 0, pulsated_size, pulsated_size))
        pulsating_rect = pulsating_square.get_rect(center=square_rect.center)


        screen.blit(pulsating_square, pulsating_rect.topleft)


        draw_button(back_to_menu_rect, button_color, "INAPOI LA MENIU")


        pygame.display.flip()


        clock.tick(60)


def fereastra_rotatie():

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Rotatie")

    pygame.mixer.music.load("Rotating-Theme.mp3")
    pygame.mixer.music.play(-1)


    green = (0, 255, 0)
    button_color = (255, 215, 0)
    text_color = (0, 173, 239)

    font = pygame.font.Font(None, 24)

    def draw_button(rect, color, text):
        button_text = font.render(text, True, text_color)
        text_rect = button_text.get_rect(center=rect.center)
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, text_color, rect, 2)
        screen.blit(button_text, text_rect.topleft)

    back_to_menu_rect = pygame.Rect(10, 10, 150, 50)


    square_size = 100
    square = pygame.Surface((square_size, square_size), pygame.SRCALPHA)
    pygame.draw.rect(square, green, (0, 0, square_size, square_size))

    square_rect = square.get_rect(center=(width // 2, height // 2))


    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if back_to_menu_rect.collidepoint(mouse_x, mouse_y):
                    pygame.mixer.music.stop()
                    return


        screen.fill((0, 173, 239))


        rotated_square = pygame.transform.rotate(square, pygame.time.get_ticks() / 10)
        rotated_rect = rotated_square.get_rect(center=square_rect.center)


        screen.blit(rotated_square, rotated_rect.topleft)


        draw_button(back_to_menu_rect, button_color, "INAPOI LA MENIU")


        pygame.display.flip()


        clock.tick(60)


def fereastra_meniu():
    pygame.mixer.music.load("tetris-theme.mp3")
    pygame.mixer.music.play(-1)

    menu_width, menu_height = 640, 480
    menu_screen = pygame.display.set_mode((menu_width, menu_height))
    pygame.display.set_caption("Meniu")


    background_color = (0, 173, 239)
    button_color = (255, 215, 0)
    text_color = (0, 173, 239)

    font = pygame.font.Font(None, 36)

    def draw_button(rect, color, text):
        button_text = font.render(text, True, text_color)
        text_rect = button_text.get_rect()
        rect.width = text_rect.width + 20
        rect.height = text_rect.height + 10
        pygame.draw.rect(menu_screen, color, rect)
        pygame.draw.rect(menu_screen, (255, 255, 255), rect, 2)
        text_rect.center = rect.center
        menu_screen.blit(button_text, text_rect.topleft)

    welcome_text = font.render("Proiect", True, button_color)
    welcome_rect = welcome_text.get_rect(center=(menu_width // 2, 50))

    button_data = [
        {"rect": pygame.Rect(menu_width // 4, menu_height // 3, menu_width // 2, 50), "text": "SCALARE"},
        {"rect": pygame.Rect(menu_width // 4, 2 * menu_height // 3, menu_width // 2, 50), "text": "ROTATIE"},
        {"rect": pygame.Rect(menu_width // 4, 5 * menu_height // 6, menu_width // 2, 50), "text": "JOCULET"},
        {"rect": pygame.Rect(menu_width // 4, 6 * menu_height // 7, menu_width // 2, 50), "text": "IESIRE"},
    ]

    button_height_spacing = 20

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for button in button_data:
                    if button["rect"].collidepoint(mouse_x, mouse_y):
                        if button["text"] == "SCALARE":
                            fereastra_scalare()
                        elif button["text"] == "ROTATIE":
                            fereastra_rotatie()
                        elif button["text"] == "JOCULET":
                            fereastra_joc()
                        elif button["text"] == "IESIRE":
                            pygame.quit()
                            sys.exit()

        menu_screen.fill(background_color)

        menu_screen.blit(welcome_text, welcome_rect.topleft)


        current_y = button_data[0]["rect"].top
        for button in button_data:
            button["rect"].top = current_y
            draw_button(button["rect"], button_color, button["text"])
            current_y += button["rect"].height + button_height_spacing

        pygame.display.flip()



fereastra_meniu()
