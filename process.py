print("New process")
import sys

class PatternPrinter:
    def __init__(self, int_val:str) -> None:
        try:
            self.number_of_rows = PatternPrinter._is_positive_integer(int_val)
            self.final_pattern_list = []
        except ValueError as e:
            print(f"Input is not valid, Please re-run with valid input. - {e}")
            sys.exit(1)
    
    @staticmethod
    def _is_positive_integer(input_val:str) -> int:
        check_val = int(input_val)
        if check_val < 0:
            raise ValueError("Value is less than 0.")
        else:
            return check_val
    
    def generate_pattern(self):
        if self.number_of_rows == 1:
            self.final_pattern_list = self.generate_pattern_for_one_row()
        elif self.number_of_rows == 2:
            self.final_pattern_list = self.generate_pattern_for_2_row()
        else:
            self.final_pattern_list = self.generate_pattern_for_2_row()
            for index in range(3, self.number_of_rows+1):
                calculated_row_list = self.generate_pattern_for_next_row(self.final_pattern_list[-1])
                self.final_pattern_list.append(calculated_row_list)
        
        self.print_output()

    def generate_pattern_for_one_row(self):
        return [[1]]

    def generate_pattern_for_2_row(self):
        return [[1], [1,1]]
    
    def generate_pattern_for_next_row(self, previous_row_list:list) -> list:
        final_output_list = []
        final_output_list.append(1)
        for i, item in enumerate(previous_row_list):
            try:
                sum_value = item + previous_row_list[i+1]
            except IndexError:
                sum_value = item + 0
            finally:
                final_output_list.append(sum_value)
        return final_output_list

    def print_output(self):
        for item in self.final_pattern_list:
            for inner_item in item:
                print(inner_item, end="\t")
            print()