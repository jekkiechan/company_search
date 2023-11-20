import pandas as pd


def create_column_description_df():
    return pd.DataFrame(
        {
            "column_name": [
                "Date",
                "Company Name",
                "Person In Charge",
                "Title",
                "Email",
                "Website",
                "Tel",
                "Start Time",
                "End Time",
                "Startups Meeting",
                "No. Attendee",
                "Ticket Requested",
                "Note",
                "Confirmation Email",
            ],
            "column_description": [
                "Meeting Date",
                "Name of target company",
                "Name of person in charge for this company-startup interaction",
                "Title of the person in charge",
                "Email of the person in charge",
                "Website of this company",
                "Telephone of the person in charge",
                "Meeting Start Time",
                "Meeting End Time",
                "Name of startup that the company met with",
                "Number of attendees in the meeting",
                "Number of ticket requested",
                "Notes in the meeting",
                "Whether the startup received a confirmation email from the company",
            ],
        }
    ).set_index("column_name")


def drop_columns(data):
    unnamed_cols = [col for col in data.columns if col.startswith("Unnamed")]
    return data.drop(columns=[*unnamed_cols, "Require ticket"])


def format_date_column(data):
    data["Date"] = data["Date"].replace({"TBC": None})
    data["Date"] = pd.to_datetime(data["Date"], format="%m/%d")
    data["Date"] = data["Date"].apply(lambda x: x.replace(year=2023))
    return data


def clean_text_columns(data):
    text_cols = ["Company Name", "Startups Meeting", "Company-email", "Company Website"]
    for col in text_cols:
        data[col] = data[col].str.strip().str.replace("\n|\t", "")
    data["Startups Meeting"] = data["Startups Meeting"].replace(
        {"Inter holding": "Inter Holdings"}
    )
    return data


def preprocess(company_data, people_data):
    data = people_data.merge(company_data, on=["Company Name"], how="left")
    data = data.rename(columns={"Meeting history - Date of meeting": "Date"})
    data = (
        data.pipe(drop_columns)
        .pipe(format_date_column)
        .pipe(clean_text_columns)
    )
    data = data.astype(str).replace({"nan": None}).rename(
        columns={"Startups Meeting": "Startups that met with the company"}
    )
    return data


if __name__ == '__main__':
    company = pd.read_excel("data/company_database.xlsx", usecols="B:P", sheet_name="Company")
    people = pd.read_excel("data/company_database.xlsx", usecols="B:AB", sheet_name="Person")
    data = preprocess(company, people)
    breakpoint()

