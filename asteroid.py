import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_vel = random.uniform(20,50)
            vel1 = self.velocity.rotate(new_vel)
            vel2 = self.velocity.rotate(-new_vel)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            aster1 = Asteroid(self.position.x, self.position.y, new_radius)
            aster2 = Asteroid(self.position.x, self.position.y, new_radius)
            aster1.velocity = vel1 * 1.2
            aster2.velocity = vel2 * 1.2
