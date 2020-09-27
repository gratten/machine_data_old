"""updated kit table

Revision ID: f4a8aacb197f
Revises: df218c3aa780
Create Date: 2020-09-27 12:00:55.133906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4a8aacb197f'
down_revision = 'df218c3aa780'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kit', sa.Column('customer', sa.String(length=64), nullable=True))
    op.add_column('kit', sa.Column('project', sa.String(length=8), nullable=True))
    op.add_column('kit', sa.Column('serialnum', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_kit_project'), 'kit', ['project'], unique=False)
    op.drop_constraint(None, 'kit', type_='foreignkey')
    op.create_foreign_key(None, 'kit', 'machine', ['serialnum'], ['serialnum'])
    op.drop_column('kit', 'machine_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kit', sa.Column('machine_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'kit', type_='foreignkey')
    op.create_foreign_key(None, 'kit', 'machine', ['machine_id'], ['id'])
    op.drop_index(op.f('ix_kit_project'), table_name='kit')
    op.drop_column('kit', 'serialnum')
    op.drop_column('kit', 'project')
    op.drop_column('kit', 'customer')
    # ### end Alembic commands ###
