"""order.createtime date->timestamp

Revision ID: cf20121a5001
Revises: 63debef10df6
Create Date: 2023-03-09 11:31:17.507304

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cf20121a5001'
down_revision = '63debef10df6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('createtime',
               existing_type=mysql.DATETIME(),
               type_=sa.Integer(),
               existing_comment='添加时间',
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.alter_column('createtime',
               existing_type=sa.Integer(),
               type_=mysql.DATETIME(),
               existing_comment='添加时间',
               existing_nullable=False)

    # ### end Alembic commands ###
