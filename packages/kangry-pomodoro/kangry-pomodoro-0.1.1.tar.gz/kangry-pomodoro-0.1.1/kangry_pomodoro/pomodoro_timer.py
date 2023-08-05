import time

from threading import Timer
from enum import Enum


class Event(list):
    def __call__(self, *args, **kwargs):
        for f in self:
            f(*args, **kwargs)

    def __repr__(self):
        return "Event(%s)" % list.__repr__(self)


class PomodoroState(Enum):
    Stopped = 1
    WorkTime = 2
    ShortBreak = 3
    LongBreak = 4
    Pause = 5


class Pomodoro:
    work_time = 30 * 60
    short_break_time = 5 * 60
    long_break_time = 25 * 60

    _state: PomodoroState = PomodoroState.Stopped
    _previous_state: PomodoroState = None
    _timer: Timer = None

    # Переменная для определения какой перерыв делать после `WorkTime`
    _loop_count = 1

    # Для отображения оставшегося времени
    # прим. есть некоторый рассинхрон с таймером
    _timer_launch_time = 0.0
    _timer_stopped_time = 0.0

    state_changed_event = Event()
    time_out_event = Event()

    @property
    def state(self) -> PomodoroState:
        return self._state

    @state.setter
    def state(self, state: PomodoroState):
        self._state = state
        self.state_changed_event(self, previous_state=self._previous_state, state=self.state)

    def _transition_to(self, state: PomodoroState):
        """Изменяет состояние системы"""
        # state.transition()
        if self.state is PomodoroState.Pause:
            time_left = self.work_time - (self._timer_stopped_time - self._timer_launch_time)
            self._timer = Timer(time_left, self._time_out)
        elif state is PomodoroState.WorkTime:
            self._timer = Timer(self.work_time, self._time_out)
        elif state is PomodoroState.ShortBreak:
            self._timer = Timer(self.short_break_time, self._time_out)
        elif state is PomodoroState.LongBreak:
            self._timer = Timer(self.long_break_time, self._time_out)

        self._previous_state = self.state
        self.state = state

    def _time_out(self):
        """Вызывается при срабатывании таймера"""
        self.stop()
        self.time_out_event(state=self._previous_state)

    def start(self):
        """Запускает работу таймера"""

        # !!! Изменить состояние перед запуском таймера
        if self.state is PomodoroState.Stopped:
            if self._previous_state is PomodoroState.WorkTime:
                if self._loop_count % 4 == 0:
                    self._transition_to(PomodoroState.LongBreak)
                else:
                    self._transition_to(PomodoroState.ShortBreak)
            else:
                self._transition_to(PomodoroState.WorkTime)
        elif self.state is PomodoroState.Pause:
            self._transition_to(PomodoroState.WorkTime)
        else:
            # Если система не в состоянии `Stopped` или `Pause`, то таймер уже работает и делать ничего не нужно
            return

        self._timer.start()
        if self._previous_state is not PomodoroState.Pause:
            self._timer_launch_time = time.time()

    def stop(self):
        """Останавливает таймер"""
        self._timer.cancel()
        self._timer_stopped_time = time.time()

        # Изменить состояние
        if self.state in [PomodoroState.WorkTime, PomodoroState.LongBreak, PomodoroState.ShortBreak]:
            self._transition_to(PomodoroState.Stopped)

    def get_time(self) -> float:
        """Возвращает оставшееся время"""
        if self.state is PomodoroState.WorkTime:
            t = self.work_time - (time.time() - self._timer_launch_time)
        elif self.state is PomodoroState.ShortBreak:
            t = self.short_break_time - (time.time() - self._timer_launch_time)
        elif self.state is PomodoroState.LongBreak:
            t = self.long_break_time - (time.time() - self._timer_launch_time)
        elif self.state is PomodoroState.Pause:
            t = self.work_time - (self._timer_stopped_time - self._timer_launch_time)
        else:
            t = 0
        return t

    def pause(self):
        """Приостанавливает таймер"""
        self._timer.cancel()
        self._timer_stopped_time = time.time()

        if self.state is PomodoroState.WorkTime:
            self._transition_to(PomodoroState.Pause)

    def continue_work(self):
        """Продолжает работу таймера после паузы или после перерыва"""
        self.start()
