import pandas as pd

# Load and clean OSHA data
df = pd.read_csv('src/dataset/January2015toFebruary2025.csv')
df = df.drop_duplicates()
df_clean = df.dropna(subset=['State'])

print("Original records:", len(df))
print("Records after cleaning:", len(df_clean))
print("Records removed:", len(df) - len(df_clean))

# Injury count by state
state_counts = df_clean['State'].value_counts()

print("=== INJURY COUNT PER STATE ===")
print(state_counts)
print("\n")

# Calculate percentages
total_injuries = len(df_clean)
print("=== TOP 5 STATES ===")
for i, (state, count) in enumerate(state_counts.head(5).items(), 1):
    percentage = (count / total_injuries) * 100
    print(str(i) + ". " + state + ": " + str(count) + " injuries (" + str(round(percentage, 2)) + "% of total)")

print("\n")

# Summary statistics
print("=== SUMMARY STATISTICS ===")
print("Mean injuries per state:", round(state_counts.mean(), 2))
print("Median injuries per state:", round(state_counts.median(), 2))
print("Std deviation:", round(state_counts.std(), 2))
print("State with most injuries:", state_counts.index[0], "(" + str(state_counts.iloc[0]) + ")")

print("State with least injuries:", state_counts.index[-1], "(" + str(state_counts.iloc[-1]) + ")")


