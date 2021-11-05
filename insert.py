import sqlite3conn = sqlite3.connect('students.db')
conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
"VALUES (1, 'John', '001', 'Bangalore', '10th')")
conn.execute("INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS) "
"VALUES (2, 'Naren', '002', 'Hyd', '12th')")
conn.commit()
conn.close()
