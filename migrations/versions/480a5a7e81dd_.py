"""empty message

Revision ID: 480a5a7e81dd
Revises: fb0bef1c703c
Create Date: 2023-01-30 17:05:34.184459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '480a5a7e81dd'
down_revision = 'fb0bef1c703c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=45), nullable=True),
    sa.Column('product_id', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.product_id'], ),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('product_id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart')
    # ### end Alembic commands ###
