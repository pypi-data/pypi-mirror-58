import subprocess

TESTPYPI = "-i https://test.pypi.org/simple/ "

def _subprocess(command):
    result = str(subprocess.check_output(command,shell=True,stderr=subprocess.PIPE))
    return result.replace("\\n","\n").replace("\\r","\r")

def _command_install(package, version=None, is_test_pypi=False, pip_version=""):
    command = "pip" + pip_version +" install "
    if is_test_pypi is True:
        command += TESTPYPI
    command += package
    if version is not None:
        command += "=" + version
    command += " " + " --upgrade --user"
    return command

def _command_uninstall(package, pip_version=""):
    return "pip" + pip_version +" uninstall " + package +" -y"

def uninstall(package, pip_version=""):
    return _subprocess(_command_uninstall(package, pip_version=pip_version))

def install(package, pip_version=""):
    data = package.split(",")
    if len(data) == 1:
        return _subprocess(_command_install(package, pip_version=pip_version))
    else:
        if "1" in data[1]:
            return _subprocess(_command_install(data[0], is_test_pypi=True, pip_version=pip_version))
        else:
            return _subprocess(_command_install(data[0], is_test_pypi=False, pip_version=pip_version))

def install_all(package_list, pip_version=""):
    message = ""
    try:
        package_log = ""
        for package in package_list:
            package_log += install(package, pip_version) + "\n"
        message = "install_all >> True\n\n" +  package_log + "end\n"
    except Exception as e:
        message = "install_all >> False -> " + str(e)
    return message

if __name__ == "__main__":

    print("\n uninstall ConfigHelper \n", uninstall("ConfigHelper"))

    print("\n install ConfigHelper \n", install("ConfigHelper"))

    print("\n uninstall ConfigHelper \n", uninstall("ConfigHelper"))

    print("\n install ConfigHelper, contrib-extension \n", install_all(["ConfigHelper", "contrib-extension"]))

    print("\n uninstall ConfigHelper \n", uninstall("ConfigHelper"))

    print("\n uninstall contrib-extension \n", uninstall("contrib-extension"))