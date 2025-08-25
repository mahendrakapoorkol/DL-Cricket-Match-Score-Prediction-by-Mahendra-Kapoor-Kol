# Identify top 10 wicket-takers
top_bowlers = df.groupby("bowler")["wickets"].sum().nlargest(10)

# Visualize the results
plt.figure(figsize=(12, 6))
sns.barplot(y=top_bowlers.index, x=top_bowlers.values, palette="crest")
plt.title("Top 10 IPL Bowlers by Wickets")
plt.xlabel("Wickets Taken")
plt.ylabel("Player")
plt.show()
