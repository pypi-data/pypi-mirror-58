import json
import os

try:
    from . import Url
    from . import Query
    from . import Create
except:
    import url as Url
    import create as Create
    import query as Query

#####################################
# Get the 'Query'
#####################################

def load_from_file(uri, temporary_path):
    path = Create.folder(temporary_path)
    query_path = Url.download(uri, path, ["query"])
    return Query.get_query_from(query_path[1] + query_path[0])

def load_from_db(plpy, package_name):
    data = {}
    SQL=""+\
        "SELECT * FROM m_installer_information WHERE name='"+package_name+"';"
    result = plpy.execute(SQL)
    if len(result) >= 1:
        data = json.loads(result[0]["sql"])
    return data

def load_from_default():
    default_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/default.py"
    return Query.get_query_from(default_dir)


if __name__ == "__main__":
    
    class fakePLPY:
        ####################
        # This is the default PLPY provided by PostgreSQL.
        ####################
        def execute(self, sql):
            print(sql)
            return [{"sql":'{"info":{"name":"me.faena.postgresql_extension"}}'}]

    # default Query
    print("\ndefault Query\n", load_from_default())

    # from DB
    print("\nfrom DB\n", load_from_db(fakePLPY(),"me.faena.postgresql_extension"))

    # from URI
    print("\nfrom URI\n", load_from_file("https://raw.githubusercontent.com/Sotaneum/PostgreSQL-Extension-Installer/alpha/postgresql_extension_installer/default.py",""))