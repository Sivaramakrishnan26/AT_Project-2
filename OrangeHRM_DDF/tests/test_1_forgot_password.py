from pages.forgot_password_page import ForgotPasswordPage
from datetime import datetime
from conftest import setup
import pandas as pd
import pytest
import os


def get_forgot_password_data():  # Method to fetch the data from the Excel sheet
    forgot_password_data = []
    # Read the Excel file into a DataFrame
    df = pd.read_excel('reset_data.xlsx', 'FORGOT_PASSWORD')  # Update the path to your Excel file if needed

    # Iterate through the rows of the DataFrame and extract username
    for index, row in df.iterrows():
        username = row['USERNAME']
        forgot_password_data.append(username)

    return forgot_password_data


def update_excel(username, test_result, tester_name):  # Method to update the status in the Excel sheet
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    file_path = 'reset_data.xlsx'
    temp_file_path = 'reset_data_temp.xlsx'

    try:
        # Load the existing Excel file into a DataFrame
        df = pd.read_excel(file_path, engine='openpyxl')
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return

    # Ensure necessary columns are present and of type string
    for col in ["DATE", "TIME OF TEST", "NAME OF TESTER", "TEST RESULT"]:
        if col not in df.columns:
            df[col] = ""  # Add missing columns with empty strings

    df["DATE"] = df["DATE"].astype(str)
    df["TIME OF TEST"] = df["TIME OF TEST"].astype(str)
    df["NAME OF TESTER"] = df["NAME OF TESTER"].astype(str)
    df["TEST RESULT"] = df["TEST RESULT"].astype(str)

    # Update the DataFrame with the test result for the matching username
    record_found = False
    for index, row in df.iterrows():
        if row["USERNAME"] == username:
            df.at[index, "DATE"] = current_date
            df.at[index, "TIME OF TEST"] = current_time
            df.at[index, "NAME OF TESTER"] = tester_name
            df.at[index, "TEST RESULT"] = test_result
            record_found = True
            break

    if not record_found:
        print(f"No matching record found for username: {username}")
        return

    try:
        # Save the updated DataFrame to a temporary file
        with pd.ExcelWriter(temp_file_path, engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, index=False, sheet_name='FORGOT_PASSWORD')

        # Replace the original file with the temporary file
        os.replace(temp_file_path, file_path)
    except Exception as e:
        print(f"Error writing to the Excel file: {e}")
        # Optionally, handle the temporary file cleanup here
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)


@pytest.mark.usefixtures("setup")
class TestLogin:
    @pytest.mark.parametrize("username", get_forgot_password_data())
    def test_forgot_password(self, setup,username):
        forgot_password_page = ForgotPasswordPage(self.driver)
        forgot_password_page.forgot_password(username)

        # Replace 'Tester_Name' with the actual tester's name or get it dynamically
        tester_name = "Sivaramakrishnan T"

        # Check if the reset password was successful by verifying the presence of 'sendPasswordReset' in the URL
        if "sendPasswordReset" in self.driver.current_url:
            update_excel(username, "Passed", tester_name)
            print("Reset Password link sent successfully")
        else:
            update_excel(username, "Failed", tester_name)
            print("Failed to send Reset Password link")
