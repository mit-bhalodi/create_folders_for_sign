import pandas as pd
import os

# Load the Excel file into a DataFrame
excel_file = "/Users/meetbhalodi/Downloads/dl.xlsx"
df = pd.read_excel(excel_file, engine="openpyxl")
for index, row in df.iterrows():
    company_name = str(row[0])  # 1st column (Company)
    template_name = str(row[1])  # 2nd column (Template Name)
    html_content = str(row[2])  # 3rd column (HTML content)

    # print(index, company_name, template_name)

    # Create the company folder if it doesn't exist
    company_folder = os.path.join("./extracted", company_name)
    if not os.path.exists(company_folder):
        os.makedirs(company_folder)

    # Create the template folder inside the company folder if it doesn't exist
    # template_folder = os.path.join(company_folder, template_name)
    # if not os.path.exists(template_folder):
    #     os.makedirs(template_folder)

    # Create a file inside the template folder with the HTML content
    file_path = os.path.join(company_folder, f"{template_name}_{index}.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

print("Folder structure created successfully.")