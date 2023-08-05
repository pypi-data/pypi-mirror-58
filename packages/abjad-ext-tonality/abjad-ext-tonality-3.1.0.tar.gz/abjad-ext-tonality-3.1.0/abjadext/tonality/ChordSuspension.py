import re

import abjad

from .ScaleDegree import ScaleDegree


class ChordSuspension(object):
    """
    Chord suspension.

    ..  container:: example

        Initializes from numbers:

        >>> abjadext.tonality.ChordSuspension('4-b3')
        ChordSuspension('4-b3')

    ..  container:: example

        Initializes from other suspension:

        >>> suspension = abjadext.tonality.ChordSuspension('4-3')
        >>> abjadext.tonality.ChordSuspension(suspension)
        ChordSuspension('4-3')

    9-8, 7-6, 4-3, 2-1 and other types of suspension typical of, for example,
    the Bach chorales.
    """

    ### CLASS VARIABLES ###

    __slots__ = ("_start", "_stop")

    _symbol_regex = re.compile(r"([#|b]?\d+)-([#|b]?\d+)")

    ### INITIALIZER ###

    def __init__(self, figured_bass_string="4-3"):
        if isinstance(figured_bass_string, type(self)):
            figured_bass_string = figured_bass_string.figured_bass_string
        start, stop = self._initialize_by_symbol(figured_bass_string)
        self._start = start
        self._stop = stop

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        """
        Is true when ``argument`` is a chord suspension when start and stop
        equal to those of this chord suspension.

        ..  container:: example

            >>> suspension_1 = abjadext.tonality.ChordSuspension('4-3')
            >>> suspension_2 = abjadext.tonality.ChordSuspension('4-3')
            >>> suspension_3 = abjadext.tonality.ChordSuspension('2-1')

            >>> suspension_1 == suspension_1
            True
            >>> suspension_1 == suspension_2
            True
            >>> suspension_1 == suspension_3
            False


            >>> suspension_2 == suspension_1
            True
            >>> suspension_2 == suspension_2
            True
            >>> suspension_2 == suspension_3
            False


            >>> suspension_3 == suspension_1
            False
            >>> suspension_3 == suspension_2
            False
            >>> suspension_3 == suspension_3
            True

        Returns true or false.
        """
        return abjad.StorageFormatManager.compare_objects(self, argument)

    def __hash__(self):
        """
        Hashes chord suspension.

        Required to be explicitly redefined on Python 3 if __eq__ changes.

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

    def __str__(self):
        """
        Gets string representation of chord suspension.

        Returns string.
        """
        if self.start is not None and self.stop is not None:
            return "{!s}-{!s}".format(self.start, self.stop)
        else:
            return ""

    ### PRIVATE METHODS ###

    def _get_format_specification(self):
        values = [self.figured_bass_string]
        return abjad.FormatSpecification(
            client=self,
            repr_is_indented=False,
            storage_format_is_indented=False,
            storage_format_args_values=values,
        )

    def _initialize_by_pair(self, pair):
        start, stop = pair
        return self._initialize_by_start_and_stop(start, stop)

    def _initialize_by_reference(self, chord_suspension):
        start, stop = chord_suspension.start, chord_suspension.stop
        return self._initialize_by_start_and_stop(start, stop)

    def _initialize_by_start_and_stop(self, start, stop):
        start = ScaleDegree(start)
        stop = ScaleDegree(stop)
        return start, stop

    def _initialize_by_symbol(self, symbol):
        groups = self._symbol_regex.match(symbol).groups()
        start, stop = groups
        start = ScaleDegree(start)
        stop = ScaleDegree(stop)
        return start, stop

    def _initialize_empty(self):
        return None, None

    ### PUBLIC PROPERTIES ###

    @property
    def chord_name(self):
        """
        Gets chord name.

        ..  container:: example

            >>> abjadext.tonality.ChordSuspension('4-b3').chord_name
            'sus4'

            >>> abjadext.tonality.ChordSuspension('b2-1').chord_name
            'susb2'

        Returns string.
        """
        return "sus{!s}".format(self.start)

    @property
    def figured_bass_pair(self):
        """
        Gets figured bass pair.

        ..  container:: example

            >>> abjadext.tonality.ChordSuspension('4-b3').figured_bass_pair
            ('4', 'b3')

            >>> abjadext.tonality.ChordSuspension('b2-1').figured_bass_pair
            ('b2', '1')

        Returns integer pair.
        """
        return str(self.start), str(self.stop)

    @property
    def figured_bass_string(self):
        """
        Gets figured bass string.

        ..  container:: example

            >>> abjadext.tonality.ChordSuspension('4-b3').figured_bass_string
            '4-b3'

            >>> abjadext.tonality.ChordSuspension('b2-1').figured_bass_string
            'b2-1'

        Returns string.
        """
        return "{!s}-{!s}".format(self.start, self.stop)

    @property
    def start(self):
        """
        Gets start.


            >>> abjadext.tonality.ChordSuspension('4-b3').start
            ScaleDegree('4')

            >>> abjadext.tonality.ChordSuspension('b2-1').start
            ScaleDegree('b2')

        Returns scale degree.
        """
        return self._start

    @property
    def stop(self):
        """
        Gets stop.

        ..  container:: example

            >>> abjadext.tonality.ChordSuspension('4-b3').stop
            ScaleDegree('b3')

            >>> abjadext.tonality.ChordSuspension('b2-1').stop
            ScaleDegree('1')

        Returns scale degree.
        """
        return self._stop

    @property
    def title_string(self):
        """
        Gets title string.

        ..  container:: example

            >>> abjadext.tonality.ChordSuspension('4-b3').title_string
            'FourFlatThreeSuspension'

            >>> abjadext.tonality.ChordSuspension('b2-1').title_string
            'FlatTwoOneSuspension'

        Returns string.
        """
        start = self.start.title_string
        stop = self.stop.title_string
        return "{!s}{!s}Suspension".format(start, stop)
