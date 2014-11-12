#!/bin/sh

echo "Creating MySQL db"
mysql -uvk_lang_model -pvk_lang_model < create_sql_db.sql

echo "Creating initial tables"
python ../manage.py syncdb


#user - admin
#email - admin@admin.com
#password - admin
