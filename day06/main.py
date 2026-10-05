import ScoreCollector, FibIterator, iterator
from pathlib import Path

print("MyRange(1, 5):")
for num in iterator.MyRange(1, 5):
    print(num)

p = Path(__file__).parent.parent # python_study 目录 
py_files = p.glob( "**/*.py" )
for file in py_files:
    print(file)