"""empty message

Revision ID: 3e06c1fbbeff
Revises: d5155ab4db73
Create Date: 2020-08-22 17:00:12.671373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e06c1fbbeff'
down_revision = 'd5155ab4db73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.add_column('artist', sa.Column('genres', sa.ARRAY(sa.String()), nullable=True))
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.drop_column('artist', 'genres')
    
    # ### end Alembic commands ###
