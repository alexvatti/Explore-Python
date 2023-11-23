#pip install pandas
#pip install openpyxl

'''
Need python developer to move one excel data to another and rename header using python script. I have 2 excels.
one with data and one that is empty. the excel with data will be moved to empty excel using python script. 
I will need script to execute myself. Also I have a mac
'''
import pandas as pd

def move_and_rename_excel_data(source_file, destination_file):
    # Read data from the source Excel file
    data = pd.read_excel(source_file)

    # Rename headers as needed
    # Example: Rename 'old_header' to 'new_header'
    data.rename(columns={'SL': 'SLength','SW':'SWidth', 'PL':'PLength','PW':'PWidth', 'Species':'species'}, inplace=True)

    # Write the modified data to the destination Excel file
    data.to_excel(destination_file, index=False)

if __name__ == "__main__":
    # Replace 'source_file.xlsx' and 'destination_file.xlsx' with your file paths
    source_file_path = r'C:\Users\91956\Desktop\UPWORK-PROJECT\Python-Upwork\Task-01-XLSX\Input.xlsx'
    destination_file_path = r'C:\Users\91956\Desktop\UPWORK-PROJECT\Python-Upwork\Task-01-XLSX\Output.xlsx'

    move_and_rename_excel_data(source_file_path, destination_file_path)
