import sys
from pathlib import Path
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'firmware'))
from core import Vault, TARGETS, DIRECTIONS, PULSES_MS

def solve_orbits(v, now=0):
    v.press(now)
    for target, direction in zip(TARGETS, DIRECTIONS):
        n = 0
        while v.position != target or n == 0:
            now += 10
            v.rotate(direction, now)
            n += 1
        now += 40
        v.press(now)
    return now

def start_pulses(v):
    now = solve_orbits(v)
    v.tick(now + 2600)
    now += 2700
    v.press(now)
    return now

class PuzzleTests(unittest.TestCase):
    def test_boot_is_open(self):
        self.assertFalse(Vault().locked)

    def test_full_solution(self):
        v = Vault()
        now = start_pulses(v)
        for interval in PULSES_MS:
            now += interval
            v.press(now)
        self.assertEqual(v.phase, 'OPEN')
        self.assertFalse(v.locked)

    def test_wrong_direction_rejected(self):
        v = Vault(); v.press(0)
        for n in range(9): v.rotate(-1, n + 1)
        self.assertEqual(v.position, 3)
        v.press(100)
        self.assertEqual(v.phase, 'COOLDOWN')

    def test_wrong_target_rejected(self):
        v = Vault(); v.press(0); v.rotate(1, 20); v.press(40)
        self.assertEqual(v.phase, 'COOLDOWN')

    def test_no_motion_rejected(self):
        v = Vault(); v.press(0); v.press(40)
        self.assertEqual(v.phase, 'COOLDOWN')

    def test_failure_restarts_whole_puzzle(self):
        v = Vault(); v.press(0); v.press(40); v.tick(1540)
        self.assertEqual((v.phase, v.stage, v.position), ('ORBIT', 0, 0))
        self.assertTrue(v.locked)

    def test_playback_ignores_taps(self):
        v = Vault(); now = solve_orbits(v)
        v.press(now + 200)
        self.assertEqual(v.phase, 'PLAYBACK')

    def test_timeout_without_last_tap(self):
        v = Vault(); now = start_pulses(v); v.tick(now + 631)
        self.assertEqual(v.phase, 'COOLDOWN')

    def test_boundary_acceptance(self):
        for error in (-180, 180):
            v = Vault(); now = start_pulses(v)
            for interval in PULSES_MS:
                now += interval + error
                v.press(now)
            self.assertEqual(v.phase, 'OPEN')

    def test_outside_boundary_rejected(self):
        for error in (-181, 181):
            v = Vault(); now = start_pulses(v); v.press(now + 450 + error)
            self.assertEqual(v.phase, 'COOLDOWN')

    def test_reset_always_opens(self):
        for phase in ('READY','ORBIT','PLAYBACK','ARM','PULSE','COOLDOWN','OPEN'):
            v = Vault(); v.phase = phase; v.locked = True; v.reset(500)
            self.assertEqual(v.phase, 'READY'); self.assertFalse(v.locked)

    def test_pixel_power_cap_all_phases(self):
        v = Vault(); v.playback_start = 0
        for phase in ('READY','ORBIT','PLAYBACK','ARM','PULSE','COOLDOWN','OPEN'):
            v.phase = phase
            for now in range(0, 3000, 37):
                pixels = v.lights(now)
                self.assertEqual(len(pixels), 12)
                self.assertTrue(all(0 <= c <= 32 for p in pixels for c in p))

    def test_arm_timeout(self):
        v = Vault(); now = solve_orbits(v); v.tick(now + 2600); v.tick(now + 17600)
        self.assertEqual(v.phase, 'COOLDOWN')

    def test_rotation_wraps_both_directions(self):
        v = Vault(); v.press(0); v.rotate(-1,10)
        self.assertEqual(v.position,11)
        v.rotate(1,20); self.assertEqual(v.position,0)

    def test_event_log_is_bounded(self):
        v = Vault(); v.press(0)
        for i in range(200): v.rotate(1,i)
        self.assertEqual(len(v.events),40)

if __name__ == '__main__': unittest.main(verbosity=2)
