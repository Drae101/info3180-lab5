"""empty message

Revision ID: 4a1661884453
Revises: b2bce1f61558
Create Date: 2017-02-22 18:22:17.906423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a1661884453'
down_revision = 'b2bce1f61558'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'user_profile', ['password'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_profile', type_='unique')
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
