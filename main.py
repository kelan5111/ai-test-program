import pygame

from graph import Graph

pygame.init()


class AiProgram:
    def __init__(self, width, height):
        self.__running = True
        self.__screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        self.__clock = pygame.time.Clock()

        self.__graph = Graph(width, height, width // 10)

    def run(self):
        self.__graph.build()

        while self.__running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False

            self.__screen.fill((0, 51, 51))

            self.__graph.draw(self.__screen)

            pygame.display.flip()
            self.__clock.tick()

        pygame.quit()


def main():
    width, height = pygame.display.get_desktop_sizes()[0]

    ai = AiProgram(width, height)
    ai.run()


if __name__ == '__main__':
    main()
