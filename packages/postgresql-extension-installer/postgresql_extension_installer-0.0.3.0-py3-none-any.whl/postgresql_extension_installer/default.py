-->Info<--
--<name>--
me.faena.postgresql_extension_installer
--<Version>--
2019.12.29.0013
--<lib>--
postgresql_extension_installer
--<Provider>--
https://raw.githubusercontent.com/Sotaneum/PostgreSQL-Extension-Installer/beta/postgresql_extension_installer/default.py
-->Table<--
--<m_installer_Information>--
CREATE TABLE m_installer_information(
   sql json,
   version text,
   name text
)
WITH (
   OIDS = TRUE
);
-->Function<--
--<m_installer_install>--
CREATE OR REPLACE FUNCTION m_installer_install(
    uri TEXT
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 LEE DONG GUN(2019.12.28)
    # -- ==========================================================

    from postgresql_extension_installer import Installer

    installer = Installer(plpy)
    try:
        installer.load(query=uri)
        installer.install()
    except Exception as e:
        return str(e)
    return "ok"
$BODY$;
--<m_installer_update>--
CREATE OR REPLACE FUNCTION m_installer_update(
    package_name TEXT
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 LEE DONG GUN(2019.12.28)
    # -- ==========================================================

    from postgresql_extension_installer import Installer

    installer = Installer(plpy)
    try:
        installer.load(package_name=package_name)
        installer.update()
        return "ok"
    except Exception as e:
        return str(e)

$BODY$;
--<m_installer_uninstall>--
CREATE OR REPLACE FUNCTION m_installer_uninstall(
    package_name TEXT
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 LEE DONG GUN(2019.12.28)
    # -- ==========================================================

    from postgresql_extension_installer import Installer

    installer = Installer(plpy)
    try:
        installer.load(package_name=package_name)
        installer.uninstall()
        return "ok"
    except Exception as e:
        return str(e)
$BODY$;
--<m_installer_pylib_update>--
CREATE OR REPLACE FUNCTION m_installer_pylib_update(
    package_name TEXT
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 LEE DONG GUN(2019.12.28)
    # -- ==========================================================

    from postgresql_extension_installer import PythonPackage
    from postgresql_extension_installer import Loader
    from postgresql_extension_installer import Query
    
    try:
        query = Loader.load_from_db(plpy, package_name)
        lib_list = Query.get_lib_from(query)
        PythonPackage.install_all(lib_list)
        return "ok"
    except Exception as e:
        return str(e)
$BODY$;
--<m_installer_delete_cache>--
CREATE OR REPLACE FUNCTION m_installer_delete_cache(
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 LEE DONG GUN(2019.12.28)
    # -- ==========================================================

    from postgresql_extension_installer import Installer

    installer = Installer(plpy)
    try:
        installer.remove_cache()
        return "ok"
    except Exception as e:
        return str(e)
$BODY$;