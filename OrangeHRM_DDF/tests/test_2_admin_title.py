from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from datetime import datetime
from conftest import setup
import pandas as pd
import pytest
import os


def get_login_data():  # Method to get the Employee Data from the Excel sheet to add a new employee
    login_data = []
    # Read the Excel file into a DataFrame
    df = pd.read_excel('title_data.xlsx', 'TITLE')  # Update the path to your Excel file if needed
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces
    print(df.columns)

    # Iterate through the rows of the DataFrame and extract username and password
    for index, row in df.iterrows():
        username = row['USERNAME']
        password = row['PASSWORD']

        login_data.append((username, password))

    return login_data


def update_excel(username, password, test_result, tester_name):  # Method to update the status in the Excel sheet
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")
    file_path = 'title_data.xlsx'
    temp_file_path = 'title_data_temp.xlsx'

    try:
        df = pd.read_excel(file_path, engine='openpyxl')  # Load the existing Excel file into a DataFrame
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

    # Update the DataFrame with the test result for the matching username and password
    record_found = False
    for index, row in df.iterrows():
        if row["USERNAME"] == username and row["PASSWORD"] == password:
            df.at[index, "DATE"] = current_date
            df.at[index, "TIME OF TEST"] = current_time
            df.at[index, "NAME OF TESTER"] = tester_name
            df.at[index, "TEST RESULT"] = test_result
            record_found = True
            break

    if not record_found:
        print(f"No matching record found for username: {username} and password: {password}")
        return

    try:
        # Save the updated DataFrame to a temporary file
        with pd.ExcelWriter(temp_file_path, engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, index=False, sheet_name='TITLE')

        os.replace(temp_file_path, file_path)  # Replace the original file with the temporary file
    except Exception as e:
        print(f"Error writing to the Excel file: {e}")
        # Optionally, handle the temporary file cleanup here
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)


@pytest.mark.usefixtures("setup")
class TestLoginTitle:
    @pytest.mark.parametrize("username, password", get_login_data())
    def test_add(self, setup, username, password):
        login_page = LoginPage(self.driver)
        login_page.login(username, password)

        admin_page = AdminPage(self.driver)
        admin_page.title()

        # Replace 'Tester_Name' with the actual tester's name or get it dynamically
        tester_name = "Sivaramakrishnan T"

        if "viewSystemUsers" in self.driver.current_url:
            update_excel(username, password, "Passed", tester_name)
            print("\nAll the elements are present in the Header of the Admin Page")
        else:
            update_excel(username, password, "Failed", tester_name)
            print("Failed")
