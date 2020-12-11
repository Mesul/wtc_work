import unittest
from unittest.mock import patch
from io import StringIO
import robot
 

class MyTestCase(unittest.TestCase):
    @patch("sys.stdin", StringIO("HAL\nmes\nkId\n"))
    def test_robot_name(self):
        self.assertEqual(robot.robot_name(), "HAL")
        self.assertEqual(robot.robot_name(), "mes")
        self.assertEqual(robot.robot_name(), "kId")


    def test_robot_commands(self):
        self.assertEqual(robot.robot_commands("Hal", "forward 10"), False)
        self.assertEqual(robot.robot_commands("Hal", "back 50"), False)
        self.assertEqual(robot.robot_commands("Hal", "right"), False)
        self.assertEqual(robot.robot_commands("Hal","left"), False)
        self.assertEqual(robot.robot_commands("Hal", "off"), True)


    @patch("sys.stdin", StringIO("forward 10\nright\nwongal\n"))
    def test_get_command(self):
        self.assertEqual(robot.get_command("Hal"), "forward 10")
        self.assertEqual(robot.get_command("Hal"), "right")
        self.assertEqual(robot.get_command("Hal"), "")


    def test_forward_command(self):
        self.assertEqual(robot.forward_command(20, "Hal"), (0, -70))
        self.assertEqual(robot.forward_command(30, "Hal"), (0, -40))
        self.assertEqual(robot.forward_command(80, "Hal"), (0, 40))


    def test_back_command(self):
        self.assertEqual(robot.back_command(30, "Hal"), (0, -30))
        self.assertEqual(robot.back_command(60, "Hal"), (0, -90))


    def test_right_command(self):
        self.assertEqual(robot.right_command("right", "Hal"), (0, 40))
        self.assertEqual(robot.right_command("right", "Hal"), (0, 40))
    

    def test_left_command(self):
        self.assertEqual(robot.left_command("left", "Hal"), (0, 40))
        self.assertEqual(robot.left_command("left", "Hal"), (0, 40))


    def test_sprint_command(self):
        self.assertEqual(robot.sprint_command(10, "Hal"), (0, 55))
        self.assertEqual(robot.sprint_command(15, "Hal"), (0, 175))

   
if __name__ == "__main__":
    unittest.main()

