#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the engine to connect to MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}', pool_pre_ping=True)

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a configured "Session" class and a session instance
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and order by state id
    states = session.query(State).order_by(State.id).all()

    # Print each state's id and name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
