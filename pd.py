import pandas as pd

data = {
    'Name': ["Ali", "Mobina", "Mina", "Reza"],
    'Age': [18, 21, 17, 899],
    'Score': [88, 100, 99, 60]
}

df = pd.DataFrame(data)
print(df)
print("Mean: ",df['Score'].mean())
print("\ntop ones: \n", df[df['Score'] > 80])
