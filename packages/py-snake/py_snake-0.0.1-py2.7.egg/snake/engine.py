import time


class Clock:
    def __init__(self, interval, on_tick=None, on_wait=None, on_stop=None):
        self.interval = interval
        self.tick_callback = on_tick if on_tick else self._noop
        self.wait_callback = on_wait if on_wait else self._noop
        self.stop_callback = on_stop if on_stop else self._noop
        self.running = False
        self.t0 = time.time()

    @staticmethod
    def _noop(): pass

    def _tick(self):
        self.t0 = time.time()
        self.tick_callback()

    def _wait(self):
        self.wait_callback()

    def _stop(self):
        self.stop_callback()

    def start(self):
        self.running = True
        while self.running:
            self._tick()
            while self.timedelta < self.interval:
                self._wait()
        self._stop()

    def stop(self):
        self.running = False

    @property
    def timedelta(self):
        return time.time() - self.t0


class EngineState:
    INSTANTIATED = 0
    STARTING = 1
    RUNNING = 2
    ENDING = 3
    FINISHED = 4

    legal_transitions = {
        INSTANTIATED: (STARTING,),
        STARTING: (RUNNING, ENDING),
        RUNNING: (ENDING,),
        ENDING: (FINISHED,),
        FINISHED: (STARTING,)
    }

    def __init__(self):
        self.state = self.INSTANTIATED

    def update(self, new_state):
        if new_state not in self.legal_transitions[self.state]:
            raise RuntimeError("Illegal state transition.")
        self.state = new_state

    def __eq__(self, other):
        return True if self.state == other else False


class GameEngine(object):
    def __init__(self, speed):
        self.initial_speed = speed
        self._speed = speed
        self.state = EngineState()
        self.start_time = time.time()
        self.clock = Clock(self.tick_interval, on_tick=self._update, on_wait=self._wait)

    def start_game(self):
        self.state.update(EngineState.STARTING)
        self.game_will_begin()
        self.clock.start()

    def stop_game(self):
        self.state.update(EngineState.ENDING)
        self.game_will_end()
        self.clock.stop()
        self.state.update(EngineState.FINISHED)
        self.game_did_end()

    def _update(self):
        if self.state == EngineState.STARTING:
            self.state.update(EngineState.RUNNING)
            self.game_did_begin()

        elif self.state in (EngineState.RUNNING, EngineState.ENDING):
            self.game_should_update_frame()

    def _wait(self):
        time.sleep(1 / 60)
        self.game_should_capture_input()

    @property
    def elapsed_time(self):
        return time.time() - self.start_time

    @property
    def tick_interval(self):
        return 1 / self.speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value
        self.clock.interval = self.tick_interval

    # These hooks should be implemented in the subclass

    def game_will_begin(self):
        pass

    def game_did_begin(self):
        pass

    def game_should_update_frame(self):
        pass

    def game_should_capture_input(self):
        pass

    def game_will_end(self):
        pass

    def game_did_end(self):
        pass
