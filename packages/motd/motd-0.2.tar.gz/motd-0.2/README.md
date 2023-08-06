## MOTD

Retrieve famous 'Mathematicians Of The Day' from 
[http://mathshistory.st-andrews.ac.uk/Day_files/Year.html](http://mathshistory.st-andrews.ac.uk/Day_files/Year.html)

Disclaimer: This package is not supported by the University of St-Andrews. This is not an official package!

Output's format is JSON.

## 0.2
Modify to English words command and method names

### Usage as a library

#### Minimal example

``` python3
>>> import motd
>>> motd.motd()
<motd.motd.motd object at 0x7fd2675eb550>
>>> motd.motd().out()
'{"30/12": [{"year": 1869, "fname": "Emilie", "name": "MARTIN", "event": "birth"}, {"year": 1897, "fname": "Stanis\\u0142aw", "name": "SAKS", "event": "birth"}, {"year": 1691, "fname": "Robert", "name": "BOYLE", "event": "death"}, {"year": 1932, "fname": "Eliakim", "name": "MOORE", "event": "death"}, {"year": 1947, "fname": "Alfred North", "name": "WHITEHEAD", "event": "death"}, {"year": 1956, "fname": "Heinrich", "name": "SCHOLZ", "event": "death"}, {"year": 1978, "fname": "Mark Aronovich", "name": "NAIMARK", "event": "death"}, {"year": 1982, "fname": "Philip", "name": "HALL", "event": "death"}]}'
>>> 

```

#### Options

The constructor admits two optional arguments:

* `day` specifying date using a string formated as `DD/MM`
  (default is the current system day)
* `delta` specifying the number of days before (negative
  integer) or after (positivie integer) `day` value. (default is
  0)


``` python3

>>> import motd
>>> motd.motd('01/01').out()
'{"01/01": [{"year": 1803, "fname": "Guglielmo", "name": "LIBRI", "event": "birth"}, ...

```

``` python3

>>> import motd
>>> motd.motd(delta=1).out()
'{"31/12": [{"year": 1856, "fname": "William", "name": "THOMSON", "event": "birth"}, ...
```

``` python3

>>> import motd
>>> motd.motd('01/01', delta=-2).out()
'{"30/12": [{"year": 1869, "fname": "Emilie", "name": "MARTIN", "event": "birth"}, ...
```

``` python3

>>> import motd
>>> motd.motd(day='01/01', delta=-2).out()
'{"30/12": [{"year": 1869, "fname": "Emilie", "name": "MARTIN", "event": "birth"}, ...
```



### Usage in standalone app (code below)

#### How-to use it

1. Copy next code content in a `motd` file.

2. Change eventually the shebang line and make the file executable
`chmod 755 motd`

3. Move it in a path known by your shell. For example: `~/.local/bin`

4. Session example

``` console
$ motd
1869 birth Emilie MARTIN
1897 birth Stanisław SAKS
1691 death Robert BOYLE
1932 death Eliakim MOORE
1947 death Alfred North WHITEHEAD
1956 death Heinrich SCHOLZ
1978 death Mark Aronovich NAIMARK
1982 death Philip HALL
$ motd -d 01/01
1803 birth Guglielmo LIBRI
1878 birth Agner ERLANG
1886 birth Alexander Barrie GRIEVE
1894 birth Satyendranath BOSE
1905 birth Stanisław MAZUR
1912 birth Boris Vladimirovich GNEDENKO
1923 birth Daniel GORENSTEIN
1924 birth Jacques DIXMIER
1931 birth Sergei Ivanovich ADIAN
1748 death Johann BERNOULLI
1787 death Anastácio da CUNHA
...
$ motd -d 01/01 -1
1856 birth William THOMSON
1872 birth Volodymyr LEVYTSKY
1896 birth Carl SIEGEL
1916 birth Douglas NORTHCOTT
1937 birth Vladimir MAZ'YA
1945 birth Leonard ADLEMAN
1952 birth Vaughan JONES
1610 death Ludolph Van CEULEN
1659 death János APÁCZAI
1679 death Giovanni Alfonso BORELLI
1719 death John FLAMSTEED
1894 death Thomas STIELTJES
1912 death Robert FERGUSON
1944 death Nikolai Evgrafovich KOCHIN
1956 death Edwin P ADAMS
1962 death Charles Galton DARWIN
1982 death Kurt FRIEDRICHS

```

Further you can pipe with `sort` command.

You can also change source code of the app to output different
lines.


#### Standalone app code

``` python3

#!/usr/bin/python3
__author__ = "David COBAC"
__date__ = 20191230

import motd
import json
import argparse


parseur_args = argparse.ArgumentParser(
    description="""Mathematicians Of The Day from website
    http://mathshistory.st-andrews.ac.uk/Day_files/Year.html
    not an official package""")

parseur_args.add_argument('-d', '--day', help='DD/MM')
parseur_args.add_argument('delta',
                          nargs='?',
                          default='+0')

args = parseur_args.parse_args()

m = motd.motd(args.day, args.delta)
dico = json.loads(m.sortie())
for k in dico:
    # print(k)
    for entree in dico[k]:
        s = str(entree['year'])
        s += " "
        s += entree['event']
        s += " "
        s += entree['fname']
        s += " "
        s += entree['name']
        #
        print(s)

```

## about

`motd` is rather an attempt to publish on the `PyPi` packages
index than a fully completed python project, I do not recommend
to use it for professionnal purpose. You have to consider this
package as an experiment.
