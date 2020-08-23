"""empty message

Revision ID: 17f105b5d278
Revises: a8a0a1bd8f95
Create Date: 2020-08-23 16:50:30.193695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17f105b5d278'
down_revision = 'a8a0a1bd8f95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'shows', 'venue', ['venue_id'], ['id'])
    op.create_foreign_key(None, 'shows', 'artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_constraint(None, 'shows', type_='foreignkey')
    # ### end Alembic commands ###
