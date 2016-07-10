
__depends__ = ['0001.create']

step(
    """CREATE INDEX idx_created_at ON tweets(created_at DESC);""",
    "DROP INDEX idx_created_at",
)
