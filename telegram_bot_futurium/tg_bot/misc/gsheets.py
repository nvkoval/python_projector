import gspread
from tg_bot.services.servives import select_user


# Authentication to interact with the Google Drive API
gc = gspread.service_account("tgbot_futurium.json")
sheet = gc.open("Futurium_price")
worksheet_num = sheet.worksheet("num_classes")
worksheet_users = sheet.worksheet("users_from_bot")


def num_class_left(name: str) -> str:
    cell = worksheet_num.find(name)
    num_class_left = worksheet_num.cell(cell.row, 5).value
    return num_class_left
