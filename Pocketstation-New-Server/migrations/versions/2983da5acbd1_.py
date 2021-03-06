"""empty message

Revision ID: 2983da5acbd1
Revises: c2ed97ad1cc5
Create Date: 2019-02-28 11:07:41.378382

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2983da5acbd1'
down_revision = 'c2ed97ad1cc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lesson_', sa.String(length=255), nullable=True))
    op.drop_column('user', 'lesson')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lesson', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('user', 'lesson_')
    # ### end Alembic commands ###
