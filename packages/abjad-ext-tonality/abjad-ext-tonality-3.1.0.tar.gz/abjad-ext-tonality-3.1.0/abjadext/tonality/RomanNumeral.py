import re

import abjad

from .ChordExtent import ChordExtent
from .ChordInversion import ChordInversion
from .ChordQuality import ChordQuality
from .ChordSuspension import ChordSuspension
from .ScaleDegree import ScaleDegree


class RomanNumeral(object):
    """
    Roman numeral.

    ..  container:: example

        Initializes from string:

        >>> abjadext.tonality.RomanNumeral('bII6/4')
        RomanNumeral('bII6/4')

    ..  container:: example

        Initializes from other Roman numeral:

        >>> roman_numeral = abjadext.tonality.RomanNumeral('bII')

    """

    ### CLASS VARIABLES ###

    __slots__ = (
        "_extent",
        "_inversion",
        "_quality",
        "_root_scale_degree",
        "_suspension",
    )

    _figured_bass_string_to_extent = {
        "": 5,
        "6": 5,
        "6/4": 5,
        "7": 7,
        "6/5": 7,
        "4/3": 7,
        "4/2": 7,
    }

    _figured_bass_string_to_inversion = {
        "": 0,
        "6": 1,
        "6/4": 2,
        "7": 0,
        "6/5": 1,
        "4/3": 2,
        "4/2": 3,
    }

    _symbol_regex = re.compile(r"([#|b]*)([i|I|v|V]+)([M|m|o|@|+]?)(.*)")

    ### INITIALIZER ###

    def __init__(self, symbol="V7"):
        groups = self._symbol_regex.match(symbol).groups()
        accidental, roman_numeral, quality, figured_bass = groups
        scale_degree = accidental + roman_numeral
        scale_degree = ScaleDegree(scale_degree)
        figured_bass_parts = figured_bass.split("/")
        naive_figured_bass = [x for x in figured_bass_parts if "-" not in x]
        naive_figured_bass = "/".join(naive_figured_bass)
        extent = self._figured_bass_string_to_extent[naive_figured_bass]
        extent = ChordExtent(extent)
        uppercase = roman_numeral == roman_numeral.upper()
        quality = self._get_quality_name(uppercase, quality, extent.number)
        quality = ChordQuality(quality)
        inversion = self._figured_bass_string_to_inversion[naive_figured_bass]
        inversion = ChordInversion(inversion)
        suspension = [x for x in figured_bass_parts if "-" in x]
        if not suspension:
            suspension = None
        elif 1 < len(suspension):
            raise NotImplementedError("no multiple suspensions yet.")
        else:
            suspension = ChordSuspension(suspension[0])
        self._root_scale_degree = scale_degree
        self._quality = quality
        self._extent = extent
        self._inversion = inversion
        if suspension is not None and suspension.start is None:
            suspension = None
        self._suspension = suspension

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        """
        Is true when ``argument`` is a Roman numeral with scale degree,
        quality, extent, inversion and suspension equal to those of this Roman
        numeral.

        ..  container:: example

            >>> roman_numeral_1 = abjadext.tonality.RomanNumeral('I')
            >>> roman_numeral_2 = abjadext.tonality.RomanNumeral('I')
            >>> roman_numeral_3 = abjadext.tonality.RomanNumeral('V7')

            >>> roman_numeral_1 == roman_numeral_1
            True
            >>> roman_numeral_1 == roman_numeral_2
            True
            >>> roman_numeral_1 == roman_numeral_3
            False


            >>> roman_numeral_2 == roman_numeral_1
            True
            >>> roman_numeral_2 == roman_numeral_2
            True
            >>> roman_numeral_2 == roman_numeral_3
            False

            >>> roman_numeral_3 == roman_numeral_1
            False
            >>> roman_numeral_3 == roman_numeral_2
            False
            >>> roman_numeral_3 == roman_numeral_3
            True

        Returns true or false.
        """
        return abjad.StorageFormatManager.compare_objects(self, argument)

    def __hash__(self):
        """
        Hashes Roman numeral.

        Returns integer.
        """
        hash_values = abjad.StorageFormatManager(self).get_hash_values()
        try:
            result = hash(hash_values)
        except TypeError:
            raise TypeError(f"unhashable type: {self}")
        return result

    def __repr__(self) -> str:
        """
        Gets interpreter representation.
        """
        return abjad.StorageFormatManager(self).get_repr_format()

    ### PRIVATE METHODS ###

    def _get_accidental_name(self):
        accidental = self.root_scale_degree.accidental
        if accidental.semitones != 0:
            return accidental.name.title()
        return ""

    def _get_figured_bass_digits(self):
        characters = self._get_figured_bass_string()
        if characters:
            characters = characters.split("/")
            digits = [int(x) for x in characters]
            return tuple(digits)
        return ()

    def _get_figured_bass_string(self):
        return self.inversion.extent_to_figured_bass_string(self.extent.number)

    def _get_format_specification(self):
        return abjad.FormatSpecification(
            client=self,
            storage_format_is_indented=False,
            storage_format_args_values=[self.symbol],
        )

    def _get_quality_name(self, uppercase, quality_string, extent):
        if quality_string == "o":
            return "diminished"
        elif quality_string == "@":
            return "half diminished"
        elif quality_string == "+":
            return "augmented"
        elif quality_string == "M":
            return "major"
        elif quality_string == "m":
            return "minor"
        elif extent == 5:
            if quality_string == "" and uppercase:
                return "major"
            elif quality_string == "" and not uppercase:
                return "minor"
            else:
                message = "unknown quality string: {!r}."
                message = message.format(quality_string)
                raise ValueError(message)
        elif extent == 7:
            if quality_string == "" and uppercase:
                return "dominant"
            elif quality_string == "" and not uppercase:
                return "minor"
            else:
                message = "unknown quality string: {!r}."
                message = message.format(quality_string)
                raise ValueError(message)
        else:
            message = "unknown extent: {!r}."
            message = message.format(extent)
            raise ValueError(message)

    def _get_quality_symbol(self):
        from abjadext import tonality

        if self.extent == tonality.ChordExtent(5):
            if self.quality == tonality.ChordQuality("diminished"):
                return "o"
            elif self.quality == tonality.ChordQuality("augmented"):
                return "+"
            else:
                return ""
        elif self.extent == tonality.ChordExtent(7):
            if self.quality == tonality.ChordQuality("dominant"):
                return ""
            elif self.quality == tonality.ChordQuality("major"):
                return "M"
            elif self.quality == tonality.ChordQuality("diminished"):
                return "o"
            elif self.quality == tonality.ChordQuality("half diminished"):
                return "@"
            elif self.quality == tonality.ChordQuality("augmented"):
                return "+"
            else:
                return ""
        else:
            raise NotImplementedError

    def _get_roman_numeral_string(self):
        roman_numeral_string = self.root_scale_degree.roman_numeral_string
        if not self.quality.is_uppercase:
            roman_numeral_string = roman_numeral_string.lower()
        return roman_numeral_string

    ### PUBLIC PROPERTIES ###

    @property
    def bass_scale_degree(self):
        """
        Gets bass scale degree.

        ..  container:: example

            >>> abjadext.tonality.RomanNumeral('bII6/4').bass_scale_degree
            ScaleDegree('6')

            >>> abjadext.tonality.RomanNumeral('V7').bass_scale_degree
            ScaleDegree('5')

        Returns scale degree.
        """
        from abjadext import tonality

        root_scale_degree = self.root_scale_degree.number
        bass_scale_degree = root_scale_degree - 1
        bass_scale_degree += 2 * self.inversion.number
        bass_scale_degree %= 7
        bass_scale_degree += 1
        bass_scale_degree = tonality.ScaleDegree(bass_scale_degree)
        return bass_scale_degree

    @property
    def extent(self):
        """
        Gets extent.

        ..  container:: example

            >>> abjadext.tonality.RomanNumeral('bII').extent
            ChordExtent(5)

        Returns extent.
        """
        return self._extent

    @property
    def figured_bass_string(self):
        """
        Gets figured bass string.

        ..  container:: example

            >>> abjadext.tonality.RomanNumeral('II6/5').figured_bass_string
            '6/5'

        Returns string.
        """
        digits = self._get_figured_bass_digits()
        if self.suspension is None:
            return "/".join([str(_) for _ in digits])
        suspension_pair = self.suspension.figured_bass_pair
        figured_bass_list = []
        for n in range(9, 1, -1):
            if n == suspension_pair[0]:
                figured_bass_list.append(str(self.suspension))
            elif n == suspension_pair[1]:
                pass
            elif n in digits:
                figured_bass_list.append(str(n))
        figured_bass_string = "/".join(figured_bass_list)
        return figured_bass_string

    @property
    def inversion(self):
        """
        Gets inversion.

        ..  container:: example

            >>> abjadext.tonality.RomanNumeral('bII').inversion
            ChordInversion(0)

        Returns nonnegative integer.
        """
        return self._inversion

    @property
    def markup(self):
        r"""
        Gets markup.

        ..  container:: example

            >>> markup = abjadext.tonality.RomanNumeral('bII').markup
            >>> abjad.show(markup) # doctest: +SKIP

            ..  docs::

                >>> abjad.f(markup)
                _ \markup { bII }

        Returns markup.
        """
        import abjad

        symbol = self.symbol
        symbol = symbol.replace("#", r"\sharp ")
        return abjad.Markup(symbol, direction=abjad.Down)

    @property
    def quality(self):
        """
        Gets quality.

        ..  container:: example

            >>> abjadext.tonality.RomanNumeral('bII').quality
            ChordQuality('major')

        Returns chord quality.
        """
        return self._quality

    @property
    def root_scale_degree(self):
        """
        Gets root scale degree.

        ..  container:: example

            >>> abjadext.tonality.RomanNumeral('bII').root_scale_degree
            ScaleDegree('b2')

            >>> abjadext.tonality.RomanNumeral('bII6/4').root_scale_degree
            ScaleDegree('b2')

        Returns scale degree.
        """
        return self._root_scale_degree

    @property
    def suspension(self):
        """
        Gets suspension.

        ..  container:: example

            >>> abjadext.tonality.RomanNumeral('bII6/4').suspension is None
            True

            >>> abjadext.tonality.RomanNumeral('V7').suspension is None
            True

        Returns suspension.
        """
        return self._suspension

    @property
    def symbol(self):
        """
        Gets symbolc of Roman numeral.

        ..  container:: example

            >>> abjadext.tonality.RomanNumeral('bII6/4').symbol
            'bII6/4'

            >>> abjadext.tonality.RomanNumeral('V7').symbol
            'V7'

        Returns string.
        """
        result = ""
        result += self.root_scale_degree.accidental.symbol
        result += self._get_roman_numeral_string()
        result += self._get_quality_symbol()
        result += self.figured_bass_string
        return result

    ### PUBLIC METHODS ###

    @staticmethod
    def from_scale_degree_quality_extent_and_inversion(
        scale_degree, quality, extent, inversion
    ):
        """
        Makes Roman numeral from ``scale_degree``, ``quality``, ``extent`` and
        ``inversion``.

        Returns new Roman numeral.
        """
        from abjadext import tonality

        scale_degree = tonality.ScaleDegree(scale_degree)
        quality = tonality.ChordQuality(quality)
        extent = tonality.ChordExtent(extent)
        inversion = tonality.ChordInversion(inversion)
        roman_numeral = RomanNumeral()
        roman_numeral._root_scale_degree = scale_degree
        roman_numeral._quality = quality
        roman_numeral._extent = extent
        roman_numeral._inversion = inversion
        return roman_numeral
