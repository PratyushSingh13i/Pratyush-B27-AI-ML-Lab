import pandas as pd

# Read the original CSV
df = pd.read_csv("onehotvector(Sheet1).csv")

# One-hot encode 'future dream' and combine as a single list
df['dream_one_hot'] = pd.get_dummies(df['future dream'], dtype=int).values.tolist()

# Save the result to a NEW CSV file
output_file = "onehotvector_output.csv"
df.to_csv(output_file, index=False)

print(f"One-hot vector column added successfully!")
print(f"Output saved to: {output_file}")
