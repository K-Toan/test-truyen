from enum import Enum


class Genre(str, Enum):
    shonen = "Shonen"
    adventure = "Adventure"
    sport = "Sports"
    humor = "Humorous"
    drama = "Drama"
    tragedy = "Tragedy"
