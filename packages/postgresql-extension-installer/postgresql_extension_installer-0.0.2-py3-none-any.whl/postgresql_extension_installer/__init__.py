# __init__.py
# Copyright (C) 2019 LEE DONG GUN. (gnyontu39@gmail.com) and contributors

import inspect
import os
import sys

__version__ = '0.0.2'

real_path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
sys.path.append(real_path)

try:
    from installer import Installer
    import create as Create # Create Folder
    import loader as Loader # Get the 'Query'
    import python_package as PythonPackage
    import query as Query  # Control Query
    import url as Url # Download File

except ImportError as e:
    print(e," 추가할 수 없습니다.")
    exit(1)


__all__ = [name for name, obj in locals().items()
           if not (name.startswith('_') or inspect.ismodule(obj))]