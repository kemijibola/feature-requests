"""empty message

Revision ID: cf84afa45dcb
Revises: 9bc1533d8291
Create Date: 2018-12-17 12:29:17.787274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf84afa45dcb'
down_revision = '9bc1533d8291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('email', sa.String(length=60), nullable=False))
    op.create_index(op.f('ix_client_email'), 'client', ['email'], unique=True)
    op.create_index(op.f('ix_client_phone_number'), 'client', ['phone_number'], unique=True)
    op.drop_constraint('client_phone_number_key', 'client', type_='unique')
    op.create_index(op.f('ix_feature_title'), 'feature', ['title'], unique=False)
    op.drop_column('feature', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feature', sa.Column('name', sa.VARCHAR(length=60), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_feature_title'), table_name='feature')
    op.create_unique_constraint('client_phone_number_key', 'client', ['phone_number'])
    op.drop_index(op.f('ix_client_phone_number'), table_name='client')
    op.drop_index(op.f('ix_client_email'), table_name='client')
    op.drop_column('client', 'email')
    # ### end Alembic commands ###
