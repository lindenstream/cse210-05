from game.casting.actor import Actor


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._counter = 0
        self.add_counter(0)
        self._is_playing = True

    def add_counter(self, counter):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._counter += counter
        self.set_text(f"Timer: {self._counter}")

    def get_counter(self):
        """Returns the counter.
        
        """
        return self._counter

    def stop_counter(self):
        self._is_playing = False

    def is_playing(self):
        return self._is_playing
