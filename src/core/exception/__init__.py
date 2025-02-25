# Custom Exception script (BankChurnException)

import sys

def error_message_detail(error, error_detail: sys):
    """
    Generates a detailed error message with the script name, line number, 
    and error message.

    Args:
        error (Exception): The exception instance.
        error_detail (sys): System-specific parameters used to extract stack trace.

    Returns:
        str: A detailed error message including script name, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in Python script: {file_name}, " \
                    f"Line number: {exc_tb.tb_lineno}, " \
                    f"Error message: {str(error)}"
    
    return error_message


class BankChurnException(Exception):
    """
    A custom exception for handling errors related to hotel booking operations.
    
    Automatically includes file name, line number, and the error message.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the BankChurnException with an error message and stack trace 
        without requiring explicit input for error details.

        Args:
            error_message (str): The error message that describes the issue.
            error_detail (sys): Provides the system-specific details to extract stack trace.
        """
        self.error_message = error_message_detail(error_message, error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        """
        Returns a string representation of the exception with detailed error information.
        
        Returns:
            str: A formatted string with the error message and additional details.
        """
        return self.error_message
