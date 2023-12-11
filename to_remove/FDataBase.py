import sqlite3


class FDataBase:
    def __init__(self, db: sqlite3.Connection):
        self.__db = db
        self.__cur = db.cursor()

    def getUsers(self):
        sql = '''SELECT * FROM users'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("error: ", e)

    def getUser(self, username=None, id_of_user=None) -> sqlite3.Row:
        sql = ""
        if id_of_user:
            sql = f'''SELECT * FROM users WHERE id = "{id_of_user}" LIMIT 1 '''
        elif username:
            sql = f'''SELECT * FROM users WHERE username = "{username}" LIMIT 1 '''

        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res[0]
        except sqlite3.Error as e:
            print("error: ", e)

    def addUser(self, email, first_name, last_name, gender, birthday, address, username, password, phone_number):
        try:
            self.__cur.execute(f"INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (email, first_name, last_name, gender, birthday, address, username, password, phone_number))
            self.__db.commit()
            self.add_profile_data(self.getUser(username)["id"], "NULL", "NULL", "NULL", "NULL")
        except sqlite3.Error as e:
            print("error", e)
            return False
        return True

    def add_profile_data(self, userId, avatar, description, englishLevel, groups):
        try:
            self.__cur.execute(f"INSERT INTO usersProfile VALUES(?, ?, ?, ?, ?)", (userId, avatar, description, englishLevel, groups))
            self.__db.commit()
        except sqlite3.Error as e:
            print("error", e)
            return False

        return True

    def get_profile_data(self, userId):
        sql = f'''SELECT * FROM usersProfile WHERE userId = "{userId}" LIMIT 1 '''

        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res[0]
        except sqlite3.Error as e:
            print("error: ", e)

    def update_user_avatar(self, img, user_id):
        try:
            binary = sqlite3.Binary(img)
            self.__cur.execute("UPDATE users SET avatar = ? WHERE id = ? ", (binary, user_id))
            self.__db.commit()
        except sqlite3.Error as e:
            print(e)
