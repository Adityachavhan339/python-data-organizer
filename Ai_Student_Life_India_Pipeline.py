import os
import shutil
import pandas as pd

print("Starting Data Analysis...")
try:
    folder_name = input("Enter Name For Folder:")
    if os.path.exists(folder_name):
        print(f"Error Folder With Name {folder_name} Already Exist")
    else:
        os.mkdir(folder_name)
except Exception as e:
    print(e)

print(f"Creating Folder {folder_name}..")
print(f"Successfully Created Folder {folder_name} at:", os.getcwd())

print("Opening Dataset..")
try:
    data = pd.read_csv("AI_Student_Life_india.csv")
    mumbai_high_satisfaction = data[(data["City"] == "Mumbai") & (data["Satisfaction_Level"] == "High")]
except Exception as e:
    print(e)

print("Updating..")
mumbai_high_satisfaction.fillna("Unknown",inplace=True)
sorted_MB_High_Satisfaction = mumbai_high_satisfaction.sort_values("Age",ascending=False)

sorted_MB_High_Satisfaction.to_csv("Sorted_Mumbai_High_Satisfaction.csv",index=False)
print("Dataset Updated Successfully..")
try:
    shutil.move("Sorted_Mumbai_High_Satisfaction",os.path.join(folder_name,"Sorted_Mumbai_High_Satisfaction"))
except Exception as e:
    print(e)

print("Moving Files..")
 
try:
    os.mkdir("Backup_AI_Student_Life_India")
    shutil.copy("AI_Student_Life_india.csv",os.path.join("Backup_AI_Student_Life_India","AI_Student_Life_india.csv"))
except Exception as e:
    print(e)

print("Saving Files As Backup..")
print("Operation Successful")
