#!/usr/bin/python3
"""
rints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    q = session.query(State.id).filter(
            State.name == sys.argv[4])
    if not q:
        print("Not found")
    else:
        for state in q:
            print(state[0])
