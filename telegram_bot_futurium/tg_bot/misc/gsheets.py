import gspread

# Authentication to interact with the Google Drive API
gc = gspread.service_account("tgbot_futurium.json")
sheet = gc.open("Futurium_price")
worksheet_num = sheet.worksheet("num_lessons")

def num_lessons_left(name: str) -> str:
    cell = worksheet_num.find(name)
    num_lessons_left = worksheet_num.cell(cell.row, 2).value
    return num_lessons_left
