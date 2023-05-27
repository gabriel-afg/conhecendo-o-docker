"""First Migration

Revision ID: 4bc460dbed2f
Revises: 
Create Date: 2023-04-09 06:05:31.979748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bc460dbed2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('director', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movie_id'), 'movie', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_movie_id'), table_name='movie')
    op.drop_table('movie')
    # ### end Alembic commands ###
