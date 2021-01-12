"""empty message

Revision ID: 00b4bb16bdae
Revises: 56d873f464d4
Create Date: 2021-01-12 18:44:05.473063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00b4bb16bdae'
down_revision = '56d873f464d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'slack_messages', ['event_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'slack_messages', type_='unique')
    # ### end Alembic commands ###