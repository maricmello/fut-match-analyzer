# Function to collect scores and calculate results
def analyze_team(team, team_data):
    # Collect home match scores and goals
    home_scores = []
    home_goals = []
    home_wins = 0
    home_draws = 0
    home_losses = 0

    print(f"Enter the scores of the last 5 home games for {team} in the format HOME x AWAY")
    for i in range(5):
        match_number = i + 1
        score = input(f"{match_number}º Game: ")
        home_scores.append(score)
        home_goals.append(int(score.split('x')[0]))  # Home goals

        # Analyze the result
        if int(score[0]) > int(score[-1]):
            home_wins += 1
        elif int(score[0]) == int(score[-1]):
            home_draws += 1
        else:
            home_losses += 1

    total_home_goals = sum(home_goals)
    avg_home_goals = total_home_goals / 5

    # Collect away match scores and goals
    away_scores = []
    away_goals = []
    away_wins = 0
    away_draws = 0
    away_losses = 0

    print(f"Enter the scores of the last 5 away games for {team} in the format HOME x AWAY")
    for i in range(5):
        match_number = i + 1
        score = input(f"{match_number}º Game: ")
        away_scores.append(score)
        away_goals.append(int(score.split('x')[-1]))  # Away goals

        # Analyze the result
        if int(score[0]) < int(score[-1]):
            away_wins += 1
        elif int(score[0]) == int(score[-1]):
            away_draws += 1
        else:
            away_losses += 1

    total_away_goals = sum(away_goals)
    avg_away_goals = total_away_goals / 5

    # Store data in the dictionary
    team_data[team] = {
        "home_scores": home_scores,
        "home_goals": home_goals,
        "total_home_goals": total_home_goals,
        "avg_home_goals": avg_home_goals,
        "away_scores": away_scores,
        "away_goals": away_goals,
        "total_away_goals": total_away_goals,
        "avg_away_goals": avg_away_goals,
        "home_wins": home_wins,
        "home_draws": home_draws,
        "home_losses": home_losses,
        "away_wins": away_wins,
        "away_draws": away_draws,
        "away_losses": away_losses
    }

# Function to display stored team data
def display_team_data(team, team_data):
    if team in team_data:
        print(f"\nStatistics for {team}:")
        print(f"Home scores: {team_data[team]['home_scores']}")
        print(f"Home goals: {team_data[team]['total_home_goals']} | Average: {team_data[team]['avg_home_goals']}")
        print(f"Away scores: {team_data[team]['away_scores']}")
        print(f"Away goals: {team_data[team]['total_away_goals']} | Average: {team_data[team]['avg_away_goals']}")
        print(f"Home results: {team_data[team]['home_wins']} wins, {team_data[team]['home_draws']} draws, {team_data[team]['home_losses']} losses.")
        print(f"Away results: {team_data[team]['away_wins']} wins, {team_data[team]['away_draws']} draws, {team_data[team]['away_losses']} losses.")
    else:
        print(f"Team {team} not found in the data.")

# Dictionary to store team data
team_data = {}

# Ask for the first team and analyze
team_1 = input("What is the first team we are analyzing? ")
analyze_team(team_1, team_data)

# Ask for the second team and analyze
team_2 = input("What is the second team we are analyzing? ")
analyze_team(team_2, team_data)

# Display the analysis
print("\n--- Team Analysis ---")
display_team_data(team_1, team_data)
display_team_data(team_2, team_data)
