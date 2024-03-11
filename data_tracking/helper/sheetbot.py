import gspread

class google_sheet:
    def __init__(self,url):
        gc = gspread.service_account()
        self.sht = gc.open_by_url(url)
    
    def add_worksheet(self,name,rows,cols):
        self.ws = self.sht.add_worksheet(title=name, rows=rows, cols=cols)
        return self.ws

    def open_worksheet(self,name):
        self.ws = self.sht.worksheet(name)
        return self.ws

    def insert_columns(self,col_index,number_of_columns):
        # col_index : Column index after which column(s) would be inserted
        self.ws.insert_cols([None] * number_of_columns, col=col_index, value_input_option='RAW', inherit_from_before=False)

    def merge_cells(self,start,end):
        self.ws.merge_cells("{}:{}".format(start,end), merge_type='MERGE_ALL')
