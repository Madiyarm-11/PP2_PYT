import psycopg2
from psycopg2.extras import DictCursor

params = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "680057",  
    "port": "5432"
}

def manage_contacts():
    name, phone = "Ivan", "+79001112233"
    pattern = "Ivan"

    try:
        with psycopg2.connect(**params) as conn:
            
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                
                
                cursor.execute("CALL upsert_contact(%s, %s)", (name, phone))
                print(f"Контакт {name} успешно обработан.")

                
                cursor.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
                
                results = cursor.fetchall()
                if results:
                    for row in results:
                        print(f"Найдено: {row['name']} | {row['phone']}")
                else:
                    print("Ничего не найдено.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    manage_contacts()