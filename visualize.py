import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file (change 'your_file.csv' to your actual file path)
df = pd.read_csv('test_outputs.csv')

# Check if 'race' column exists
if 'race' not in df.columns:
    raise ValueError("The CSV file does not contain a 'race' column.")

# Count the occurrences of each race
race_counts = df['race'].value_counts().sort_values(ascending=False)

# Print race distribution
print("Race Distribution amongst 70 samples:")
print(race_counts)

# Set Seaborn style
sns.set(style="whitegrid")

# Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=race_counts.values, y=race_counts.index, palette="viridis")
plt.title("Stable-diffusion-v1-5 Race Distribution of Race amongst 70 samples")
plt.xlabel("Count")
plt.ylabel("Race")
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Stable-diffusion-v1-5 Race Distribution amongst 70 samples")
plt.axis('equal')
plt.tight_layout()
plt.show()
