"""empty message

Revision ID: 80aec7e67365
Revises: 769086df7bef
Create Date: 2022-09-07 15:27:32.389043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80aec7e67365'
down_revision = '769086df7bef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('nauczyciel', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'nauczyciel')
    # ### end Alembic commands ###
