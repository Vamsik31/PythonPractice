def greet(name):
    return f"Hello, {name}!"


 
def create_transaction(connection, Transaction_Id, Member_id, Date,Amount,Tran_type,Desc:None):
    cursor = connection.cursor()
    cursor.execute(f"""
    INSERT INTO members (Transaction_Id, Member_id, Date,Amount,Tran_type,Descfname, lname, gender)
    VALUES (%s, %s, %s,%s, %s, %s);
    """, (Transaction_Id, Member_id, Date,Amount,Tran_type,Desc))
    connection.commit()
    #id = cursor.fetchone()[0]
    print(f"Record inserted successfully!")


def retrieve_transactions(connection, member_id=None):
    cursor = connection.cursor()
    if(member_id is None):
        query = "SELECT * FROM transactions;"
    else:
        query = f"SELECT * FROM transactions where id = {member_id};"
        #query = "SELECT * FROM members where id = " + member_id
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.commit()
    for row in rows:
        print(row)


def update_transactions(connection, Transaction_Id, Member_id, Date,Amount,Tran_type,Desc):
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE members
    SET first_name = %s, last_name = %s
        WHERE id = %s;
    """, (Transaction_Id, Member_id, Date,Amount,Tran_type,Desc))
    #connection.commit()
    print("Record updated successfully!")
    print("updated data")
    retrieve_transactions(connection, Transaction_Id)


def delete_transactions(connection, member_id):
    cursor = connection.cursor()
    cursor.execute(f"""
    DELETE FROM members
    WHERE id = {member_id};
    """)
    connection.commit()
    print("Record deleted successfully!")