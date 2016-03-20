## Utility to convert a postgresql database to mysql ##

__This project needs more testing and feedback, though. Use it at your own risk!__

Most of the information holds good, as given by Original Author. Important updates are addition of a python script to fix minor issues with sql conversion and, a shell script which does all the job for us. You essentially, need to use only the "migrate.sh" script. The syntax is as follows.


## CLI usage ##
***migrate.sh <postgresql-db-name> [mysql-db-engine]***
mysql-db-engine is optional and, it defaults to MyISAM


## Original Author
Credit goes to:
Author: James Grant
Lightbox Technolgoies
http://www.lightbox.org


Special thanks to [N3X15](http://www.nexisonline.net/index.php/2015/07/18/migrating-gitlab-from-postgresql-to-mysqlmariadb/) for valuable pointers.
