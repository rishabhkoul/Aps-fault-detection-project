from typing import List
x = "checking the function List and what it does"

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()