import subprocess
import json
import os
import sys
import create
import url
import shutil
from datetime import datetime

version = "0.0.1.54"

def _load_install_query(path):
    f = open(path, 'r')
    key = ""
    sub_key = ""
    temp = ""
    data = {}
    while True:
        line = f.readline()
        if not line: break
        if "-->" in line and "<--" in line:
            key = line.replace("-->","").replace("<--","").replace("\n","")
            if key not in data:
                data[key] = {}
            temp = ""
        elif "--<" in line and ">--" in line:
            temp_sub_key = line.replace(">--","").replace("--<","").replace("\n","")
            if sub_key == temp_sub_key:
                data[key][sub_key] = temp
            else:
                sub_key = temp_sub_key
            temp = ""
        else:
            temp+=line
    f.close()
    return data

def log(context):
    file_ = os.path.dirname(os.path.abspath("./")).replace("\\","/") + "/Installer.log"
    now = datetime.now()
    str_ = now.strftime('%Y-%m-%d %H:%M:%S') + " > " + context + "\n"
    try:
        with open(file_, "a") as myfile:
            myfile.write(str_)
    except:
        print(str_)

class Installer():
    def __init__(self, plpy, install_query=None):
        log("Installer >> Verison : " + version)
        self._plpy = plpy
        self._base_path = os.path.dirname(os.path.abspath("./")).replace("\\","/")
        if install_query is not None:
            log("Installer >> Load From URI")
            path = self._base_path + "/download"
            log("Installer >> "+path)
            path = create.folder(path)
            query_path = url.download(install_query, path, ["query"])
            self._data = _load_install_query(query_path[1] + query_path[0])
            self._default_data()
        else:
            log("Installer >> Load From Table")
            self._data = self._load_local_table()
            log("Installer >> "+str(self._data))
        
    def _load_local_table(self):
        SQL=""+\
            "SELECT * FROM m_installer_information;"
        result = self._plpy.execute(SQL)
        if len(result) >= 1:
            return json.loads(result[0]["sql"])
        return {

        }
    def _load_default_data(self):
        default_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\","/") + "/default.py"
        log("_default_data >> " + default_dir)
        data = _load_install_query(default_dir)
        return data

    def _default_data(self):
        data = self._load_default_data()
        self._install(data, "Table")
        SQL=""+\
            "INSERT INTO m_installer_information VALUES('"+json.dumps(self._data)+"', "+"'"+self._data["Info"]["Version"].replace("\n","")+"');"
        self._plpy.execute(SQL)
        self._install(data, "Function")

    def _install(self, data, key):
        try:
            if key in data:
                for i in data[key]:
                    self._plpy.execute(data[key][i])
            return True, "_install >> True"
        except Exception as e:
            print("_install >> "+str(e))
            return False, "_install >> "+str(e)

    def _install_type(self):
        return self._install(self._data, "Type")

    def _install_table(self):
        return self._install(self._data, "Table")

    def _install_functions(self):
        return self._install(self._data, "Function")

    def _isInstall(self):
        SQL=""+\
            "SELECT tablename FROM pg_tables WHERE tablename='m_installer_information';"
        result = self._plpy.execute(SQL)
        if len(result) == 1:
            return True
        return False

    def _isNew(self):
        if "Info" in self._data and "Provider" in self._data["Info"]:
            providers = self._data["Info"]["Provider"].split("\n")
            for provider in providers:
                new_data = _load_install_query(url.download(provider, "", ["query"]))
                if "Info" in new_data and "Version" in new_data["Info"]: 
                    if new_data["Info"]["Version"] >= self._data["Info"]["Version"]:
                        return False
        return True

    def _uninstall(self, data):
        try:
            for key in data:
                if key == "Info":
                    continue
                for sub_key in data[key]:
                    SQL = "DROP " + key + " " + sub_key
                    self._plpy.execute(SQL)
            return True, "_uninstall >> True"
        except Exception as e:
            log("_uninstall >> " + str(e))
            return False, "_uninstall >> False -> " + str(e)

    def _install_pylib_package(self, package, isTestPypi=False):
        if package == "postgresql_deepgeo":
            data = self._load_default_data()
            self._uninstall(data)
        testPypi = "-i https://test.pypi.org/simple/ "
        if isTestPypi is False:
            testPypi = ""
        command = "pip3 install " + testPypi + package + " --upgrade --user"
        log("_install_pylib_package >> command -> " + command)
        result = str(subprocess.check_output([command],shell=True,stderr=subprocess.PIPE))
        log("_install_pylib_package >> result -> " + result)
        if package == "postgresql_deepgeo":
            self._default_data()
        log("_install_pylib_package >> end")
        return result

    def remove_cache(self):
        shutil.rmtree(self._base_path+"/download/")

    def python_lib_update(self):
        package_list = []
        try:
            lib = self._data["Info"]["lib"].split("\n")
            for i in lib:
                if i != "":
                    package_list.append(i.replace(" ",""))
            package_log = ""
            for package in package_list:
                package_log += self._install_pylib_package(package, True) + "\n"
            return True, "python_lib_update >> True >> " +  package_log + " end"
        except Exception as e:
            log("python_lib_update >> False -> "+str(e))
            return False, "python_lib_update >> False -> " + str(e)

    def uninstall(self):
        #if self._isInstall() == False:
        #    log("uninstall >> Try use install function.")
        #    return False
        r, code = self._uninstall(self._data)
        if r == True:
            data = self._load_default_data()
            r, code = self._uninstall(data)
            if r == True:
                return True, "uninstall >> True"
            else:
                return False, "uninstall >> False -> " + code
        return False, "uninstall >> False -> " + code

    def update(self):
        if self._isInstall() == False:
            log("update >> Try use install function.")
            return False
        if self._isNew() == True:
            log("update >> The last version has already been installed.")
            return False
        try:
            r, code = self._uninstall(self._data)
            if r == True:
                if self._isInstall() == False:
                    self._install_type()
                    self._install_table()
                    self._install_functions()
            else:
                return False, "update >> False -> " + code
        except Exception as e:
            log("update >> "+str(e))
            return False, "update >> False -> "+str(e)
        log("update >> Updated")
        return True, "update >> True"

    def install(self):
        if self._isInstall() == True:
            print("install >> Already installed. If you want update, try use update function.")
            return False, "install >> False -> Already installed. If you want update, try use update function."
        try:
            r, code = self.python_lib_update()
            if r == True:
                self._install_type()
                self._install_table()
                self._install_functions()
            else:
                return False, "install >> False -> "+ code
        except Exception as e:
            print("install >> "+str(e))
            return False, "install >> False -> "+str(e)
        print("install >> Installed")
        return True

if __name__ == "__main__":
    class FakePLPY:
        
        def execute(self, SQL):
            print(SQL)
            return []

    installer = Installer(FakePLPY(), "http://duration.digimoon.net/dev/test/pldeepgeo/install.query")
    installer.install()
    installer.update()
    installer.uninstall()
    installer.update()
    installer.uninstall()
    installer.remove_cache()
