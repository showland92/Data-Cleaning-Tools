#Import neccessary libraries
import pandas as pd
import gspread

#Authorize with Google
gc = gspread.oauth()

# Read in the data
survey_data = gc.open("Google Sheet File Name") #Add the name of the Google Sheet file here
survey_data = pd.DataFrame(survey_data.sheet1.get_all_records())


skills = {
    1: "Excel",
    2: "Networking & Interviewing",
    3: "PowerPoint",
    4: "Adobe Creator Design",
    5: " Digital Marketing",
    6: "Product Management",
    7: "Programming",
    8: "Public Policy Analysis",
    9: "Sales",
    10: "Project Management",
    11: "Leadership",
    12: "Financial Literacy and Investing",
}

#columns to convert
columns_to_convert = ['Q15_1','Q15_2','Q15_3','Q15_4','Q15_5','Q15_6','Q15_7','Q15_8','Q15_9','Q15_10','Q15_11','Q15_12'] #Add the columns you want to convert here

#Convert the numbers to text in selected columns
def convert_number_to_text_in_column(df, column_name):
    survey_data[columns_to_convert] = survey_data[columns_to_convert].applymap(lambda x: skills.get(x, x))
    return df

# Apply the function to the survey data
survey_data = convert_number_to_text_in_column(survey_data, columns_to_convert)

# Save the data to a new CSV
survey_data.to_csv("Path of desired save location", index=False) #Add the path of the desired save location here