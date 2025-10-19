import sys
from cell_segmentation.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = f"""Error occurred in script: {file_name} at line number: {line_number} error message: {str(error)}"""
    
    return error_message 

class AppException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """"
        parmas:
        error_message: Error message in string format
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        # Log the error message
        logging.error(self.error_message, exc_info=error_detail.exc_info())

    def __str__(self):
        return self.error_message