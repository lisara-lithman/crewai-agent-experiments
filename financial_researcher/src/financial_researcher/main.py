#!/usr/bin/env python
import sys
import warnings
from dotenv import load_dotenv, find_dotenv

# Search up the directory tree for a .env file and load it
load_dotenv(find_dotenv())

from datetime import datetime

from financial_researcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """Run the crew.""" 

    inputs = {
    'company' : 'Tesla'
    }

    results = FinancialResearcher().crew().kickoff(inputs=inputs)
    print(results.raw)

if __name__ == "__main__":
    run()
    


