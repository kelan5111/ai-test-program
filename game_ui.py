import pygame
from coordinate import Coordinate


class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, waypoint_graph, *groups: pygame.sprite.Group):
        super().__init__(*groups)
        self._coord = Coordinate(x, y)
        self._width = width
        self._height = height

        self.image = pygame.transform.scale(pygame.image.load("assets/images/ninja.png"),
                                            (self._width, self._height))
        self.rect = self.image.get_rect()

        self._waypoint_graph = waypoint_graph
        self._target_waypoint = None
        self._curr_waypoint = None
        self._path = None
        self._collected_coins = 0
        self._speed = speed

        self.set_path(Coordinate(1, 1))

        self._moving = False

    def draw(self, screen):
        screen.blit(self.image, (self._coord.get_x(), self._coord.get_y()))

    def update(self):
        self._update_image()

    def _update_image(self):
        self.rect.center = (self._coord.get_x(), self._coord.get_y())

    def _execute_player_movement(self):
        if self._target_waypoint is None:
            if self._path:
                self._target_waypoint = self._path.pop()

                self._moving = False
                return

        target_coord = self._target_waypoint.get_coord()

        if self._coord == target_coord:
            self._curr_waypoint = self._target_waypoint
            self._target_waypoint = None
            return

        next_coord = self._calc_next_move(target_coord)

        if next_coord is not None:
            self._target_waypoint = next_coord

    def set_path(self, target_coord=None, waypoint_id=None):
        if target_coord is not None:  # If we want to move to a certain coord (find the closest waypoint)
            self._target_waypoint = self._waypoint_graph.find_nearest_waypoint(target_coord)
            path = self._waypoint_graph.build_path([self._target_waypoint], waypoint_id, self._curr_waypoint,
                                                   self._target_waypoint)
        else:
            path = self._waypoint_graph.build_path([], waypoint_id, self._curr_waypoint, None)

        if path is not None:
            self._moving = True
            self._path = path
            self._target_waypoint = None
        else:
            self._moving = False

    def _calc_next_move(self, target_coord):
        step = 1
        target_x = target_coord[0]
        target_y = target_coord[1]
        curr_x = self._coord.get_x()
        curr_y = self._coord.get_y()

        if curr_x < target_x:
            curr_x += (step * self._speed)
        elif curr_x > target_x:
            curr_x -= (step * self._speed)

        if curr_y < target_y:
            curr_y += (step * self._speed)
        elif curr_y > target_y:
            curr_y -= (step * self._speed)

        return Coordinate(curr_x, curr_y)

    def collect(self, target_coord):
        self.rect.collidepoint(target_coord)
