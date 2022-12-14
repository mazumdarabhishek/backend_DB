import mysql.connector
from datetime import datetime


class OrderDbQuery:

    def createOrder(self, payload_dict: dict):

        # Establish DB connection
        connection = mysql.connector.connect(host='localhost',
                                             port=3306,
                                             database='foodapp',
                                             user='root',
                                             password='')
        if connection.connection_id:
            print(f"Connection established with ID::{connection.connection_id}")
        else:
            print("Connection not established")

        try:
            # Create cursor
            cur = connection.cursor()

            # insert query string
            INSERT_QUERY = ("INSERT INTO foodapp.order_database"
                        "(orderid, type, ordertime, itemname, unitprice, quantity, totalprice, orderstatus, clientname, clientphone, clientaddress, itemid, itemsize)"
                        "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

            cur.execute(INSERT_QUERY, list(payload_dict.values()))
            connection.commit()
            connection.close()
            return "order entered"
        except Exception as e:

            return "Error occurred:: ", str(e)

    def updateOrder(self, payload_dict: dict, orderid):
        # Establish DB connection
        connection = mysql.connector.connect(host='localhost',
                                             port=3306,
                                             database='foodapp',
                                             user='root',
                                             password='')
        if connection.connection_id:
            print(f"Connection established with ID::{connection.connection_id}")
        else:
            print("Connection not established")

        try:
            # create cursor
            cur = connection.cursor()
            cur.execute("SELECT * FROM foodapp.order_database WHERE orderid = %s",(payload_dict['orderid'],))
            data = cur.fetchone()
            if data:
                for column in payload_dict.keys():
                    UPDATE_QUERY = '''UPDATE foodapp.order_database SET %s = %s WHERE orderid = '%s' ''' % (
                    column, payload_dict[column],orderid)
                    cur.execute(UPDATE_QUERY)
                connection.commit()
                connection.close()
                return "Successfully Updated"
            else:
                return "OrderID Does not exists"

        except Exception as e:
            return "Error occurred while updating records:: ", str(e)



    def changeOrderStatus(self,orderid):
        # Establish DB connection
        connection = mysql.connector.connect(host='localhost',
                                             port=3306,
                                             database='foodapp',
                                             user='root',
                                             password='')
        if connection.connection_id:
            print(f"Connection established with ID::{connection.connection_id}")
        else:
            print("Connection not established")

        # create cursor
        cur = connection.cursor()
        cur.execute("SELECT * FROM foodapp.order_database WHERE orderid = %s",(orderid,))
        data = cur

    def deleteOrder(self):
        pass

    def fetchAllOrders(self):
        pass

    def fetchOrderByID(self):
        pass