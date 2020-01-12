# coding: utf8
from __future__ import unicode_literals

# The original stop words list (added in f46ffe3) was taken from
# http://www.damienvanholten.com/downloads/dutch-stop-words.txt
# and consisted of about 100 tokens.
# In order to achieve parity with some of the better-supported
# languages, e.g., English, French, and German, this original list has been
# extended with 200 additional tokens. The main source of inspiration was
# https://raw.githubusercontent.com/stopwords-iso/stopwords-nl/master/stopwords-nl.txt.
# However, quite a bit of manual editing has taken place as well.
# Tokens whose status as a stop word is not entirely clear were admitted or
# rejected by deferring to their counterparts in the stop words lists for English
# and French. Similarly, those lists were used to identify and fill in gaps so
# that -- in principle -- each token contained in the English stop words list
# should have a Dutch counterpart here.

# Copied from Dutch, but altered by exploring Wikipedia articles.

STOP_WORDS = set(
    """
aal al achter allind allebie allein allen altied an ärg arg  argaander as aandere aans ander andere  aover aordig
beide beie  better bie bienao bi'j bi-j biejen bin binnen bint
daar dårüm dat dät de dee den der derbie dertoe derveur deur deran die dij disse dit dizze daor door doaras daoras daormee doarmee daoran doaran daornet doarnet daormet doarmet doarmit daormit döörvan döörveur d'r dus duur
e een eerste ef en eigen et ene
gien gin geliek
had hebben hee he hef het heur heure hier hum 
ie ien iene in inkelde is ik
je
kan kloar
lang liever leever
mar meer meeste meesten meestentieds meer mer meyr minder mit mid mien mie miej
n nao naobie naobiej naobij naodat naor ne neffens net neet niet noa nog now noe nooit
oek oet of ok ook om omdebi'j onder op oaver aover oare over overigens ou oezelf
paor
rundumme rundum
samen self sikkom sinds slim soms somstieden sülv summege sund syn
't t te tegen teeng ter tiedens tiejens toch to tot tussen
um under uut
van vaeke vanaf vanof vanwegen vake veul veule veur veuraal veural veuraf veurbij veurbie veurdat vöäl vöär volgens völle vule
wal wat was wanneer weader weer wel wier waor woar waoran woaran waorbij woarbij waorbie woarbie waordeur woardeur waorvan woarvan waordeur wodde wodt woerbie woervan woerdeur woeran wol wör wörden wördden wörren wört
zain ze zels zie zien zoas zonder zovölle zowat zowel zowat zwat zölf zikzölf zich
""".split()
)
