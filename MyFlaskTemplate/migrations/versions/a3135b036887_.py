#!/usr/bin/env python
# coding:utf-8
"""empty message

Revision ID: a3135b036887
Revises: 
Create Date: 2018-08-10 09:52:18.204474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3135b036887'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('piao',
    sa.Column('pid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('detail', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('pid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('piao')
    # ### end Alembic commands ###
