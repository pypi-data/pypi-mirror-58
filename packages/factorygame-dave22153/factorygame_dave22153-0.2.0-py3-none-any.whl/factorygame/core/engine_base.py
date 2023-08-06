"""Game engine for FactoryGame."""

from tkinter import Tk
from factorygame.core.input_base import EngineInputMappings
from factorygame.core.input_tk import TkInputHandler
from factorygame.utils.loc import Loc
from factorygame.utils.gameplay import GameplayStatics

class EngineObjectBase(object):
    """
    Low level implementation of EngineObjectBase, should not be used directly
    in game code.
    """
    pass

class EngineObject(EngineObjectBase):
    """
    Base object for all Engine objects. Provides basic gameplay functions
    that can be overridden in children.
    """

    def begin_play(self):
        """
        Called when this object has been successfully initialised
        and it is safe to call gameplay functions from this point on
        """
        pass

    def begin_destroy(self):
        """
        Called before this object will be destroyed.
        """
        pass

class GameEngine(EngineObject):
    """
    High level engine object that initialises other components when the
    game is created.
    """

    WINDOW_TITLE = property(lambda self: self._window_title)
    FRAME_RATE   = property(lambda self: self._frame_rate) # in frames per second
    FRAME_TIME   = property(lambda self: 1000 // self.FRAME_RATE) # in miliseconds

    def __init__(self):
        """Initialise game engine in widget MASTER. If omitted a new window is made."""

        ## Name to use in window title.
        self._window_title      = "engine_base"

        ## Number of times to update game per second.
        self._frame_rate        = 30

        ## Class to use for initial world creation. If omitted default world will be used.
        self._starting_world    = None

    def __init_game_engine__(self, master=None):
        """
        Create the game engine. Shouldn't be called directly, call
        from GameplayUtilities instead.
        """

        # Set central reference to game engine.
        GameplayStatics.set_game_engine(self)


        # Create/setup the game window.

        if master is None:
            # Create window for game.
            self._window = Tk()
            self._window.title(self.WINDOW_TITLE)
        else:
            # Use existing window.
            # Doesn't guarantee that it is a Toplevel widget.
            self._window = master

        # Set reference to the window.
        GameplayStatics.set_root_window(self._window)


        # Create input binding objects.
        
        # TODO: There needs to be a safer way to instantiate EngineObjects

        # Let action mappings be added.
        self._input_mappings = EngineInputMappings()

        # Create GUI input receiver.
        self._input_handler = TkInputHandler()
        self._input_handler.bind_to_widget(GameplayStatics.root_window)

        # Override in child game engines to set up the action mappings,
        # possibly from a config file.
        self.setup_input_mappings()


        # Create the starting world.

        if self._starting_world is None:
            # Choose default world if not specified.
            self._starting_world = World

        # try:
        world = self._starting_world()
        world.__init_world__(self._window)
        GameplayStatics.set_world(world)
        world.begin_play()
        # except AttributeError as e:
        #     # The starting world is not a valid class.
        #     raise AttributeError("Starting world '%s' for engine '%s' is not valid. %s"
        #         % (self._starting_world.__name__, type(self).__name__, e)) from e


        # Call begin play.
        self.begin_play()

        # Start game window tkinter event loop.        

        if master is None:
            return self._window.mainloop()

    def setup_input_mappings(self):
        """
        Set up input mappings associated with a set of keys.
        """
        pass

    def close_game(self):
        """
        Close the game engine. Shouldn't be called directly, call
        from GameplayUtilities instead.
        """
        if not GameplayStatics.is_game_valid():
            return

        # Attempt to close game window.
        if self._window is not None and self._window.winfo_exists():
            # It does exist. Close it.
            self._window.destroy()
        
        # Delete world and all actors.
        world = GameplayStatics.world
        if world is not None:
            world.begin_destroy()

        # Begin destroying self.
        self.begin_destroy()

        # Delete gameplay statics, which holds many references.
        GameplayStatics.clear_all()

    @property
    def input_mappings(self):
        return self._input_mappings

class World(EngineObject):
    """
    Manages all content that makes up a level as well as keeping
    track of all dynamically spawned actors and triggering core
    gameplay events such as tick.
    """

    def __init__(self):
        """Set default values."""


        ## All spawned actors to receive tick events, grouped by tick priority.
        self._ticking_actors = {
            # Create an actor set for each ticking group.
            group: set() for group in range(ETickGroup.MAX)
            }

        ## All spawned actors in the world.
        self._actors            = []

        ## List of actors to destroy next tick.
        self._to_destroy        = []

        ## Tkinter object reference for tick loop timer.
        self._tk_obj            = None

    def __init_world__(self, tk_obj):
        """Initialise world with any active tkinter object TK_OBJ."""

        # Prepare for starting tick timer.
        self._tk_obj = tk_obj
        self.__try_start_tick_loop()

    def spawn_actor(self, actor_class, loc):
        """
        Attempt to initialise a new actor in this world, from start
        to finish.

        To have further control on the actor before it is gameplay ready,
        use deferred_spawn_actor.

        * actor_class: Class of actor to spawn
        * loc: Location to spawn actor at.

        * return: Spawned actor if successful, otherwise None
        """

        actor_object = self.deferred_spawn_actor(actor_class, loc)
        return (self.finish_deferred_spawn_actor(actor_object)
                if actor_object else None)

    def deferred_spawn_actor(self, actor_class, loc):
        """
        Begin to initialise a new actor in this world, then allow
        attributes to be set before finishing the spawning process.

        Warning: It is not safe to call any gameplay functions (eg tick)
        or anything involving the world because the actor is not officially
        in the world yet.

        * actor_class: class of actor to spawn
        * loc: location to spawn actor at

        * return: initialised actor object if successful, otherwise None
        """

        # validate actor_class to check it is valid
        if actor_class is None:
            return None

        # initialise new actor object
        actor_object = actor_class()
        actor_object.__spawn__(self, Loc(loc))

        # return the newly created actor_object for further modification and
        # to pass in to finish_deferred_spawn_actor
        return actor_object

    def finish_deferred_spawn_actor(self, actor_object):
        """
        Finish spawning an actor in this world, allowing gameplay
        functions to safely begin for the actor.

        * actor_object: initialised actor object to finish spawning

        * return: gameplay ready actor object if successful, otherwise None
        """

        # validate actor_object to check that it is valid
        if actor_object is None:
            return None

        # update world references
        actor_object._world = self
        self._actors.append(actor_object)

        # call begin play
        actor_object.begin_play()

        # schedule ticks if necessary
        # if actor_object.primary_actor_tick.start_with_tick_enabled:
        #     self.set_actor_tick_enabled(actor_object, True)

        # return the fully spawned actor for further use
        return actor_object

    def destroy_actor(self, actor):
        """
        Remove an actor from this world.

        :warning: EXPERIMENTAL FEATURE!!! MAY NOT WORK!!!

        :param actor: (Actor) Actor to destroy.
        """

        # TODO:  check if the actor is actually in this world!

        self._to_destroy.append(actor)

    def _destroy_pending(self):
        """
        Called to remove actors pending destruction.
        """

        for actor in self._to_destroy:
            actor.begin_destroy()
            self._actors.remove(actor)

        # Clear pending destruction. It's done already!
        self._to_destroy = []

    def __try_start_tick_loop(self):
        """
        Attempt to start a tick loop.

        :return bool: Whether the tick loop was started successfully.
        """
        if not self._tk_obj:
            return False

        self._tick_loop()
        return True        

    def _tick_loop(self):
        # Perform actor cleanup.
        self._destroy_pending()

        # get delta time
        dt = GameplayStatics.game_engine.FRAME_TIME # in miliseconds, as integer

        # call tick event on other actors
        for group in range(ETickGroup.MAX):
            # Call the groups in order.
            actor_set = self._ticking_actors[group]
            for actor in actor_set:
                actor.tick(dt)

        # schedule next tick
        self._tk_obj.after(dt, self._tick_loop)

    def set_actor_tick_enabled(self, tick_function, new_tick_enabled):
        """
        Set whether an actor should tick and schedule/cancel tick events
        for the future.
        
        Shouldn't be called directly, call from the actor itself. Use actor's
        tick_function like `primary_actor_tick.tick_enabled`.

        :param tick_function: (FTickFunction) Data about the tick function to
        modify.
        """

        actor = tick_function.target

        # Ensure we are adding a valid actor with a valid tick function.
        try:
            func = actor.tick
        except AttributeError:
            return
        else:
            if not callable(func):
                return

        if new_tick_enabled:
            # Add the actor to its specified tick group's actor set.

            try:
                group = self._ticking_actors[tick_function.tick_group]
            except KeyError:
                return
            else:
                group.add(actor)

        else:
            # Remove the actor from its tick group's actor set.

            try:
                group = self._ticking_actors[tick_function.tick_group]
            except KeyError:
                return
            else:
                try:
                    group.remove(actor)
                except KeyError:
                    pass

    def begin_destroy(self):
        """Destroy all actors."""
        for actor in self._actors:
            actor.begin_destroy()
            self._actors.pop(0)
        
        self._ticking_actors = {group: set() for group in range(ETickGroup.MAX)}
            # try:
            #     self._ticking_actors.remove(actor)
            # except KeyError:
            #     pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Start of tick data structures

class ETickGroup:
    """Groups for ticking objects. Lower value groups are fired first."""
    ENGINE  = 0
    WORLD   = 1
    PHYSICS = 2
    GAME    = 3
    UI      = 4

    MAX     = 5

class FTickFunction:
    """
    Contains data about how a particular object should tick.
    """

    @property
    def tick_enabled(self):
        return self._tick_enabled

    @tick_enabled.setter
    def tick_enabled(self, value):
        if self.target is None: return

        world = GameplayStatics.world
        if world is None: return

        if value:
            self.register_tick_function(world)
            self._tick_enabled = True
            return

        self.unregister_tick_function(world)
        self._tick_enabled = False

    def __init__(self, target=None):
        """
        Set reasonable defaults.

        :param target: (Actor) Object containing `tick` method.
        """
        self.target = target
        self.can_ever_tick = True
        self.start_with_tick_enabled = True
        self.tick_group = ETickGroup.GAME
        self.priority = 1

        self._tick_enabled = False

        # Pausing is not implemented yet.
        self.tick_even_when_paused = False

    def register_tick_function(self, world):
        """
        Register a tick function in the given world.

        :param world: (World) World containing master list.

        :see: Setter for tick_enabled.
        """
        if self.target is None: return

        try:
            world.set_actor_tick_enabled(self, True)
        except AttributeError:
            raise RuntimeWarning("Tried to register tick function on invalid world")

    def unregister_tick_function(self, world):
        """
        Unregister the tick function from the master
        list of tick functions.

        :param world: (World) World containing master list.

        :see: Setter for tick_enabled.
        """
        if self.target is None: return

        try:
            world.set_actor_tick_enabled(self, False)
        except AttributeError:
            raise RuntimeWarning("Tried to unregister tick function on invalid world")

# End of tick data structures
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Actor(EngineObject):
    """
    An object that has a visual representation in the world. Actors
    are directly managed by a world object and should only be created
    by using spawn_actor functions from the current world.
    """

    world = property(lambda self: self._world)
    location = property(lambda self: self.__get_location(),
        lambda self, value: self.__set_location(value))

    def __get_location(self):
        return self._location
    def __set_location(self, value):
        self._location = Loc(value)

    def __spawn__(self, world, location):
        """Called when actor is spawned by world. Shouldn't be called directly."""

        ## World actor is in.
        self._world = world

        ## Location of actor in world.
        self._location = location

        # Register the tick function for this actor.
        try:
            tick_func = self.primary_actor_tick
        except AttributeError:
            pass
        else:
            if tick_func.can_ever_tick:
                tick_func.target = self
                tick_func.tick_enabled = tick_func.start_with_tick_enabled

    def __init__(self):
        ## Tick options for this actor. Can be further modified by children.
        self.primary_actor_tick = FTickFunction()

    def tick(self, delta_time):
        """
        Called every frame if the actor is set to tick.
        delta_time: time since last frame, in seconds
        """
        raise NotImplementedError("Actor %s has tick enabled but default tick "
              "function is being called" % self)

    def begin_destroy(self):
        super().begin_destroy()
        
        # Stop ticking
        self.world.set_actor_tick_enabled(self.primary_actor_tick, False)
