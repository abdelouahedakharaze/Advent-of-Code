"""

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""
import os

script_dir = os.path.dirname(__file__) 
file_path = os.path.join(script_dir, 'input1.txt')
numbersList=[]
with open(file_path,'r') as f:
  s=f.readlines()
  for i in s:
    v=[a for a in i if a.isdigit()]
    numbersList.append(v)
h=[]
for i in numbersList:
  if len(i)>1:
    h.append(int(f"{i[0]}{i[-1]}"))
  else:
    h.append(int(f"{i[0]}{i[0]}"))

print(sum(h))