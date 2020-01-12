# coding: utf8
from __future__ import unicode_literals

from ...attrs import LIKE_NUM

# Taken from the Dutch language, translated as best as possible for personal purposes.

_num_words = set(
    """
nul een één ean ien een ein iene twee twei drie dree drai drè dri'j vier vear veer vief zes zesse 
zeven zeuvn zeum'n zövvene acht achte negen neggene neagen neegn tien tiene teen elf twoalf derteen
veerteen vearteen viefteen twinnig twintig dertig dartig veartig viertig vieftig zestig zeumtig zeuvntig 
tachntig neagentig  neegntig hoonderd duuzend doezend miljoen
""".split()
)

_ordinal_words = set(
    """
eerste eerstn eerst tweede twijde därde dadde daarde deerde vierde veerdn veerde viefde vieftn zesde 
zeuvende zeuvnde achtste achtstn neegnde tiendn elfde twaolfde dattiende derteende veertiende
veerteende twintigste dartigste dertigste veertigste vieftigste zestigste zeumtigste zeuvntigste tachtigste 
tachntigste neagentigste neegntigste negentigste hoonderdste duuzendste doezendste miljoenste
""".split()
)


def like_num(text):
    # This only does the most basic check for whether a token is a digit
    # or matches one of the number words. In order to handle numbers like
    # "drieëntwintig", more work is required.
    # See this discussion: https://github.com/explosion/spaCy/pull/1177
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    if text.lower() in _num_words:
        return True
    if text.lower() in _ordinal_words:
        return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
