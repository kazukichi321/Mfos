"""empty message

Revision ID: 72acc444942e
Revises: 578575648a3b
Create Date: 2020-12-20 23:34:10.435540

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '72acc444942e'
down_revision = '578575648a3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('schedule', 'sort_date',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('schedule', 'sort_date',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###
