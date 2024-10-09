from datetime import datetime

def get_days_from_today(date):
    date_1 = datetime.strptime(date, '%Y-%m-%d') 
    date_today = datetime.today()
    difference = int(date_today.toordinal() - date_1.toordinal())
    return difference
    

result = get_days_from_today('2024-10-9')
print(result)
    