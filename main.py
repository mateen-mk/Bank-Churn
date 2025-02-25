# this script is used to run the pipelines from src/pipeline/*

import sys

from src.core.exception import BankChurnException

from src.pipelines.run import run


# run the pipeline
if __name__ == "__main__":

    try:
        
        run()

    except BankChurnException as e:
        print(f"Error occured while running pipeline from main.py: {str(e)}")
        raise BankChurnException(f"Error occured while running pipeline from main.py: {str(e)}",sys) from e