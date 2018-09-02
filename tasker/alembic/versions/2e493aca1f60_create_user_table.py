"""create user table

Revision ID: 2e493aca1f60
Revises: 
Create Date: 2018-09-02 18:18:55.284832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e493aca1f60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('login', sa.String(50), nullable=False, unique=True),
        sa.Column('first_name', sa.String(50)),
        sa.Column('last_name', sa.String(50)),
        sa.Column('password', sa.String(50)),
        sa.Column('email', sa.String(500), unique=True),
    )


def downgrade():
    op.drop_table('users')
