"""First Migration

Revision ID: bbbde19b1861
Revises: 
Create Date: 2021-06-01 17:27:12.232620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbbde19b1861'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('venue')
    op.drop_table('artist')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('city', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('state', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('genres', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.CHAR(length=500), autoincrement=False, nullable=False),
    sa.Column('facebook_link', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='artist_pkey')
    )
    op.create_table('venue',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('name', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('city', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('state', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('address', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('phone', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('image_link', sa.CHAR(length=500), autoincrement=False, nullable=False),
    sa.Column('facebook_link', sa.CHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='venue_pkey')
    )
    op.drop_table('Venue')
    op.drop_table('Artist')
    # ### end Alembic commands ###
