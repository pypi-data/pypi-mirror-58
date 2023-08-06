-->Table<--
--<m_installer_Information>--
CREATE TABLE m_installer_information(
   sql json,
   version text
)
WITH (
   OIDS = TRUE
);
--<m_installer_Information>--
-->Function<--
--<m_installer_update>--
CREATE OR REPLACE FUNCTION public.m_installer_update(
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 KSNU InfoLab. (2019.07.15 20:35)
    # -- ==========================================================

    from postgresql_deepgeo.installer import Installer

    installer = Installer(plpy)
    return installer.update()[1]

$BODY$;

ALTER FUNCTION public.m_installer_update()
    OWNER TO postgres;
--<m_installer_update>--
--<m_installer_uninstall>--
CREATE OR REPLACE FUNCTION public.m_installer_uninstall(
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 KSNU InfoLab. (2019.07.15 20:35)
    # -- ==========================================================

    from postgresql_deepgeo.installer import Installer

    installer = Installer(plpy)
    return installer.uninstall()[1]

$BODY$;

ALTER FUNCTION public.m_installer_uninstall()
    OWNER TO postgres;
--<m_installer_uninstall>--
--<m_installer_pylib_update>--
CREATE OR REPLACE FUNCTION public.m_installer_pylib_update(
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 KSNU InfoLab. (2019.07.15 20:35)
    # -- ==========================================================

    from postgresql_deepgeo.installer import Installer

    installer = Installer(plpy)
    return installer.python_lib_update()[1]

$BODY$;

ALTER FUNCTION public.m_installer_pylib_update()
    OWNER TO postgres;
--<m_installer_pylib_update>--
--<m_installer_delete_cache>--
CREATE OR REPLACE FUNCTION public.m_installer_delete_cache(
	)
    RETURNS TEXT
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
AS $BODY$
    # -- ==========================================================
    # --    Installer

    # --    Copyright 2019 KSNU InfoLab. (2019.07.15 20:35)
    # -- ==========================================================

    from postgresql_deepgeo.installer import Installer

    installer = Installer(plpy)
    return installer.remove_cache()[1]

$BODY$;

ALTER FUNCTION public.m_installer_delete_cache()
    OWNER TO postgres;
--<m_installer_delete_cache>--