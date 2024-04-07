import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cricket.csv')

print("Cricketer and their respective runs:")
print(df[['name', 'runs']])

total_wickets = df['wickets'].sum()
print("\nTotal wickets taken by all players:", total_wickets)

average_catches = df['catches'].mean()
print("\nAverage number of catches taken:", average_catches)

wicketkeeper = df.loc[df['stumpings'] > 0, 'name'].values
if len(wicketkeeper) > 0:
    print("\nWicketkeeper:", wicketkeeper[0])
else:
    print("\nWicketkeeper not found.")

highest_matches_bowler = df.loc[df['matches'].idxmax(), 'name']
print("\nBowler who played highest number of matches:", highest_matches_bowler)

bowlers_average = df['wickets'].astype(float).mean()
print("\nAverage bowling average of all the bowlers:", bowlers_average)

least_average_bowler = df.loc[df['wickets'] > 0, 'name'].iloc[df.loc[df['wickets'] > 0, 'wickets'].idxmin()]
print("\nName of the bowler with least bowling average:", least_average_bowler)

df.plot(kind='bar', x='name', y='runs', legend=None)
plt.title('Matches vs Runs Scored')
plt.xlabel('Name')
plt.ylabel('Runs')
plt.xticks(rotation=45)
plt.show()

sorted_df_by_runs = df.sort_values(by='runs')
print("\nPlayers information sorted by ascending order of runs:")
print(sorted_df_by_runs)

players_with_more_wickets_than_matches = df[df['wickets'] > df['matches']]['name'].tolist()
print("\nNames of players whose wickets are greater than matches:", players_with_more_wickets_than_matches)
