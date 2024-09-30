# Data-Cleaning-Tools
Overview
This script processes a CSV file that contains student information, including their fields of study (majors and minors). It organizes this information by assigning fields of study to designated columns and consolidating multiple rows of data into a single row per student based on their email address. The final output is a structured CSV file where each student has clearly defined "Major" and "Minor" fields.

Functionality
The script performs the following steps:

Load the Data: The script reads a CSV file using the pandas library, assuming the file contains columns for students' email addresses, their field of study type (whether it's a major or minor), and other relevant information.
Assign Fields of Study: A custom function, assign_fields(), is used to:
Sort and organize the student's declared majors and minors.
Assign the first and second majors (if available) to "Major 1" and "Major 2".
Assign the first and second minors (if available) to "Minor 1" and "Minor 2".
Group by Email: The data is grouped by the "Email Address" field, and the assign_fields() function is applied to assign the correct major and minor columns for each student.
Merge Data: After processing, the original data (including other important fields such as name, student classification, etc.) is merged with the newly assigned fields to ensure that each student has one row with their corresponding information.
Export Processed Data: The final processed data is saved to a new CSV file.
How to Use
Prerequisites
Install Python 3.x.
Install the required library:
bash
Copy code
pip install pandas
Steps
Prepare your CSV file:

Ensure your CSV file has the following columns (or modify the script to match your column names):
Email Address: The unique identifier for each student.
Field Of Study: The student's declared field of study (e.g., Computer Science, Mathematics).
Field Of Study Type: Specifies whether the field of study is a 'Major' or 'Minor'.
Other relevant columns you want to retain in the output file.
Update file paths:

Update the path to your CSV file at:
python
Copy code
file_path = r"paste the path of the CSV file here"
Update the path for saving the processed output file at:
python
Copy code
merged_df.to_csv(r'paste path of desired save location here', index=False)
Run the script:

Run the Python script after updating the paths and columns as necessary.
It will generate a new CSV file containing organized major and minor fields for each student.
