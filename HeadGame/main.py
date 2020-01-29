from multiprocessing import Process, Manager
import sys
import pygame
from time import time, sleep

from FaceClassifier.search_face import face_reader
from GameObjects.setting import Setting
from GameObjects.rival import Rival
from GameObjects.gamer import Gamer
from GameObjects.play import Play


def game(var_global):
    sleep(5)  # check on cam
    setting = Setting()

    pygame.init()
    screen = pygame.display.set_mode((setting.window_width, setting.window_height))
    clock = pygame.time.Clock()

    delta_time = 0.0

    gamer = Gamer(setting.window_width, setting.window_height)
    play = Play()

    static_timer = time()
    rivals = []

    font = pygame.font.SysFont("cambria", 14)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        text_level = font.render(play.get_text_level(), True, (0, 128, 0))
        text_time = font.render(play.get_time_game_in_last_around(), True, (0, 128, 0))

        # rival
        if time() - static_timer > play.get_time_on_create_rival():
            static_timer = time()
            rivals.append(Rival(setting.window_width))

        # ticking
        delta_time += clock.tick()/1000.0
        while delta_time > 1/setting.max_fps:
            delta_time -= 1/setting.max_fps

            # lvl up
            if time() - play.time_level > play.time_on_level:
                play.time_level = time()
                play.increment_level()

            if len(var_global):
                if var_global[-1] > gamer.last_movement and gamer.x - gamer.movement >= 0:
                    gamer.gamer_on_left()
                elif var_global[-1] < gamer.last_movement and gamer.x + gamer.width < setting.window_width:
                    gamer.gamer_on_right()
                gamer.last_movement = var_global[-1]
                del var_global[-1]
            for rival in rivals:
                rival.gamer_on_bottom()
                if (rival.y >= gamer.y and rival.y <= gamer.y + gamer.height) and ((rival.x >= gamer.x and rival.x + rival.width >= gamer.x) and rival.x <= gamer.x + gamer.width):
                        play.clear_game()

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (255, 255, 255), gamer.player)
        for index, rival in enumerate(rivals):
            pygame.draw.rect(screen, (rival.r, rival.g, rival.b), rival.rival)
            if rival.y > setting.window_height:
                del rivals[index]

        screen.blit(text_level, (5, setting.window_height - 20))
        screen.blit(text_time, (setting.window_width - 50, setting.window_height - 20))

        pygame.display.flip()


if __name__ == '__main__':
    var_global = Manager().list()

    process_face = Process(target=face_reader, args=(var_global, ))
    process_game = Process(target=game, args=(var_global, ))

    process_face.start()
    process_game.start()

    process_game.join()
