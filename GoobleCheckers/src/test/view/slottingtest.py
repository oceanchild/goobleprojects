'''
Created on 2011-11-26

@author: Gooble
'''
import unittest
from main.view.boardcoordinate import BoardCoordinate

class SlottingTest(unittest.TestCase):

    def test_slotting_case_all_coordinates_in_first_row_first_cell(self):
        self.check_slot_in_entire_cell_range(0, 60, 0, 60, 0, 0)
        
    def test_slotting_case_all_coordinates_in_first_row_second_cell(self):
        self.check_slot_in_entire_cell_range(60, 120, 0, 60, 0, 1)
        
    def test_slotting_case_3(self):
        self.check_slot(1, 40, 0, 0)    
        
    def test_slotting_case_final_cell_very_corner_gives_invalid_coordinate(self):
        self.check_slot(480, 480, 8, 8)
        
    def check_slot_in_entire_cell_range(self, xrangestart, xrangeend, yrangestart, yrangeend, expected_row, expected_col):
        for x in range(xrangestart, xrangeend):
            for y in range(yrangestart, yrangeend):
                self.check_slot(x, y, expected_row, expected_col)
            
    def check_slot(self, canvasx, canvasy, row, col):
        position = BoardCoordinate(canvas_size=(480, 480), board_size=(8, 8)).get_from(x=canvasx, y=canvasy)
        self.assertEqual((row, col), position, "failed for values: canvas=" + str((canvasx, canvasy)) + "row=" + str(row) + "col=" + str(col) + " got instead: " + str(position))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()