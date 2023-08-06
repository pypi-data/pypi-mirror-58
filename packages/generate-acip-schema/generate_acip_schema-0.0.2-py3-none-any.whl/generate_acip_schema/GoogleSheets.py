import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheets:
    def __init__(self, config, key=None, sheet=None):
        self.config = config
        self.credentials = self.authorize()
        self.workbook_key = key
        self.worksheet_name = sheet

        if key is None and 'workbook_key' in config:
            self.workbook_key = config['workbook_key']

        if sheet is None and 'worksheet_name' in config:
            self.worksheet_name = config['worksheet_name']

        self.data = self.get_column_data()

    def authorize(self):
        gc = None
        try:
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                self.config["json_creds"], self.config["scope"]
            )

            gc = gspread.authorize(credentials)
            print(f"Authorizing script for Google Sheets...")
        except IOError as e:
            print(e)

        return gc

    def get_column_data(self, col=1):

        if self.workbook_key is not None and self.worksheet_name is not None:
            wkb = self.credentials.open_by_key(self.workbook_key)
            wks = wkb.worksheet(self.worksheet_name)
            works = wks.col_values(col)
            return sorted(works[1:])

        return None

    def write_data(self, data=None):
        current_ws = {}

        if data is None:
            data = self.data

        if self.workbook_key is not None and self.worksheet_name is not None:
            workbook = self.credentials.open_by_key(self.workbook_key)

            for item in workbook.worksheets():
                current_ws.update({item.title: item.id})

            print(current_ws)

            if self.config["write_sheet_name"] in current_ws:
                print("deleting worksheet", self.config["write_sheet_name"])
                sh = workbook.worksheet(self.config["write_sheet_name"])
                workbook.del_worksheet(sh)

            # recreate the worksheet
            print("Recreating worksheet. Data has length: ", len(data))
            workbook.add_worksheet(title=self.config["write_sheet_name"], rows=len(data), cols=2)

            # to add as a column, create for loop
            data.insert(0, "Works")
            workbook.values_append(
                self.config["write_sheet_name"],
                params={'valueInputOption': 'RAW'},
                body={'values': [data], 'majorDimension': 'COLUMNS'}
            )
