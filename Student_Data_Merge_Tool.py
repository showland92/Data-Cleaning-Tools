import pandas as pd

# Load the data from the uploaded CSV file
file_path = r"paste the path of the CSV file here"
df = pd.read_csv(file_path)

# Create a function to assign fields of study to the correct columns
def assign_fields(group):
    # Only consider non-null and string values for majors and minors
    majors = sorted([x for x in group.loc[group['Field Of Study Type'] == 'Major', 'Field Of Study'] if isinstance(x, str)])
    minors = sorted([x for x in group.loc[group['Field Of Study Type'] == 'Minor', 'Field Of Study'] if isinstance(x, str)])
    
    # Creating a dictionary to store the assignments
    return pd.Series({
        'Major 1': majors[0] if len(majors) > 0 else None,
        'Major 2': majors[1] if len(majors) > 1 else None,
        'Minor 1': minors[0] if len(minors) > 0 else None,
        'Minor 2': minors[1] if len(minors) > 1 else None
    })

# Group by 'Email Address' and apply the function to assign fields of study
grouped_df = df.groupby('Email Address').apply(assign_fields, include_groups=False).reset_index()

# Merge the first and last name columns along with other columns you want to keep with the grouped data while avoiding duplicates
# Here, you can include other columns from the original dataframe that you want to keep
original_columns = df[['Email Address', 'Ndid', 'Name First', 'Name Last', 'First Generation Student', 'Degree College', 'Student Classification', 'Month, Day, Year of Student Expected Grad Date', 'Campus' ]].drop_duplicates() #Make sure to edit desired columns according to your data

# Perform the merge with the newly grouped dataframe
merged_df = pd.merge(original_columns, grouped_df, on='Email Address')

# Export the processed dataframe to a CSV file
merged_df.to_csv(r'paste path of desired save location here', index=False)
