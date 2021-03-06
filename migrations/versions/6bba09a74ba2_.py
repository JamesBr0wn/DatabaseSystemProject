"""empty message

Revision ID: 6bba09a74ba2
Revises: 1bd75496fc53
Create Date: 2019-06-08 17:46:45.314285

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bba09a74ba2'
down_revision = '1bd75496fc53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vouchers', sa.Column('total_money', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vouchers', 'total_money')
    # ### end Alembic commands ###
