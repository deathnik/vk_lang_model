#!/bin/sh

echo "Creating MySQL db"
mysql -uroot -padmin < create_sql_db.sql

echo "Creating initial tables"
python ../manage.py syncdb


#user - admin
#email - admin@admin.com
#password - admin
