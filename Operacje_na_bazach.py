from _decimal import Decimal

import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='***',
    database='sda2',
    host='localhost',
)

cursor = connection.cursor()
print('Zadanie1')
cursor.execute("""
    SELECT first_name,last_name
    FROM users
    ORDER BY first_name
    LIMIT 10
""")

for row in cursor:
    print(row)

print('\nZadanie2')
cursor.execute("""
    SELECT first_name,last_name
    FROM users
    ORDER BY last_name DESC
    LIMIT 10
""")

for row in cursor:
    print(row)

print('\nZadanie3')
cursor.execute("""
    SELECT first_name,last_name, post_count
    FROM users
    WHERE post_count >= 3400
    ORDER BY post_count DESC
""")

for row in cursor:
    print(row)

print('\nZadanie4')
cursor.execute("""
    SELECT first_name,last_name, post_count, rating
    FROM users
    WHERE post_count >= 3400 or rating > 4.0
    ORDER BY rating DESC
""")

for row in cursor:
    print(row)

print('\nZadanie5')
cursor.execute("""
    SELECT first_name,last_name, post_count, rating, joined_date
    FROM users
    WHERE (post_count >= 3400 or rating > 4.0) and joined_date BETWEEN '2000-01-01' AND '2010-12-31'
    ORDER BY joined_date
""")

for row in cursor:
    print(row)

print('\nZadanie6')
cursor.execute("""
    SELECT first_name,last_name
    FROM users
    WHERE first_name = 'Carolynn' or first_name = 'Christie' or first_name = 'West' 
""")
# WHERE first_name IN ('Carolynn', 'Christie', 'West')

for row in cursor:
    print(row)

print('\nZadanie7')
cursor.execute("""
    SELECT first_name,last_name
    FROM users
    WHERE first_name LIKE 'S%'
    # '___' imięna 3 znaki
""")

for row in cursor:
    print(row)

print('\nZadanie8')
cursor.execute("""
    SELECT first_name, last_name
    FROM users
    WHERE first_name LIKE 'S%a' or first_name LIKE 'D%a'
""")

for row in cursor:
    print(row)

print('\nZadanie9')
cursor.execute("""
    SELECT first_name, last_name
    FROM users
    WHERE last_name LIKE '%G%' or last_name LIKE '%g%'
""")

for row in cursor:
    print(row)

print('\nZadanie10')
cursor.execute("""
    SELECT Count(*) from users
""")

for row in cursor:
    print(row[0])

print('\nZadanie11')
cursor.execute("""
    SELECT SUM(post_count) from users
""")

for row in cursor:
    d: Decimal = row[0]
    print(int(d))

print('\nZadanie12')
cursor.execute("""
    SELECT min(rating), MAX(rating) from users
""")

for row in cursor:
    print(row)

print('\nZadanie13')
cursor.execute("""
    SELECT avg(rating) from users
""")

for row in cursor:
    print(row[0])

print('\nZadanie14')
cursor.execute("""
    SELECT first_name, COUNT(first_name) as name_count from users
    GROUP BY first_name
    ORDER BY name_count DESC
    LIMIT 10
""")

for row in cursor:
    print(row)

print('\nZadanie15')
cursor.execute("""
    SELECT first_name,last_name, post_count, rating from users
    WHERE post_count > 0 AND rating IS NULL
    ORDER BY post_count DESC
""")

for row in cursor:
    print(row)

cursor.close()

connection.close()

if __name__ == '__main__':
    pass
