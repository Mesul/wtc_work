import unittest
from unittest.mock import patch
from io import StringIO
import robot


class MyTestCase(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\nmes\nkId\n"))
    def test_get_robot_name(self):
        self.assertEqual(robot.get_robot_name(), "HAL")
        self.assertEqual(robot.get_robot_name(), "mes")
        self.assertEqual(robot.get_robot_name(), "kId")


    def test_do_history(self):
        self.assertEqual(robot.do_history("forward 20"), ["forward 20"])
        self.assertEqual(robot.do_history("forward 10"), ["forward 20", "forward 10"])
        self.assertEqual(robot.do_history("left"), ["forward 20", "forward 10", "left"])
        self.assertEqual(robot.do_history("right"), ["forward 20", "forward 10", "left", "right"])
        self.assertEqual(robot.do_history("forward 5"), ["forward 20", "forward 10", "left", "right", "forward 5"])

    
    def test_do_replay(self):
        self.assertEqual(robot.do_replay("HAL", "replay"), (True, " > HAL replayed 5 commands."))
        self.assertEqual(robot.do_replay("HAL", "replay silent"), (True, " > HAL replayed 5 commands silently."))
        self.assertEqual(robot.do_replay("Lah", "replay 2"), (True, " > Lah replayed 2 commands."))
        self.assertEqual(robot.do_replay("AHL", "replay reversed"), (True, " > AHL replayed 5 commands in reverse."))
        self.assertEqual(robot.do_replay("HAL", "replay 3-2"), (True, " > HAL replayed 1 commands."))
        self.assertEqual(robot.do_replay("I", 'replay reversed silent'), (True, " > I replayed 5 commands in reverse silently."))

    
    def test_do_replay_limit(self):
        self.assertEqual(robot.do_replay_limit("replay", ["forward 20", "forward 10", "left", "right", "forward 5"]), ["forward 20", "forward 10", "left", "right", "forward 5"])
        self.assertEqual(robot.do_replay_limit("replay reverse", ["forward 20", "forward 10", "left", "right", "forward 5"]), ["forward 20", "forward 10", "left", "right", "forward 5"])
        self.assertEqual(robot.do_replay_limit("replay 3", ["forward 20", "forward 10", "left", "right", "forward 5"]), ["left", "right", "forward 5"])
        self.assertEqual(robot.do_replay_limit("replay", ["forward 20", "forward 10", "left", "right", "forward 5"]), ["forward 20", "forward 10", "left", "right", "forward 5"])

    
    def test_get_limit_range(self):
        self.assertEqual(robot.get_limit_range(["replay"]), (False, ""))
        self.assertEqual(robot.get_limit_range(["replay", "3--1"]), (True, "3--1"))
        self.assertEqual(robot.get_limit_range(["replay", "2"]), (True, "2"))
        self.assertEqual(robot.get_limit_range(["replay", "reversed", "4-2"]), (True, "4-2"))
        self.assertEqual(robot.get_limit_range(["replay", "silent", "5-1"]), (True, "5-1"))


    def test_contains_int(self):
        self.assertEqual(robot.contains_int("105"), True)
        self.assertEqual(robot.contains_int("55"), True)
        self.assertEqual(robot.contains_int(""), False)


if __name__ == '__main__':
    unittest.main()