import datetime, sqlite3

class Person:
    def __init__(self, full_name, date_of_birth):
        
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        return

    def is_adult(self):
        dob = self.date_of_birth
        today = str(datetime.date.today())
        currentyear = today[:4]
        year = dob[:4]
        age = int(currentyear) - int(year)
        if age > 18:
            return True
        else:
            return False

    def screen_name(self):
        name = self.full_name
        cleanname = ''
        for i in name:
            if i.isalpha():
                cleanname = cleanname + i

        dob = self.date_of_birth
        month = dob[5:7]
        day = dob[8:]
        screenname = cleanname+month+day
        return screenname

class Staff(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)
        return

    def is_adult(self):
        return True

    def screen_name(self):
        name = self.full_name
        cleanname = ''
        for i in name:
            if i.isalpha():
                cleanname = cleanname + i

        dob = self.date_of_birth
        month = dob[5:7]
        day = dob[8:]
        screenname = cleanname+month+day+"Staff"
        return screenname

class Student(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)
        return

    def is_adult(self):
        return False


    

connection = sqlite3.connect("school.db")
connection.execute("DROP TABLE IF EXISTS People")

openfile = open('task4_1.sql')
data = openfile.read()
openfile.close()

connection.executescript(data)


openfile = open('people.txt')
data = openfile.readlines()
for i in data:
    i = i.strip()
    lst = i.split(",")
    name, dob, status = lst[0], lst[1], lst[2]

    if status == "Person":
        obj = Person(name, dob)

    elif status == "Staff":
        obj = Staff(name, dob)

    else:
        obj = Student(name, dob)

    
    screen = obj.screen_name()

    isadult = obj.is_adult()

    if isadult == True:
        adult = 1

    else:
        adult = 0


    connection.execute("INSERT INTO People(FullName, DateOfBirth, ScreenName, IsAdult) VALUES(?, ?, ?, ?)", (name, dob, screen, adult))

connection.commit()





























                
 
