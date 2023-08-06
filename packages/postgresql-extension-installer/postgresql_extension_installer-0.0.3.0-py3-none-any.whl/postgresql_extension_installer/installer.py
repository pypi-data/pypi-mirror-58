import os
import sys
import subprocess
import shutil

import json

try:
    from . import Loader
    from . import Query
    from . import PythonPackage
    from . import Create
except:
    import loader as Loader
    import query as Query
    import python_package as PythonPackage
    import create as Create

class Installer():
    def __init__(self, plpy, is_log=False, is_print=False):
        self._plpy = plpy
        self._is_log = is_log
        self._is_print = is_print
        self._download_path = Create.folder(os.path.dirname(os.path.abspath("./")).replace("\\","/") + "/pgextinstall_download/")
        self._data = {}
        if self._system_install_check() is False:
            query = Loader.load_from_default()
            Query.install(self._plpy, query)
            Query.install_sql(self._plpy, query)
        else:
            system_query = Loader.load_from_default()
            installed_query = Loader.load_from_db(self._plpy, "me.faena.postgresql_extension_installer")
            Query.update_from_key(self._plpy, installed_query, system_query, "function")
            Query.update_sql(self._plpy, system_query)

    def _system_install_check(self):
        SQL = "" + \
            "SELECT tablename FROM pg_tables WHERE tablename='m_installer_information';"
        result = self._plpy.execute(SQL)
        if len(result) == 1:
            return True
        return False

    def _extension_install_check(self):
        package_name=Query.get_package_name_from(self._data)
        SQL=""+\
            "SELECT * FROM m_installer_information WHERE name='"+package_name+"';"
        result = self._plpy.execute(SQL)
        if len(result) == 1:
            return True
        return False

    def load(self, query=None, package_name=None):
        if package_name:
            self._data = Loader.load_from_db(self._plpy, package_name)
        elif query:
            self._data = Loader.load_from_file(query, self._download_path)

    def update(self):
        if self._data:
            if self._extension_install_check() is True:
                providers = Query.get_provider_from(self._data)
                for provider in providers:
                    load_query = Loader.load_from_file(provider, self._download_path)
                    if load_query:
                        Query.update(self._plpy, self._data, load_query)
                        Query.update_sql(self._plpy, load_query)
                        lib_list = Query.get_lib_from(load_query)
                        if lib_list:
                            PythonPackage.install_all(lib_list)
                        self._data = load_query
                        break
            else:
                self.install()

    def install(self):
        if self._data:
            if self._extension_install_check() is False:
                Query.install(self._plpy, self._data)
                Query.install_sql(self._plpy, self._data)
                lib_list = Query.get_lib_from(self._data)
                if lib_list:
                    PythonPackage.install_all(lib_list)

    def uninstall(self):
        if self._data:
            if self._extension_install_check() is True:
                Query.uninstall(self._plpy, self._data)
                Query.uninstall_sql(self._plpy, self._data)

    def remove_cache(self):
        if os.path.isdir(self._download_path):
            shutil.rmtree(self._download_path)



if __name__ == "__main__":
    class FakePLPY:
        def execute(self, SQL):
            print(SQL)
            return []

    installer = Installer(FakePLPY())
    installer.load(query="https://raw.githubusercontent.com/Sotaneum/PostgreSQL-Extension-Installer/alpha/tests/test.query")
    installer.install()
    installer.update()
    installer.uninstall()
    installer.update()
    installer.uninstall()
    installer.remove_cache()
