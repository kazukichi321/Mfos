"""empty message

Revision ID: d5357a178c6a
Revises: 5d83ea0dd2b9
Create Date: 2020-12-17 22:23:30.277938

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd5357a178c6a'
down_revision = '5d83ea0dd2b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zoom_access_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('access_token', sa.String(length=1000), nullable=False),
    sa.Column('refresh_token', sa.String(length=1000), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.CheckConstraint('updated_at >= created_at'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('access_token', table_name='zoom_access_token')
    op.drop_index('refresh_token', table_name='zoom_access_token')
    op.drop_table('zoom_access_token')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zoom_access_token',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('access_token', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('refresh_token', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False),
    sa.Column('updated_at', mysql.DATETIME(), nullable=False),
    sa.CheckConstraint('(`updated_at` >= `created_at`)', name='zoom_access_token_chk_1'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='zoom_access_token_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('refresh_token', 'zoom_access_token', ['refresh_token'], unique=True)
    op.create_index('access_token', 'zoom_access_token', ['access_token'], unique=True)
    op.drop_table('zoom_access_tokens')
    # ### end Alembic commands ###
