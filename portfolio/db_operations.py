import mysql.connector
import datetime
import time

def mysql_connect():
    # Establish a connection to the MySQL database
    db_con = mysql.connector.connect(
        host="18.232.38.249",
        user="ot39",
        password="NT27",
        database="bible"
    )
    return db_con

def table():
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    # Execute a SELECT query
    query = '''CREATE TABLE skills(
                id int PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255),
                stream VARCHAR(50)
                );
                '''
    table = db_session.execute(query)
    print("Table created successfully", table)



def create_record():
    payload = {
        "name": "Jenkins",
        "stream": "DevOps"
                }
    fields = list(payload.keys())
    values = list(payload.values())
    fields = ",".join(item for item in fields)
    values = ",".join("\'" + str(item) + "\'" if type(item) == str else str(item) for item in values)
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    insert_query = f"insert into bible.skills({fields}) values ({values})"
    print(insert_query)
    db_session.execute(insert_query)
    db_con.commit()



def retrieve_records():
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    # Execute a SELECT query
    query = "SELECT * FROM skills"
    db_session.execute(query)

    # Fetch all records from the result set
    records = db_session.fetchall()
    import time
    print("records", records)
    print("type(records)", type(records))
    print("\n \n ")
    time.sleep(5)
    # Process the fetched records
    i = 1
    for record in records:
        # Access individual columns using indexing or column names
        print(f"record{i}", record)
        print("type(record)", type(record))
        print("\n")
        i += 1
        # time.sleep(5)
        column1 = record[0]
        column2 = record[1]
        # ... continue accessing other columns as needed
        # print(column1, column2)

def update_record():
    start_provision_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    update_query = f"update bible.skills set stream='devops'where name='Python'"
    print(update_query)
    db_session.execute(update_query)
    db_con.commit()

def delete_record():
    start_provision_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    update_query = f"DELETE FROM bible.skills where name='Python'"
    print(update_query)
    db_session.execute(update_query)
    db_con.commit()

def mysql_close():
    db_con = mysql_connect()
    # Create a cursor to interact with the database
    db_session = db_con.cursor()
    # Close the cursor and database connection
    db_session.close()
    db_con.close()

if __name__ == "__main__":
    mysql_connect()
    # table()
    create_record()
    retrieve_records()
    # update_record()
    # delete_record()
    mysql_close()