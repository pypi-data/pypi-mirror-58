from factorygame import GameEngine, GameplayStatics
from factorygame.core.blueprint import WorldGraph, GridGismo

class FactoryEngine(GameEngine):
    """Game engine class for factories."""

    def __init__(self):

        # Set default properties.
        self._window_title      = "FactoryGame"
        self._frame_rate        = 90
        self._starting_world    = WorldGraph

    def begin_play(self):
        GameplayStatics.world.spawn_actor(GridGismo, (0, 0))
