Övningar: Sorterings- och sökalgoritmer
=======================================

Detta repository innehåller övningar som behandlar sortering och sökning.


Övningarna
----------
Övningarna finns i moduler i paketet exercises.
Förväntad funktion finns i de docstrings som hör ihop med funktionerna.

För att köra linter och enhetstester kan du använda följande kommandon.

.. code-block::

  python manage.py lint
  python manage.py test

För vissa övningar förväntas du själv skriva enhetstester. Detta görs med
fördel i testfiler med beskrivande namn. (De måste ha formen :code:`test_*.py`.)

.. code-block::

  python manage.py test --coverage

Kör testerna med code coverage-analys. Används med fördel för att få en
uppfattning om vilken kod du har kvar att skriva tester till. En HTML-rapport
skapas på sökvägen :code:`./tmp/coverage/index.html`.

Innan du börjar
---------------
Skapa den virtuella körmiljön med de paket som behövs.

.. code-block::

  pyvenv venv

Aktivera den virtella körmiljön:

.. code-block::

  . venv/bin/activate

Installera de paket som behövs för uppgiften:

.. code-block::

  pip install -r requirements.txt
