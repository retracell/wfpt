"""initial tables

Revision ID: 145feefe74a8
Revises: None
Create Date: 2014-03-03 02:09:20.671205

"""

# revision identifiers, used by Alembic.
revision = '145feefe74a8'
down_revision = None

from alembic import op

def upgrade():
    op.execute("""
    CREATE TABLE prices (
        id INT NOT NULL AUTO_INCREMENT,
        date DATE,
        location_name VARCHAR(64),
        good_name VARCHAR(64),
        high FLOAT,
        low FLOAT,
        mean FLOAT,
        PRIMARY KEY(id)
   );
    """)

def downgrade():
    op.execute("""
    DROP TABLE prices;
    """)

