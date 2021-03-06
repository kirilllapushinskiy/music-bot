from sqlalchemy import (
    Column, Integer,
    MetaData, String, Table, DateTime, func,
)

convention = {
    'all_columnnames': lambda constraint, table: ''.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix%(table_name)s%(all_column_names)s',
    'uq': 'uq%(table_name)s%(all_column_names)s',
    'ck': 'ck%(table_name)s%(constraint_name)s',
    'fk': 'fk%(table_name)s%(all_column_names)s%(referred_table_name)s',
    'pk': 'pk%(table_name)s'
}

metadata = MetaData(naming_convention=convention)

tracks = Table(
    'tracks', metadata,
    Column('id', Integer, primary_key=True),
    Column('file_id', String(100)),
    Column('artist', String(100), nullable=False),
    Column('title', String(100), nullable=False),
    Column('duration', Integer),
    Column('url', String(250), nullable=False),
    Column('cover_url', String(250)),
    Column('updated_at', DateTime, default=func.now(), onupdate=func.now())
)

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('vk_id', Integer, nullable=False)
)
