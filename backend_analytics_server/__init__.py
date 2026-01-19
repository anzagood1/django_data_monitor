import pymysql

# 1. Instalamos PyMySQL como si fuera MySQLdb
pymysql.install_as_MySQLdb()

import MySQLdb

# Forzamos a que reporte una versión compatible (ej: 2.2.6)
if hasattr(MySQLdb, 'version_info'):
    MySQLdb.version_info = (2, 2, 6, 'final', 0)
else:
    # En caso de que la estructura cambie, forzamos directamente
    MySQLdb.version_info = (2, 2, 6, 'final', 0)