VALID_DBMS = ('mysql',)
def validate(dbms: str):
    if dbms not in VALID_DBMS:
        raise ValueError(f'Unsupported DBMS: {dbms}')