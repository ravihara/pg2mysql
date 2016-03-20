#!/bin/bash -e
# Script for switching a database from PostgreSQL to Mysql/MariaDB
#
# Author - Ravishankar Haranath <ravikh@gmail.com>
# Date Created - 09/Nov/2015

if [ $# -lt 1 -o $# -gt 2 ]; then
  echo "Usage: $(basename $0) <postgresql-db-name> [mysql-engine-name]"
  echo "mysql-engine-name, if not provided, defaults to MyISAM"
  exit 1
fi

pgsql_db="$1"
db_name="$(echo $pgsql_db | sed -e 's/\.\w\+$//')"
tmp_dir="$(mktemp -d)"

mysql_engine=""
if [ -n "$2" ]; then
  mysql_engine="$2"
fi

sudo -u postgres pg_dump $pgsql_db --inserts --disable-dollar-quoting --quote-all-identifiers --format p -c > ${tmp_dir}/${db_name}.pgsql && sync
php pg2mysql_cli.php ${tmp_dir}/${db_name}.pgsql ${tmp_dir}/${db_name}.mysql $mysql_engine && sync
python fix_sql.py ${tmp_dir}/${db_name}.mysql ${tmp_dir}/${db_name}.sql && sync

echo "Migrated DB has been saved in the path - $tmp_dir/${db_name}.sql"
echo "Please copy it to an appropriate location. All Done!!"

exit 0
