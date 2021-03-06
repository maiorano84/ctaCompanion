"""empty message

Revision ID: 30228d27a270
Revises: 
Create Date: 2020-05-24 21:58:12.585162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30228d27a270'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('base',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('job', sa.String(length=16), nullable=True),
    sa.Column('rarity', sa.String(length=16), nullable=True),
    sa.Column('element', sa.String(length=16), nullable=True),
    sa.Column('gender', sa.String(length=16), nullable=True),
    sa.Column('crusher', sa.Integer(), nullable=True),
    sa.Column('fly', sa.Integer(), nullable=True),
    sa.Column('blitz', sa.Integer(), nullable=True),
    sa.Column('atk', sa.Integer(), nullable=True),
    sa.Column('hp', sa.Integer(), nullable=True),
    sa.Column('defense', sa.Integer(), nullable=True),
    sa.Column('crit', sa.Integer(), nullable=True),
    sa.Column('critDmg', sa.Integer(), nullable=True),
    sa.Column('movespeed', sa.Integer(), nullable=True),
    sa.Column('aps', sa.Integer(), nullable=True),
    sa.Column('arange', sa.Integer(), nullable=True),
    sa.Column('resistance', sa.Integer(), nullable=True),
    sa.Column('frenzy', sa.Integer(), nullable=True),
    sa.Column('dodge', sa.Integer(), nullable=True),
    sa.Column('stun', sa.Integer(), nullable=True),
    sa.Column('stunTime', sa.Integer(), nullable=True),
    sa.Column('aoe', sa.Integer(), nullable=True),
    sa.Column('ult', sa.Integer(), nullable=True),
    sa.Column('kshp', sa.Integer(), nullable=True),
    sa.Column('gold', sa.Integer(), nullable=True),
    sa.Column('freeze', sa.Integer(), nullable=True),
    sa.Column('freezeTime', sa.Integer(), nullable=True),
    sa.Column('freezeDmg', sa.Integer(), nullable=True),
    sa.Column('burn', sa.Integer(), nullable=True),
    sa.Column('burnTime', sa.Integer(), nullable=True),
    sa.Column('burnDmg', sa.Integer(), nullable=True),
    sa.Column('poison', sa.Integer(), nullable=True),
    sa.Column('poisonTime', sa.Integer(), nullable=True),
    sa.Column('poisonDmg', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_base_aoe'), 'base', ['aoe'], unique=False)
    op.create_index(op.f('ix_base_aps'), 'base', ['aps'], unique=False)
    op.create_index(op.f('ix_base_arange'), 'base', ['arange'], unique=False)
    op.create_index(op.f('ix_base_atk'), 'base', ['atk'], unique=False)
    op.create_index(op.f('ix_base_blitz'), 'base', ['blitz'], unique=False)
    op.create_index(op.f('ix_base_burn'), 'base', ['burn'], unique=False)
    op.create_index(op.f('ix_base_burnDmg'), 'base', ['burnDmg'], unique=False)
    op.create_index(op.f('ix_base_burnTime'), 'base', ['burnTime'], unique=False)
    op.create_index(op.f('ix_base_crit'), 'base', ['crit'], unique=False)
    op.create_index(op.f('ix_base_critDmg'), 'base', ['critDmg'], unique=False)
    op.create_index(op.f('ix_base_crusher'), 'base', ['crusher'], unique=False)
    op.create_index(op.f('ix_base_defense'), 'base', ['defense'], unique=False)
    op.create_index(op.f('ix_base_dodge'), 'base', ['dodge'], unique=False)
    op.create_index(op.f('ix_base_element'), 'base', ['element'], unique=False)
    op.create_index(op.f('ix_base_fly'), 'base', ['fly'], unique=False)
    op.create_index(op.f('ix_base_freeze'), 'base', ['freeze'], unique=False)
    op.create_index(op.f('ix_base_freezeDmg'), 'base', ['freezeDmg'], unique=False)
    op.create_index(op.f('ix_base_freezeTime'), 'base', ['freezeTime'], unique=False)
    op.create_index(op.f('ix_base_frenzy'), 'base', ['frenzy'], unique=False)
    op.create_index(op.f('ix_base_gender'), 'base', ['gender'], unique=False)
    op.create_index(op.f('ix_base_gold'), 'base', ['gold'], unique=False)
    op.create_index(op.f('ix_base_hp'), 'base', ['hp'], unique=False)
    op.create_index(op.f('ix_base_job'), 'base', ['job'], unique=False)
    op.create_index(op.f('ix_base_kshp'), 'base', ['kshp'], unique=False)
    op.create_index(op.f('ix_base_movespeed'), 'base', ['movespeed'], unique=False)
    op.create_index(op.f('ix_base_name'), 'base', ['name'], unique=True)
    op.create_index(op.f('ix_base_poison'), 'base', ['poison'], unique=False)
    op.create_index(op.f('ix_base_poisonDmg'), 'base', ['poisonDmg'], unique=False)
    op.create_index(op.f('ix_base_poisonTime'), 'base', ['poisonTime'], unique=False)
    op.create_index(op.f('ix_base_rarity'), 'base', ['rarity'], unique=False)
    op.create_index(op.f('ix_base_resistance'), 'base', ['resistance'], unique=False)
    op.create_index(op.f('ix_base_stun'), 'base', ['stun'], unique=False)
    op.create_index(op.f('ix_base_stunTime'), 'base', ['stunTime'], unique=False)
    op.create_index(op.f('ix_base_ult'), 'base', ['ult'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('registered', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('hero',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('awaken', sa.Integer(), nullable=True),
    sa.Column('wpn', sa.Integer(), nullable=True),
    sa.Column('medals', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('base_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['base_id'], ['base.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_hero_awaken'), 'hero', ['awaken'], unique=False)
    op.create_index(op.f('ix_hero_level'), 'hero', ['level'], unique=False)
    op.create_index(op.f('ix_hero_medals'), 'hero', ['medals'], unique=False)
    op.create_index(op.f('ix_hero_wpn'), 'hero', ['wpn'], unique=False)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_hero_wpn'), table_name='hero')
    op.drop_index(op.f('ix_hero_medals'), table_name='hero')
    op.drop_index(op.f('ix_hero_level'), table_name='hero')
    op.drop_index(op.f('ix_hero_awaken'), table_name='hero')
    op.drop_table('hero')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_base_ult'), table_name='base')
    op.drop_index(op.f('ix_base_stunTime'), table_name='base')
    op.drop_index(op.f('ix_base_stun'), table_name='base')
    op.drop_index(op.f('ix_base_resistance'), table_name='base')
    op.drop_index(op.f('ix_base_rarity'), table_name='base')
    op.drop_index(op.f('ix_base_poisonTime'), table_name='base')
    op.drop_index(op.f('ix_base_poisonDmg'), table_name='base')
    op.drop_index(op.f('ix_base_poison'), table_name='base')
    op.drop_index(op.f('ix_base_name'), table_name='base')
    op.drop_index(op.f('ix_base_movespeed'), table_name='base')
    op.drop_index(op.f('ix_base_kshp'), table_name='base')
    op.drop_index(op.f('ix_base_job'), table_name='base')
    op.drop_index(op.f('ix_base_hp'), table_name='base')
    op.drop_index(op.f('ix_base_gold'), table_name='base')
    op.drop_index(op.f('ix_base_gender'), table_name='base')
    op.drop_index(op.f('ix_base_frenzy'), table_name='base')
    op.drop_index(op.f('ix_base_freezeTime'), table_name='base')
    op.drop_index(op.f('ix_base_freezeDmg'), table_name='base')
    op.drop_index(op.f('ix_base_freeze'), table_name='base')
    op.drop_index(op.f('ix_base_fly'), table_name='base')
    op.drop_index(op.f('ix_base_element'), table_name='base')
    op.drop_index(op.f('ix_base_dodge'), table_name='base')
    op.drop_index(op.f('ix_base_defense'), table_name='base')
    op.drop_index(op.f('ix_base_crusher'), table_name='base')
    op.drop_index(op.f('ix_base_critDmg'), table_name='base')
    op.drop_index(op.f('ix_base_crit'), table_name='base')
    op.drop_index(op.f('ix_base_burnTime'), table_name='base')
    op.drop_index(op.f('ix_base_burnDmg'), table_name='base')
    op.drop_index(op.f('ix_base_burn'), table_name='base')
    op.drop_index(op.f('ix_base_blitz'), table_name='base')
    op.drop_index(op.f('ix_base_atk'), table_name='base')
    op.drop_index(op.f('ix_base_arange'), table_name='base')
    op.drop_index(op.f('ix_base_aps'), table_name='base')
    op.drop_index(op.f('ix_base_aoe'), table_name='base')
    op.drop_table('base')
    # ### end Alembic commands ###
