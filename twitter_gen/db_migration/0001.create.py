#
# file: migrations/0001.create.py
#
from yoyo import step
step(
    """CREATE TABLE tweets (
        id serial PRIMARY KEY,
        tweet varchar (300) NOT NULL,
        created_at timestamptz NOT NULL,
        label_s boolean,
        pred_s boolean,
        pred_p real
        )
    """,
    "DROP TABLE tweets",
)
