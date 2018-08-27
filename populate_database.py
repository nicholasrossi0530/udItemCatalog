from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Genre, Artist

engine = create_engine('sqlite:///music_catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

# Category: Jazz
genreJazz = Genre(
    name = "Jazz"
)
session.add(genreJazz)
session.commit()

artistJazz1 = Artist(
    name = "Kamasi Washington",
    description = "Kamasi Washington (born February 18, 1981) is an American jazz saxophonist, composer, producer, and bandleader. Washington is known mainly for playing tenor saxophone.",
    instrument = "Saxophone",
    labels = "Young Turks, XL, Brainfeeder",
    associated_acts = "Flying Lotus, Ibeyi, Kendrick Lamar, Run the Jewels, Thundercat",
    genre = genreJazz
)
session.add(artistJazz1)
session.commit()

artistJazz2 = Artist(
    name = "Brad Mehldau",
    description = "Bradford Alexander 'Brad' Mehldau is an American jazz pianist, composer, and arranger. Mehldau studied music at The New School, and toured and recorded while still a student.",
    instrument = "Piano",
    labels = "Warner Bros., Nonesuch",
    associated_acts = "Joshua Redman, Mark Guiliana, Chris Thile, Kurt Rosenwinkel",
    genre = genreJazz
)
session.add(artistJazz2)
session.commit()

artistJazz3 = Artist(
    name = "Herbie Hancock",
    description = "Herbert Jeffrey Hancock (born April 12, 1940) is an American pianist, keyboardist, bandleader, composer and actor.",
    instrument = "Piano",
    labels = "Columbia, Blue Note, Warner Bros., Verve",
    associated_acts = "Clark Terry, Miles Davis Quintet, Wayne Shorter, Chick Corea, the Headhunters, V.S.O.P., Jaco Pastorius, Joni Mitchell, Howard Jones",
    genre = genreJazz
)
session.add(artistJazz3)
session.commit()

artistJazz4 = Artist(
    name = "Chick Corea",
    description = "Armando Anthony 'Chick' Corea (born June 12, 1941) is an American jazz pianist/electric keyboardist and composer.",
    instrument = "Piano",
    labels = "ECM, Polydor, Stretch, Warner Bros.",
    associated_acts = "Miles Davis, Circle, Return to Forever, Chick Corea Elektric Band, Chick Corea's Akoustic Band, Five Peace Band, Gary Burton",
    genre = genreJazz
)
session.add(artistJazz4)
session.commit()