import pandas as pd
import matplotlib.pyplot as plt


fname = "datafile-1-csv.txt"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: there are 3 columns of numbers in the input file

problem_sizes = df[var_names[0]].values.tolist()
ideal_time = df[var_names[1]].values.tolist()
actual_time = df[var_names[2]].values.tolist()

# compute two new variables: ideal speedup and actual speedup

ideal_speedup = [1.0/i for i in ideal_time]
actual_speedup = [1.0/i for i in actual_time]


plt.title("Speedup: Actual vs. Ideal")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

plt.plot(ideal_speedup, "r-+")
plt.plot(actual_speedup, "b-x")

#plt.xscale("log")
plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("Speedup")

varNames = [var_names[1], var_names[2]]
plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
