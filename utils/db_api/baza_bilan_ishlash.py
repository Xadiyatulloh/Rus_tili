import sqlite3


class Database:
    def __init__(self, path_to_db="baza.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str , parametrs: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parametrs:
            parametrs = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parametrs)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql="""
        CREATE TABLE myfiles_teacher (
            id int NOT NULL,
            Name varchar (255) NOT NULL,
            email varchar (255),
            language varchar(3),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)


    @staticmethod
    def format_args(sql,parametres:dict):
            sql+= " AND ".join([
                f"{item} = ?" for item in parametres

                ])
            return sql, tuple(parametres.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = 'uz'):
        sql = """
            INSERT INTO Users(id,Name,email,language) VALUES(?,?,?,?)
            """
        self.execute(sql,parametrs=(id, name, email, language), commit=True)

    def select_all_users(self):
            sql = "SELECT * FROM myfiles_teacher "
            return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT* FROM myfiles_teacher WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parametrs=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_teacher;", fetchone=True)


    def delete_users(self):
        self.execute("DELETE FROM myfiles_teacher WHERE TRUE", commit=True)

    def user_qoshish(self, ism: str, telegrami: int, familiya: str = None, ):
        sql = """
            INSERT INTO azolar(ism,familiya,telegrami) VALUES(?, ?, ?)
            """
        self.execute(sql,parametrs=(ism, familiya, telegrami), commit=True)

    def select_all_foydalanuvchilar(self):
            sql = "SELECT * FROM azolar"
            return self.execute(sql, fetchall=True)

    def select_all_menular(self):
            sql = "SELECT * FROM menu"
            return self.execute(sql, fetchall=True)

    def select_rus_tili(self, **kwargs):
        sql = "SELECT* FROM rus_tili WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parametrs=parameters, fetchall=True)

    def select_rus_til(self, **kwargs):
        sql = "SELECT* FROM rus_tili WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parametrs=parameters, fetchone=True)

    def select_all_rus_tili_darsliklar(self):
            sql = "SELECT * FROM rus_tili"
            return self.execute(sql, fetchall=True)



def logger(statement):
    print(f"""
____________________________
Executing:
{statement}
_____________________________
""")