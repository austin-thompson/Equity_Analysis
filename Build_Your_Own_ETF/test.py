import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 
# Creating a series of data of in range of 1-50.
x = np.linspace(1,100,100)
 
#Creating a Function.
def normal_dist(x , mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density
 
#Calculate mean and Standard deviation.
mean = np.mean(x)
sd = np.std(x)
 
#Apply function to the data.
dist = normal_dist(x,mean,sd)
dist = (dist/100)*6

df1 = pd.DataFrame(
    {
        "A": ["msft", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "param2": ["C0", "C1", "C2", "C3"],
        "param1": ["D0", "D1", "D2", "D3"],
    }
)

df1.insert(4, "E", [0,1,2,3])
i = df1[df1.E == 2]

print(df1.columns.size)
print(df1)
