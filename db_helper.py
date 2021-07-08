import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "cs348348",
    database = "perfect_party"
)

print("Connection to DB: perfect_party")

cursor = db.cursor()

schema_customer = "INSERT INTO perfect_party.Customer (UserId,\
                            Password, \
                            Firstname, \
                            Lastname, \
                            Phone, \
                            Email, \
                            Address, \
                            Postalcode) VALUES \
                            (%s, %s, %s, %s, %s, %s, %s, %s)"

schema_supplier = "INSERT INTO perfect_party.Supplier (Supplier_ID,\
                            Phone, \
                            Supplier_name, \
                            Company_name, \
                            Company_Address, \
                            Email) VALUES \
                            (%s, %s, %s, %s, %s, %s)"

schema_record = "INSERT INTO perfect_party.Supply_record (Supplier_ID,\
                            Transaction, \
                            Product_ID, \
                            Price, \
                            Quantity) VALUES \
                            (%s, %s, %s, %s, %s)"


schema_order = "INSERT INTO perfect_party.OrderInfo ( Billingaddr, \
                    Iscomplete ,\
                    Orderitem ,\
                    Paidamount ,\
                    Ispaid ,\
                    Paidtype ,\
                    Order_number ,\
                    Cardtype ,\
                    Event_id ,\
                    UserId ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

schema_event = "INSERT INTO  perfect_party.Event (Event_id , \
                    Budget , \
                    Capacity , \
                    Event_Type , \
                    Party_open_time , \
                    Party_close_time , \
                    Location , \
                    Customization , \
                    Delivery_time , \
                    UserId , \
                    Venue_id ) VALUES \
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

def insert_db(table, schema, value):
    """
        Insert record into table
        Args: value is tuple, table and schema are strings
    """
    cursor.execute(schema, value)
    db.commit()
    print(cursor.rowcount, "record inserted into db: " + table)

def select_db(table, cond):
    """
        Select all columns from table based on cond
        Args: all strings
        Return: records are list of tuples

    """
    query = "SELECT * FROM " + table + " WHERE " + cond
    cursor.execute(query)
    records = cursor.fetchall()
    return records

def selectAll_db(table, name="*"):
    """
        Select all columns from table
        Args: all strings
        Return: records are list of tuples

    """
    query = "SELECT " + name + " FROM " + table
    cursor.execute(query)
    records = cursor.fetchall()
    return records

def delete_db(table, cond):
    """
        Delete matching rows from table based on cond
        Args: all strings
    """
    query = "DELETE FROM " + table + " WHERE " + cond
    print(query)
    cursor.execute(query)
    db.commit()
    print(cursor.rowcount, "record deleted from db: " + table)


def update_db(table, set, wherecond):
    """
        Update matching rows from table based on cond
        Args: all strings
    """
    query = "UPDATE " + table + " SET " + set + " WHERE " + wherecond
    print(query)
    cursor.execute(query)
    db.commit()
    print(cursor.rowcount, "record updated in db: " + table)

def generate_id(table, pk):
    """
        Generate unique Id for table
        Args: table and pk are strings where pk means primary key name
        Return: string
    """
    query = "SELECT " + pk + " FROM " + table
    cursor.execute(query)
    records = cursor.fetchall()
    if records == []:
        return "000000"
    pks = [x[0] for x in records]
    print(pks)
    pks.sort(key=int)
    max_add1 = str(int(pks[-1]) + 1)
    return max_add1.rjust(6, '0')

def join_Order_Event(userid):
    query = "select * from perfect_party.Event as A inner join perfect_party.OrderInfo as B on A.Event_id=B.Event_id where A.UserId = '"+userid+"' "
    cursor.execute(query)
    records = cursor.fetchall()
    return records

def join_customer_order_event():
    query = "SELECT * FROM (perfect_party.Event as A inner join perfect_party.OrderInfo as B on A.Event_id=B.Event_id) inner join perfect_party.Customer  as C on C.UserId=A.UserId;"
    cursor.execute(query)
    records = cursor.fetchall()
    return records
