
import random as r
"""Is this a Docstring in public module?."""


class Greeting(object):
    """Composition of greetings and methods for getting."""

    GREETINGS = ["Hello, sir",
                 "Home is Ready",
                 "Waddup Dawg"]

    def getRandom():
        """Return a random greeting."""
        return r.choice(Greeting.GREETINGS)


class Farewell(object):
    """Composition of farewells and methods for getting."""

    FAREWELLS = ["Bye, sir",
                 "Good bye lord"]

    def getRandom():
        """Return a random farewell."""
        return r.choice(Farewell.FAREWELLS)


class Songs(object):
    """Composition of songs and methods for getting."""

    RUSSKI = "https://zf.fm/download/2814983"

