import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exec_tb=error_detail.exc_info()
    file_name=exec_tb.tb_frame.f_code.co_filename
    error_message=f"there is an error in your python script in filename {file_name} and lineno is {exec_tb.tb_lineno} and the error is {str(error)}"
    return error_message

class custom_execption(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
