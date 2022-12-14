"""empty message

Revision ID: 65d48d5994a4
Revises: f08a4e946b4b
Create Date: 2022-09-14 15:38:50.419673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65d48d5994a4'
down_revision = 'f08a4e946b4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teacher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=64), nullable=True),
    sa.Column('grade', sa.String(length=64), nullable=True),
    sa.Column('student', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student'], ['student.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('ocena')
    op.add_column('news', sa.Column('title', sa.String(length=64), nullable=True))
    op.add_column('news', sa.Column('news', sa.String(length=800), nullable=True))
    op.drop_column('news', 'tytul')
    op.drop_column('news', 'tresc')
    op.add_column('user', sa.Column('type', sa.String(length=10), nullable=True))
    op.drop_column('user', 'nauczyciel')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('nauczyciel', sa.BOOLEAN(), nullable=True))
    op.drop_column('user', 'type')
    op.add_column('news', sa.Column('tresc', sa.VARCHAR(length=800), nullable=True))
    op.add_column('news', sa.Column('tytul', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('news', 'news')
    op.drop_column('news', 'title')
    op.create_table('ocena',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('przedmiot', sa.VARCHAR(length=64), nullable=True),
    sa.Column('ocena', sa.VARCHAR(length=64), nullable=True),
    sa.Column('uczen', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['uczen'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('grade')
    op.drop_table('teacher')
    op.drop_table('student')
    # ### end Alembic commands ###
