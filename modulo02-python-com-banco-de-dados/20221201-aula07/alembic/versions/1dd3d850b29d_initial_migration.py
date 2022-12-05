"""initial migration

Revision ID: 1dd3d850b29d
Revises: 
Create Date: 2022-12-05 20:32:16.019045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dd3d850b29d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_tags',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_posts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['tb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_users_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['tb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_comments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['tb_posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_posts_tags',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['tb_posts.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tb_tags.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_posts_tags')
    op.drop_table('tb_comments')
    op.drop_table('tb_users_profiles')
    op.drop_table('tb_posts')
    op.drop_table('tb_users')
    op.drop_table('tb_tags')
    # ### end Alembic commands ###
