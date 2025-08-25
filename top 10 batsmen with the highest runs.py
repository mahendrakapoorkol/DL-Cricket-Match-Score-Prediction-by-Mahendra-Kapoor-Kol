# Find top 10 batsmen based on total runs scored
top_batsmen = df.groupby("batsman")["runs"].sum().nlargest(10)

# Plot the results
plt.figure(figsize=(12, 6))
sns.barplot(y=top_batsmen.index, x=top_batsmen.values, palette="mako")
plt.title("Top 10 Run Scorers in IPL")
plt.xlabel("Runs Scored")
plt.ylabel("Player")
plt.show()
