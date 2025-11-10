import matplotlib.pyplot as plt
import matplotlib.pyplot as pt
roll_nos = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
marks = [22,87,5,43,56,73,55,54,11,20,51,5,79,31,27,60]
plt.scatter(roll_nos,marks,color='red',marker='o')
plt.xlabel("ROLL NUMBER")
plt.ylabel("MARKS")
plt.title("SCATTER PLOT OF ROLL NUMBER VS MARKS")
plt.show()