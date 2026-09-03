import pandas as pd
test_marks = [77, 55, 66, 99, 88]
student_marks = pd.Series(test_marks, 
                          index = ["Dina", "Mateo", "Amy", "Jonah", "Glenn"])
print(student_marks)
students = {
    "Name": ["Dina", "Mateo", "Amy", "Jonah", "Glenn", "Garrett"],
    "Final Percentage": [90, 87, 85, 89, 50, 45],
    "Attendance": ["Excellent", "Very Good", "Very Good", "Very Good", "Needs Improvement", "Bad"]
}
df_students = pd.DataFrame(students)
print(df_students)
readingcsvfile = pd.read_csv("studentMarksAnalyserCsvFile.csv")
print(readingcsvfile)
print(readingcsvfile.head(3))
print(readingcsvfile.tail(3))
print(readingcsvfile.info())
uncompleted_data = {
    "Day": ["Sun", "Mon", "Tue", "Wed", "Thur", "Fri", "Sat"],
    "Temp(C)": [20, 18, 17, None , 15, 21, 22],
    "Weather": ["Cloudy", "Frosty", "Cold", None, "Cold", "Warm", "Warm"]
}
uncompleted_data_df = pd.DataFrame(uncompleted_data)
print(uncompleted_data_df)
completed_data_df = uncompleted_data_df.fillna("Unknown")
print(completed_data_df)
average  = test_marks/len(test_marks)
print(average)
