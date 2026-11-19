"""Testit lippu.py-moduulille. Täydennä tehtävien mukaan (ks. README.md)."""

import pytest

from lippu import kokonaishinta, lippuhinta


def test_aikuisen_hinta():
    # Arrange: valmistellaan syöte
    ika = 30
    # Act: kutsutaan testattavaa funktiota
    hinta = lippuhinta(ika)
    # Assert: tarkistetaan tulos
    assert hinta == 15


# TEHTÄVÄ 2: Raja-arvot yhdellä parametrisoidulla testillä.
# Täydennä alla olevaan listaan pareja (ikä, odotettu hinta).
# Poista sen jälkeen rivi @pytest.mark.skip.
#@pytest.mark.skip(reason="Täydennä raja-arvot ja poista tämä rivi")
@pytest.mark.parametrize(
    "ika, odotettu",
    [
        (0, 0.0),
        (6, 0.0),
        (7, 8.0),
        (17, 8.0),
        (18, 15.0),
        (64, 15.0),
        (65, 10.0),
        (120, 10.0),
    ],
)
def test_lippuhinta_raja_arvot(ika, odotettu):
    assert lippuhinta(ika) == odotettu


# TEHTÄVÄ 3: Virheelliset iät nostavat ValueErrorin.
# Vinkki: with pytest.raises(ValueError):

with pytest.raises(ValueError):
    lippuhinta(-1)
    

with pytest.raises(ValueError):

    lippuhinta(121)
# TEHTÄVÄ 4: Kokonaishinta ja ryhmäalennuksen raja (9 ja 10 lippua).

def test_kokonaishinta_tyhja_lista():
    assert kokonaishinta([]) == 0.0


def test_kokonaishinta_9_aikuista():
    iat = [30] * 9
    assert kokonaishinta(iat) == 135.0


def test_kokonaishinta_10_aikuista():
    iat = [30] * 10
    assert kokonaishinta(iat) == 135.0

### opiskelija ###
def test_opiskelijan_lippuhinta():
    assert lippuhinta(20, opiskelija=True) == 10.0