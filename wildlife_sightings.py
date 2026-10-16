
"""Track wildlife sightings and summarize observations."""

import hashlib
import sqlite3


conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE sightings (
        id INTEGER PRIMARY KEY,
        species TEXT,
        zone TEXT,
        count INTEGER
    )
    """
)


def log_sighting(database, species, zone, count, extras=None):
    """Record a sighting and update the species totals."""
    if extras is None:
        extras = {}

    database.execute(
        """
        INSERT INTO sightings (species, zone, count)
        VALUES (?, ?, ?)
        """,
        (species, zone, count),
    )
    extras[species] = extras.get(species, 0) + count
    return extras


def observer_id(observer):
    """Return a short SHA-256-based observer identifier."""
    return hashlib.sha256(observer.encode("utf-8")).hexdigest()[:6]


def zone_summary(database, zone):
    """Return the total number of sightings recorded in a zone."""
    row = database.execute(
        "SELECT SUM(count) FROM sightings WHERE zone = ?",
        (zone,),
    ).fetchone()

    if row[0] is None:
        return 0
    return row[0]


def rarest(database):
    """Return the species with the lowest total sighting count."""
    rows = database.execute(
        """
        SELECT species, SUM(count)
        FROM sightings
        GROUP BY species
        """
    ).fetchall()

    if not rows:
        return "Unknown"

    rarest_species = min(rows, key=lambda row: row[1])
    return rarest_species[0]


def main():
    """Run the wildlife sightings demonstration."""
    totals = log_sighting(conn, "Leopard", "North", 1)
    log_sighting(conn, "Chital", "North", 24, totals)
    log_sighting(conn, "Hornbill", "East", 3, totals)

    if len(totals) != 3:
        raise RuntimeError("Unexpected number of species totals.")

    print(
        observer_id("Arun"),
        zone_summary(conn, "North"),
        rarest(conn),
    )


if __name__ == "__main__":
    main()
