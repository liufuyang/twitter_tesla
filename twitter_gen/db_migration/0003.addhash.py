
__depends__ = ['0001.create']

step(
    """
    ALTER TABLE tweets ADD COLUMN t_hash_int bigint;
    CREATE INDEX idx_t_hash_int ON tweets(t_hash_int);
    """,
    """
    ALTER TABLE tweets DROP COLUMN t_hash_int ;
    DROP INDEX idx_t_hash_int;
    """,
)
