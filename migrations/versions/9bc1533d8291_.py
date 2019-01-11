"""empty message

Revision ID: 9bc1533d8291
Revises: e3a91d80c4c3
Create Date: 2018-12-12 03:44:15.762064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bc1533d8291'
down_revision = 'e3a91d80c4c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('feature', 'description',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('feature', 'description',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###