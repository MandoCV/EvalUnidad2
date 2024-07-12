from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@localhost:3307/hospital"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



# URI para la base de datos MySQL
#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_YPv9gKHJKOhamUwUu3N@mysql-e331420-utxicotepec-f492.e.aivencloud.com:20907/defaultdb"

# Crear el motor de la base de datos
#engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear una sesión local
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear la base declarativa
#Base = declarative_base()