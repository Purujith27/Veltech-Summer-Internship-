import numpy as np

marks = np.array([46, 87, 69, 76, 58, 72, 44, 98, 83, 81])

print("Mean:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Standard Deviation:", marks.std())
print("Passed Students:", len(marks[marks >= 50]))