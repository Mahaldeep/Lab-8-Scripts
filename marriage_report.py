"""
Description:
 Generates a CSV report of all married couples in the Social Network database.

Usage:
 python generate_married_couples_report.py
"""
import os
import sqlite3
import pandas as pd

# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    married_couples_df = get_married_couples()
    generate_csv_report(married_couples_df)

def get_married_couples():
    """Gets a list of all married couples from the DB"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    married_couples_query = """
    SELECT person1.name as person1_name, person2.name as person2_name, start_date
    FROM relationships
    JOIN people person1 ON person1_id = person1.id
    JOIN people person2 ON person2_id = person2.id
    WHERE type = 'spouse'
    """
    cur.execute(married_couples_query)
    married_couples = cur.fetchall()
    con.close()
    married_couples_df = pd.DataFrame(married_couples, columns=['Person 1 Name', 'Person 2 Name', 'Start Date'])
    return married_couples_df

def generate_csv_report(df):
    """Generates a CSV report of married couples"""
    report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'married_couples_report.csv')
    df.to_csv(report_path, index=False)

if __name__ == '__main__':
    main()
