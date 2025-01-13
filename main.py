from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime

current_date = datetime.now().date()


if __name__ == '__main__':
    print('Мы находимся в main.py')
    print("Текущая дата:", current_date)
    get_employees()
    calculate_salary()
    