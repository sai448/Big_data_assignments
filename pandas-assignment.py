# Q1. How do you load a CSV file into a Pandas DataFrame?
import pandas as pd
df=pd.read_csv("CSV-FILE")

# Q2. How do you check the data type of a column in a Pandas DataFrame?
---> df.dtypes
# Q3. How do you select rows from a Pandas DataFrame based on a condition?
--->res =df[df[column]>percentage]
# Q4. How do you rename columns in a Pandas DataFrame?
--->df.rename(columns={'clName':'newClName'},inplace=True)
# Q5. How do you drop columns in a Pandas DataFrame?
---> pd.drop(column-name,axis=1)
# Q6. How do you find the unique values in a column of a Pandas DataFrame?
---> df[column-name].unique()
# Q7. How do you find the number of missing values in each column of a Pandas DataFrame?
---> df.isnull()
# Q8. How do you fill missing values in a Pandas DataFrame with a specific value?
--->df3.fillna("value")
# Q9. How do you concatenate two Pandas DataFrames?
---> df3= pd.concat([df1,df2])
df-data frame
# Q10. How do you merge two Pandas DataFrames on a specific column?
---> (pd.merge(df1, df2, on='common ClNmae'))

# Q11. How do you group data in a Pandas DataFrame by a specific column and apply an aggregation function?

# Q12. How do you pivot a Pandas DataFrame?
The pivot() function is used to reshape a given DataFrame organized by given index / column values . 
df.pivot(index='column-name',columns="column-name",values='column-name')

# Q13. How do you change the data type of a column in a Pandas DataFrame?
df.astype('data-type')

# Q14. How do you sort a Pandas DataFrame by a specific column?
df.sort_values(by=['column-names'])
# Q15. How do you create a copy of a Pandas DataFrame?
---> df.copy()

# Q16. How do you filter rows of a Pandas DataFrame by multiple conditions?
---> using &,|, ~ operators and loc methd to filter the dataframe data based on multiple conditions
# Q17. How do you calculate the mean of a column in a Pandas DataFrame?
---> df.describe()
# Q18. How do you calculate the standard deviation of a column in a Pandas DataFrame?
---> df.describe()
# Q19. How do you calculate the correlation between two columns in a Pandas DataFrame?
print(df1['Cl1'].corr(df2['Cl2']))
# Q20. How do you select specific columns in a DataFrame using their labels?
---> df['Column-name']
# Q21. How do you select specific rows in a DataFrame using their indexes?
---> using iloc method
# Q22. How do you sort a DataFrame by a specific column?
--->df.sort_values(by=['column-names'])
# Q23. How do you create a new column in a DataFrame based on the values of another column?
--->df['NewCl']=df['Cl1']+df['Cl2']
# Q24. How do you remove duplicates from a DataFrame?
---> df.drop_duplicates()
# Q25. What is the difference between .loc and .iloc in Pandas?
---> loc used to filter the data based on condition, iloc used to filter the data in DF, it accepts only integer values