from sqlalchemy.types import String, Integer, DATETIME, SmallInteger, DECIMAL, Enum
from flaskr.database.database import db
from sqlalchemy.schema import Column
import enum


class City(db.Model):
    # __bind_key__ = 'second_sample_db'  # config.pyで設定したもの
    __tablename__ = 'city'
    id = Column("ID", Integer, primary_key=True)
    name = Column("Name", String)
    country_code = Column("CountryCode", String)
    district = Column("District", String)
    population = Column("Population", Integer)


class ContinentType(str, enum.Enum):
    asia = "Asia"
    europe = "Europe"
    north_america = "North America"
    africa = "Africa"
    oceania = "Oceania"
    antarctica = 'Antarctica'
    south_america = 'South America'


class Country(db.Model):
    __tablename__ = "country"
    code = Column(String, primary_key=True)
    name = Column(String)
    continent = Column(Enum(ContinentType))
    region = Column("Region", String)
    surface_area = Column("SurfaceArea", DECIMAL(10, 2))
    indep_year = Column("IndepYear", SmallInteger)
    population = Column("Population", Integer)
    life_expectancy = Column("LifeExpectancy", DECIMAL(3, 1))
    gnp = Column("GNP", DECIMAL(10, 2))
    gnp_old = Column("GNPOld", DECIMAL(10, 2))
    local_name = Column("LocalName", String)
    government_form = Column("GovernmentForm", String)
    head_of_state = Column("HeadOfState", String)
    capital = Column("Capital", Integer)
    code2 = Column("Code2", String)


class IsOfficialType(str, enum.Enum):
    t = "T"
    f = "F"


class CountryLaunguage(db.Model):
    __tablename__ = "countrylanguage"
    country_code = Column("CountryCode", String, primary_key=True)
    language = Column("Language", String, primary_key=True)
    is_official = Column(Enum(IsOfficialType))
    percentage = Column("Percentage", DECIMAL(4, 1))

    def __init__(self, id, name, date):
        self.id = id
        self.name = name
        self.date = date
