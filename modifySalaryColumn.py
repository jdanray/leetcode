# https://leetcode.com/problems/modify-columns/

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
	employees.salary *= 2
	return employees
