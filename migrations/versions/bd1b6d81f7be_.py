"""empty message

Revision ID: bd1b6d81f7be
Revises: b8ffabb44eee
Create Date: 2020-12-20 20:45:05.699101

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bd1b6d81f7be'
down_revision = 'b8ffabb44eee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.create_unique_constraint(None, 'slack_channel_members', ['user_id', 'channel_id'])
    op.add_column('slack_channels', sa.Column('channel_id', sa.String(length=50), nullable=False))
    op.create_index(op.f('ix_slack_channels_channel_id'), 'slack_channels', ['channel_id'], unique=False)
    op.drop_index('ix_slack_channels_name', table_name='slack_channels')
    op.add_column('slack_messages', sa.Column('file_id', sa.String(length=20), nullable=True))
    op.add_column('slack_messages', sa.Column('reaction', sa.String(length=50), nullable=True))
    op.alter_column('slack_messages', 'channel_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('slack_messages', 'channel_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.drop_column('slack_messages', 'reaction')
    op.drop_column('slack_messages', 'file_id')
    op.create_index('ix_slack_channels_name', 'slack_channels', ['name'], unique=False)
    op.drop_index(op.f('ix_slack_channels_channel_id'), table_name='slack_channels')
    op.drop_column('slack_channels', 'channel_id')
    op.drop_constraint(None, 'slack_channel_members', type_='unique')
    # ### end Alembic commands ###
