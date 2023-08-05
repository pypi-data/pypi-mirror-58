import abjad


class ChordExtent(object):
    """
    Chord extent.

    ..  container:: example

        Initializes from number:

        >>> abjadext.tonality.ChordExtent(7)
        ChordExtent(7)

    ..  container:: example

        Initializes from other chord extent:

        >>> extent = abjadext.tonality.ChordExtent(7)
        >>> abjadext.tonality.ChordExtent(extent)
        ChordExtent(7)

    Defined equal to outer interval of any root-position chord.
    """

    ### CLASS VARIABLES ###

    __slots__ = ("_number",)

    _acceptable_number = (5, 7, 9)

    _extent_number_to_extent_name = {5: "triad", 7: "seventh", 9: "ninth"}

    ### INITIALIZER ###

    def __init__(self, number=5):
        if isinstance(number, int):
            if number not in self._acceptable_number:
                message = "can not initialize extent: {}."
                raise ValueError(message.format(number))
            number = number
        elif isinstance(number, type(self)):
            number = number.number
        self._number = number

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        """
        Is true when ``argument`` is a chord extent with number equal to that
        of this chord extent.

        ..  container:: example

            >>> extent_1 = abjadext.tonality.ChordExtent(5)
            >>> extent_2 = abjadext.tonality.ChordExtent(5)
            >>> extent_3 = abjadext.tonality.ChordExtent(7)

            >>> extent_1 == extent_1
            True
            >>> extent_1 == extent_2
            True
            >>> extent_1 == extent_3
            False

            >>> extent_2 == extent_1
            True
            >>> extent_2 == extent_2
            True
            >>> extent_2 == extent_3
            False

            >>> extent_3 == extent_1
            False
            >>> extent_3 == extent_2
            False
            >>> extent_3 == extent_3
            True

        Returns true or false.
        """
        return abjad.StorageFormatManager.compare_objects(self, argument)

    def __hash__(self):
        """
        Hashes chord extent.

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

    def _get_format_specification(self):
        values = [self.number]
        return abjad.FormatSpecification(
            client=self,
            repr_is_indented=False,
            storage_format_is_indented=False,
            storage_format_args_values=values,
        )

    ### PUBLIC PROPERTIES ###

    @property
    def name(self):
        """
        Gets name.

        ..  container:: example

            >>> abjadext.tonality.ChordExtent(5).name
            'triad'

            >>> abjadext.tonality.ChordExtent(7).name
            'seventh'

        Returns string.
        """
        return self._extent_number_to_extent_name[self.number]

    @property
    def number(self):
        """
        Gets number.

        ..  container:: example

            >>> abjadext.tonality.ChordExtent(7).number
            7

        Returns nonnegative integer.
        """
        return self._number
