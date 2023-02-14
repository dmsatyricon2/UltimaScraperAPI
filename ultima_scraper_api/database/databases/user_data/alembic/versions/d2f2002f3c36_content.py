"""content

Revision ID: d2f2002f3c36
Revises: 1454e4d1c6b8
Create Date: 2023-02-13 22:40:57.202281

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.orm import Session

# revision identifiers, used by Alembic.
revision = "d2f2002f3c36"
down_revision = "1454e4d1c6b8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    invalid_conn = op.get_bind()
    database_url = str(invalid_conn.engine.url)
    conn = sa.create_engine(database_url)
    session = Session(bind=conn)
    res = session.execute(sa.text("SELECT id,media_id FROM medias;"))
    results = res.fetchall()
    meta = sa.MetaData()
    meta.reflect(bind=conn, only=("medias",))
    old_table = meta.tables["medias"]

    session = Session(bind=conn)
    for items in results:
        formatted = dict(items._mapping)
        (
            session.query(old_table)
            .filter(old_table.c.id == formatted["id"])
            .update({"media_id_2": formatted["media_id"]})
        )
        session.commit()
    with op.batch_alter_table("medias") as batch_op:
        batch_op.drop_column("media_id")
        batch_op.alter_column("media_id_2", new_column_name="media_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
