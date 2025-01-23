import mysql.connector as co

# Connection to MySQL server
ob = co.connect(host="localhost", user="root", password="Ghos@789")
cur = ob.cursor()

# Creating the database and table if not exists
cur.execute("create database if not exists Details")
cur.execute("Use Details")
cur.execute("create table if not exists Staff(SNO int,Name varchar(50),Department varchar(30),DOJ date,Salary int not null)")
ob.commit()

# Function to add new staff information
def add_info():
    s = int(input("Enter Serial Number:"))
    n = input("Name:")
    dep = input("Enter Department:")
    dt = input("Date of Joining(YYYY-MM-DD):")
    sal = int(input("Enter Salary Amount:"))
    cur.execute("insert into Staff(SNO,Name,Department,DOJ,Salary) values (%s, %s, %s, %s, %s)", (s, n, dep, dt, sal))
    ob.commit()
    print("Details Added Successfully")

# Function to update staff salary
def update_sal():
    SNO = int(input("Enter Serial Number whose salary you want to update: "))
    nsal = int(input("Enter New Salary: "))
    cur.execute("update Staff set Salary = %s where SNO = %s", (nsal, SNO))
    cur.execute("select * from Staff where SNO = %s", (SNO,))
    for i in cur:
        SNO, Name, Department, DOJ, Salary = i
        print(SNO, "\t", Name, "\t", Department, "\t", DOJ, "\t", Salary)
    ob.commit()
    print("Detail Updated Successfully")

# Function to delete staff record
def del_info():
    SNO = int(input("Enter Serial Number whose record you want to delete: "))
    cur.execute("delete from Staff where SNO = %s", (SNO,))
    print("Record Deleted Successfully")
    ob.commit()

# Function to display all records
def display():
    print("All Record Details")
    cur.execute("select * from Staff")
    fa = cur.fetchall()
    ob.commit()
    k = ['SNO', 'Name', 'Department', 'DOJ', 'Salary']
    for SNO, Name, Department, DOJ, Salary in fa:
        print(SNO, "\t", Name, "\t", Department, "\t", DOJ, "\t", Salary)
    ob.commit()

# Function to search staff record
def search():
    print("Search details")
    s = int(input("Enter the SNO to Search: "))
    cur.execute("select * from Staff where SNO = %s", (s,))
    for a in cur:
        SNO, Name, Department, DOJ, Salary = a
        print(SNO, "\t", Name, "\t", Department, "\t", DOJ, "\t", Salary)
    ob.commit()

# Main program
print("PHILIPS MANAGEMENT SYSTEM")

while True:
    print("1-Add new Staff")
    print("2-Update Staff Detail")
    print("3-Delete Staff Record")
    print("4-Display All Record")
    print("5-Search Record")
    print("6-Exit")

    choice = int(input("Enter Choice (1 to 6): "))

    if choice == 1:
        add_info()
    elif choice == 2:
        update_sal()
    elif choice == 3:
        del_info()
    elif choice == 4:
        display()
    elif choice == 5:
        search()
    elif choice == 6:
        break
    else:
        print("You Entered a Wrong Number")

ob.close()
