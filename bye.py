import pandas as pd

# Sample data with continuous and categorical variables
data = {
    "age": [25, 30, 22, 38, 40, 28, 35, 32],
    "sex": ["female", "male", "female", "male", "female", "male", "female", "male"],
    "income": [50000, 70000, 45000, 80000, 60000, 65000, 75000, 90000],
    "education": ["bachelors", "masters", "bachelors", "phd", "high school", "masters", "bachelors", "phd"]
}

df = pd.DataFrame(data)

# Function to generate a descriptive table (similar to Table 1)
def generate_table_1(df):
  """
  This function generates a descriptive table (similar to Table 1) for a pandas DataFrame.

  Args:
      df (pandas.DataFrame): The DataFrame containing the data.

  Returns:
      pandas.DataFrame: The descriptive table.
  """
  table = pd.DataFrame(columns=df.columns)

  for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
      # Continuous variable: calculate mean
      table.loc[col] = df[col].mean()
    else:
      # Categorical variable: calculate frequency table
      table.loc[col] = df[col].value_counts()

  return table.transpose()

# Generate and print the table
table_1 = generate_table_1(df.copy())
print(table_1)