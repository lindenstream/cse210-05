import constants
from game.casting.actor import Actor
from game.casting.cycle import Cycle
from game.shared.point import Point


class Cycle1(Cycle):
    """
    A single cycle.
    
    The responsibility of Cycle1 is to start in a different spot that Cycle2.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def _prepare_body(self):
        # prepares the cycle body location
        x = int(constants.MAX_X / 4)
        y = int(constants.MAX_Y / 4)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.TEAL if i == 0 else constants.PINK
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def grow_tail(self, number_of_segments):
        # increases size of light tail
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.PINK)
            self._segments.append(segment)