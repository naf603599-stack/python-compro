import pandas as pd

data = {'name': ['Alice','Bob','charlie'],
        'age': [25,30,35],
        'city': ["New york",'Los Angeles','Chicago']}

df = pd.DataFrame(data)
print("DataFrame:\n",df)

average_age=df['age'].mean()
print("\nAverge Age:",average_age)

filtered_df=df[df['age']>28]
print("\nFiltered DataFrame (Age > 28 ): \n",filtered_df)

df['Salary']=[50000,60000,70000]
print("\nDataFrame with Salary column :\n",df)