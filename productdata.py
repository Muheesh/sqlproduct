import sqlite3
a = sqlite3.connect("product.db")
# a.execute('''create table productdata(
#                             code integer,
#                             name text,
#                             price integer,
#                             distributor text,
#                             manufacture text
# ); ''')
# print("Table created")
getPdcode = input("Enter product code:")
getPdname = input("Enter product name:")
getPdprice = input("Enter product price:")
getPddistributor = input("Enter distributor name:")
getManufacture = input("Enter Manufacturer name:")
a.execute("insert into productdata(code,name,price,distributor,manufacture)\
 values("+getPdcode+",'"+getPdname+"',"+getPdprice+",'"+getPddistributor+"','"+getManufacture+"')")
a.commit()
a.close()
print("table inserted")