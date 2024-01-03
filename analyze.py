import pandas as pd

def calculate_qb_rating():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/quarterback_stats.csv')

    # Specify the columns you want to extract
    selected_columns = ['PLAYER', 'CMP', 'PASS_ATT', 'PCT', 'PASS_YDS', 'PASS_TD', 'RUSH_ATT', 'RUSH_YDS', 'RUSH_TD']   

    # Create a new DataFrame with only the selected columns
    selected_df = df[selected_columns].copy()  # Ensure a copy to avoid SettingWithCopyWarning

    # Convert 'PASS_YDS' column to numeric using .loc
    selected_df.loc[:, 'PASS_YDS'] = pd.to_numeric(selected_df['PASS_YDS'].str.replace(',', ''), errors='coerce')

    # Ensure 'PASS_TD' column is treated as a string before replacing commas
    selected_df['PASS_TD'] = selected_df['PASS_TD'].astype(str)
    selected_df.loc[:, 'PASS_TD'] = pd.to_numeric(selected_df['PASS_TD'].str.replace(',', ''), errors='coerce')

    # Add checks for non-zero values before calculation
    selected_df.loc[:, 'rec_rating'] = (
        (0.8813 * (selected_df['PASS_TD'] + selected_df['RUSH_TD'])).fillna(0) +
        (0.6927 * selected_df['PASS_TD']).fillna(0) +
        (0.6523 * selected_df['PCT']).fillna(0) +
        (0.6356 * selected_df['PASS_YDS']).fillna(0) +
        (0.4777 * selected_df['CMP']).fillna(0) +
        (0.3821 * selected_df['PASS_ATT']).fillna(0)
    ) / (0.8813 + 0.6927 + 0.6523 + 0.6356 + 0.4777 + 0.3821)

    # Sort the DataFrame by 'REC_RATING' in descending order
    selected_df = selected_df.sort_values(by='rec_rating', ascending=False)

    # Round the 'REC_RATING' column to two decimal places
    selected_df['rec_rating'] = selected_df['rec_rating'].round(2)

    # Rename columns for the output
    selected_df.rename(columns={'PLAYER': 'PLAYER', 'rec_rating': 'REC_RATING'}, inplace=True)

    # Save the result to a new CSV file
    selected_df[['PLAYER', 'REC_RATING']].to_csv('data/qb_rec_ratings.csv', index=False)

def calculate_rb_rating(): 
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/runningback_stats.csv')

    # Specify the columns you want to extract
    selected_columns = ['PLAYER', 'ATT', 'RUSH_YDS', 'RUSH_TD', 'REC', 'REC_TD']

    # Create a new DataFrame with only the selected columns
    selected_df = df[selected_columns].copy()  # Ensure a copy to avoid SettingWithCopyWarning

    # Convert 'RUSH_YDS' column to numeric using .loc
    selected_df.loc[:, 'RUSH_YDS'] = pd.to_numeric(selected_df['RUSH_YDS'].str.replace(',', ''), errors='coerce')

    # Ensure 'RUSH_TD' column is treated as a string before replacing commas
    selected_df['RUSH_TD'] = selected_df['RUSH_TD'].astype(str)
    selected_df.loc[:, 'RUSH_TD'] = pd.to_numeric(selected_df['RUSH_TD'].str.replace(',', ''), errors='coerce')

    # Ensure 'REC_TD' column is treated as a string before replacing commas
    selected_df['REC_TD'] = selected_df['REC_TD'].astype(str)
    selected_df.loc[:, 'REC_TD'] = pd.to_numeric(selected_df['REC_TD'].str.replace(',', ''), errors='coerce')

    # Add checks for non-zero values before calculation
    selected_df.loc[:, 'rec_rating'] = (
        (0.6921 * (selected_df['ATT'] + selected_df['REC'])).fillna(0) +
        (0.6024 * (selected_df['RUSH_TD'] + selected_df['REC_TD'])).fillna(0) +
        (0.5735 * selected_df['ATT']).fillna(0) +
        (0.5316 * selected_df['RUSH_YDS']).fillna(0) +
        (0.4671 * selected_df['REC']).fillna(0)
    ) / (0.6921 + 0.6024 + 0.5735 + 0.5316 + 0.4671)

    # Sort the DataFrame by 'REC_RATING' in descending order
    selected_df = selected_df.sort_values(by='rec_rating', ascending=False)

    # Round the 'REC_RATING' column to two decimal places
    selected_df['rec_rating'] = selected_df['rec_rating'].round(2)

    # Rename columns for the output
    selected_df.rename(columns={'Player': 'PLAYER', 'rec_rating': 'REC_RATING'}, inplace=True)

    # Save the result to a new CSV file
    selected_df[['PLAYER', 'REC_RATING']].to_csv('data/rb_rec_ratings.csv', index=False)

def calculate_wr_rating():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/wide_receiver_stats.csv')

    # Specify the columns you want to extract
    selected_columns = ['PLAYER', 'REC', 'TGT', 'REC_YDS', 'REC_TD']

    # Create a new DataFrame with only the selected columns
    selected_df = df[selected_columns].copy()  # Ensure a copy to avoid SettingWithCopyWarning

    # Add checks for non-zero values before calculation
    selected_df.loc[:, 'rec_rating'] = (
        (0.8621 * selected_df['REC_YDS']).fillna(0) +
        (0.7849 * selected_df['REC']).fillna(0) +
        (0.6574 * selected_df['TGT']).fillna(0) +
        (0.5206 * selected_df['REC_TD']).fillna(0)
    ) / (0.8621 + 0.7849 + 0.6574 + 0.5206)

    # Sort the DataFrame by 'REC_RATING' in descending order
    selected_df = selected_df.sort_values(by='rec_rating', ascending=False)

    # Round the 'REC_RATING' column to two decimal places
    selected_df['rec_rating'] = selected_df['rec_rating'].round(2)

    # Rename columns for the output
    selected_df.rename(columns={'Player': 'PLAYER', 'rec_rating': 'REC_RATING'}, inplace=True)

    # Save the result to a new CSV file
    selected_df[['PLAYER', 'REC_RATING']].to_csv('data/wr_rec_ratings.csv', index=False)


def calculate_te_rating(): 
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/tight_end_stats.csv')

    # Specify the columns you want to extract
    selected_columns = ['PLAYER', 'REC', 'TGT', 'REC_YDS', 'REC_TD']

    # Create a new DataFrame with only the selected columns
    selected_df = df[selected_columns].copy()  # Ensure a copy to avoid SettingWithCopyWarning

    # Add checks for non-zero values before calculation
    selected_df.loc[:, 'rec_rating'] = (
        (0.8228 * selected_df['REC_YDS']).fillna(0) +
        (0.8002 * selected_df['REC']).fillna(0) +
        (0.6893 * selected_df['TGT']).fillna(0) +
        (0.5267 * selected_df['REC_TD']).fillna(0)
    ) / (0.8228 + 0.8002 + 0.6893 + 0.5267)

    # Sort the DataFrame by 'REC_RATING' in descending order
    selected_df = selected_df.sort_values(by='rec_rating', ascending=False)

    # Round the 'REC_RATING' column to two decimal places
    selected_df['rec_rating'] = selected_df['rec_rating'].round(2)

    # Rename columns for the output
    selected_df.rename(columns={'Player': 'PLAYER', 'rec_rating': 'REC_RATING'}, inplace=True)

    # Save the result to a new CSV file
    selected_df[['PLAYER', 'REC_RATING']].to_csv('data/te_rec_ratings.csv', index=False)



def calculate_dst_rating(): 
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/defense_stats.csv')

    # Specify the columns you want to extract
    selected_columns = ['Player', 'SACK', 'INT', 'FR', 'DEF TD']

    # Create a new DataFrame with only the selected columns
    selected_df = df[selected_columns].copy()  # Ensure a copy to avoid SettingWithCopyWarning

    # Add checks for non-zero values before calculation
    selected_df.loc[:, 'rec_rating'] = (
        (0.4 * selected_df['DEF TD']).fillna(0) +
        (0.3 * selected_df['INT']).fillna(0) +
        (0.2 * selected_df['FR']).fillna(0) +
        (0.1 * selected_df['SACK']).fillna(0) 
    ) / (0.4 + 0.3 + 0.2 + 0.1)

    # Sort the DataFrame by 'REC_RATING' in descending order
    selected_df = selected_df.sort_values(by='rec_rating', ascending=False)

    # Round the 'REC_RATING' column to two decimal places
    selected_df['rec_rating'] = selected_df['rec_rating'].round(2)

    # Rename columns for the output
    selected_df.rename(columns={'Player': 'PLAYER', 'rec_rating': 'REC_RATING'}, inplace=True)

    # Save the result to a new CSV file
    selected_df[['PLAYER', 'REC_RATING']].to_csv('data/dst_rec_ratings.csv', index=False)

def calculate_k_rating(): 
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/kicker_stats.csv')

    # Specify the columns you want to extract
    selected_columns = ['Player', 'FG', 'FGA', 'PCT', 'LG', 'XPT']

    # Create a new DataFrame with only the selected columns
    selected_df = df[selected_columns].copy()  # Ensure a copy to avoid SettingWithCopyWarning

    # Add checks for non-zero values before calculation
    selected_df.loc[:, 'rec_rating'] = (
        (0.25 * selected_df['FG']).fillna(0) +
        (0.20 * selected_df['FGA']).fillna(0) +
        (0.15 * selected_df['PCT']).fillna(0) +
        (0.15 * selected_df['LG']).fillna(0) + 
        (0.10 * selected_df['XPT']).fillna(0)
    ) / (0.25 + 0.20 + 0.15 + 0.15 + 0.10)

    # Sort the DataFrame by 'REC_RATING' in descending order
    selected_df = selected_df.sort_values(by='rec_rating', ascending=False)

    # Round the 'REC_RATING' column to two decimal places
    selected_df['rec_rating'] = selected_df['rec_rating'].round(2)

    # Rename columns for the output
    selected_df.rename(columns={'Player': 'PLAYER', 'rec_rating': 'REC_RATING'}, inplace=True)

    # Save the result to a new CSV file
    selected_df[['PLAYER', 'REC_RATING']].to_csv('data/k_rec_ratings.csv', index=False)






    
        
