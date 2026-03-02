import pygame

from waypoint import Graph
from game_ui import NPC

pygame.init()


class AiProgram:
    def __init__(self, width, height):
        self.__running = True
        self.__screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        self.__clock = pygame.time.Clock()
        self.__waypoint_graph = Graph(width, height, width // 10)
        self.__group = pygame.sprite.Group()
        self.__character = NPC(0, 0, 100, 100, 10,
                               self.__waypoint_graph, self.__group)

    def run(self):
        while self.__running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False

            self.__screen.fill((0, 51, 51))

            self.__group.update()
            self.__group.draw(self.__screen)

            self.__waypoint_graph.draw(self.__screen)

            pygame.display.flip()
            self.__clock.tick()

        pygame.quit()


def main():
    width, height = pygame.display.get_desktop_sizes()[0]

    ai = AiProgram(width, height)
    ai.run()


if __name__ == '__main__':
    main()
