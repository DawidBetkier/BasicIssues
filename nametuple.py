from collections import namedtuple
from datetime import date

Order = namedtuple('Order', ['product_name', 'category', 'customer_id', 'due_date', 'model'])

if __name__ == "__main__":
    order = Order('PC Keybord', 'IT', 2, date.today(), 'MK220')
    print(order)
    print(order.category)
    print(order.due_date)
    print(order.model)