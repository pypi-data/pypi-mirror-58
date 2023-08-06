import sqlite3;

def rhythmicDB(db_name = "SQLite", *args, **kwargs):
    """
    DB handlers factory
    """
    if db_name == "SQLite":
        return SQLiteDB(*args, **kwargs);
    else:
        return None;

def insertQueryFromDict(table_name, the_dict):

    column_names = the_dict.keys();
    column_names_string = ", ".join(column_names);

    values_to_insert_string = "";

    for parameter in column_names:
        values_to_insert_string += "'{}', ".format(the_dict[parameter]);

    values_to_insert = values_to_insert_string[:-2];

    the_query = "INSERT INTO {} ({}) VALUES ({});".format(table_name, column_names_string, values_to_insert);

    return the_query;

class SQLiteDB:
    """ A class to handle SQLite3 database """

    def __init__(self, db_filename):

        self.connection = sqlite3.connect(db_filename);
        self.cursor = self.connection.cursor();

    def execute(self, sql_request):
        """ Execute a single sql command """

        self.cursor.execute(sql_request);

        if (self.cursor.lastrowid):
            return self.cursor.lastrowid;
            
        else:
            return self.cursor.fetchall();

    def runScript(self, sql_script):
        """ Execute a script passed as a byte- or unicode string """

        self.cursor.executescript(sql_script);

        if (self.cursor.lastrowid):
            return self.cursor.lastrowid;
            
        else:
            return self.cursor.fetchall();

    def __enter__(self):

        return self;

    def __exit__(self, type, value, traceback):

        self.connection.commit();
        self.connection.close();