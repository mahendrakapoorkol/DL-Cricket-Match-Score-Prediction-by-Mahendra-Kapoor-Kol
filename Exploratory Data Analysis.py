# Make a copy of the dataset
df = dataset.copy()

# Count matches played at each venue
venue_counts = df.drop_duplicates(subset=["mid", "venue"])["venue"].value_counts()

# Plot the distribution
plt.figure(figsize=(12, 6))
sns.barplot(y=venue_counts.index, x=venue_counts.values, palette="viridis")
plt.title("Matches Played by Venue")
plt.xlabel("Total Matches")
plt.ylabel("Stadium")
plt.show()
