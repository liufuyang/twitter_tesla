from yoyo import read_migrations, get_backend
import os

def run_migrations(db_host, db_port, db_user, db_pass, db_name):

    connect_str = 'postgresql://'+ db_user +':'+ db_pass +'@'+ db_host + ':' + db_port +'/' + db_name
    print(connect_str)
    backend = get_backend(connect_str)
    migrations = read_migrations('db_migration')
    backend.apply_migrations(backend.to_apply(migrations))
