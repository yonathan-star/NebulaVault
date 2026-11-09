"""Nebula Vault puzzle engine. Original project by Yonathan. No hardware dependencies."""

TARGETS = (3, 8, 1)
DIRECTIONS = (1, -1, 1)
PULSES_MS = (450, 900, 450)
TOLERANCE_MS = 180


class Vault:
    def __init__(self):
        self.phase = 'READY'
        self.position = 0
        self.stage = 0
        self.travel = 0
        self.last_direction = 0
        self.deadline = 0
        self.last_tap = None
        self.pulse_index = 0
        self.message = 'PRESS TO ARM'
        self.locked = False
        self.events = []

    def event(self, now, kind):
        self.events.append((now, kind))
        self.events = self.events[-40:]

    def reset(self, now):
        self.__init__()
        self.event(now, 'reset_unlocked')

    def fail(self, now, reason):
        self.phase = 'COOLDOWN'
        self.deadline = now + 1500
        self.message = reason
        self.event(now, 'reject:' + reason)

    def rotate(self, delta, now):
        if self.phase != 'ORBIT' or not delta:
            return
        self.position = (self.position + delta) % 12
        self.travel += abs(delta)
        self.last_direction = 1 if delta > 0 else -1
        self.message = 'ORBIT %d  POS %02d' % (self.stage + 1, self.position)
        self.event(now, 'rotate:%d' % delta)

    def press(self, now):
        self.tick(now)
        if self.phase == 'READY':
            self.phase = 'ORBIT'
            self.locked = True
            self.stage = 0
            self.travel = 0
            self.message = 'ORBIT 1  CW > 03'
            self.event(now, 'armed')
        elif self.phase == 'ORBIT':
            if (self.position != TARGETS[self.stage]
                    or self.last_direction != DIRECTIONS[self.stage]
                    or self.travel < 1):
                self.fail(now, 'SIGNAL LOST')
                return
            self.stage += 1
            self.travel = 0
            if self.stage == len(TARGETS):
                self.phase = 'PLAYBACK'
                self.playback_start = now
                self.deadline = now + 2600
                self.message = 'WATCH THE PULSE'
                self.event(now, 'orbits_solved')
            else:
                self.message = 'ORBIT %d  %s > %02d' % (
                    self.stage + 1, 'CW' if DIRECTIONS[self.stage] > 0 else 'CCW',
                    TARGETS[self.stage])
        elif self.phase == 'ARM':
            self.phase = 'PULSE'
            self.last_tap = now
            self.pulse_index = 0
            self.deadline = now + PULSES_MS[0] + TOLERANCE_MS + 1
            self.message = 'PULSE 1 / 3'
            self.event(now, 'pulse_start')
        elif self.phase == 'PULSE':
            elapsed = now - self.last_tap
            expected = PULSES_MS[self.pulse_index]
            if abs(elapsed - expected) > TOLERANCE_MS:
                self.fail(now, 'PULSE MISMATCH')
                return
            self.last_tap = now
            self.pulse_index += 1
            if self.pulse_index == len(PULSES_MS):
                self.phase = 'OPEN'
                self.locked = False
                self.message = 'CORE RECOVERED'
                self.event(now, 'unlocked')
            else:
                self.deadline = now + PULSES_MS[self.pulse_index] + TOLERANCE_MS + 1
                self.message = 'PULSE %d / 3' % (self.pulse_index + 1)
        elif self.phase == 'OPEN':
            self.reset(now)

    def tick(self, now):
        if self.phase == 'PLAYBACK' and now >= self.deadline:
            self.phase = 'ARM'
            self.deadline = now + 15000
            self.message = 'TAP THEN REPEAT'
        elif self.phase in ('PULSE', 'ARM') and now >= self.deadline:
            self.fail(now, 'PULSE TIMEOUT')
        elif self.phase == 'COOLDOWN' and now >= self.deadline:
            self.phase = 'ORBIT'
            self.stage = 0
            self.position = 0
            self.travel = 0
            self.last_direction = 0
            self.message = 'ORBIT 1  CW > 03'

    def lights(self, now):
        """RGB 0..32 per channel. Absolute cap bounds load even on solid white."""
        colors = [(0, 0, 0)] * 12
        if self.phase in ('READY', 'OPEN'):
            return [(0, 20, 12)] * 12
        if self.phase == 'COOLDOWN':
            return [(28, 0, 0)] * 12
        if self.phase == 'PLAYBACK':
            elapsed = now - self.playback_start
            times = (300, 750, 1650, 2100)
            if any(t <= elapsed < t + 130 for t in times):
                return [(24, 24, 24)] * 12
        if self.phase == 'ORBIT':
            colors[self.position] = (0, 14, 30)
            for i in range(self.stage):
                colors[TARGETS[i]] = (10, 24, 0)
        elif self.phase in ('ARM', 'PULSE'):
            colors = [(10, 0, 20)] * 12
        return colors
