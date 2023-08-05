import abjad


class ChordQuality(object):
    """
    Chord quality.

    ..  container:: example

        Initializes from string:

        >>> abjadext.tonality.ChordQuality('major')
        ChordQuality('major')

    ..  container:: example

        Initializes from other chord quality:

        >>> quality = abjadext.tonality.ChordQuality('major')
        >>> abjadext.tonality.ChordQuality(quality)
        ChordQuality('major')

    """

    ### CLASS VARIABLES ###

    __slots__ = ("_quality_string",)

    _acceptable_quality_strings = (
        "augmented",
        "diminished",
        "dominant",
        "half diminished",
        "major",
        "minor",
    )

    _uppercase_quality_strings = ("augmented", "dominant", "major")

    ### INITIALIZER ###

    def __init__(self, quality_string="major"):
        quality_string = str(quality_string)
        if quality_string not in self._acceptable_quality_strings:
            message = "can not initialize chord quality: {!r}."
            message = message.format(quality_string)
            raise ValueError(message)
        self._quality_string = quality_string

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        """
        Is true when ``argument`` is a chord quality with quality string
        equal to that of this chord quality.

        ..  container:: example

            >>> quality_1 = abjadext.tonality.ChordQuality('major')
            >>> quality_2 = abjadext.tonality.ChordQuality('major')
            >>> quality_3 = abjadext.tonality.ChordQuality('dominant')

            >>> quality_1 == quality_1
            True
            >>> quality_1 == quality_2
            True
            >>> quality_1 == quality_3
            False

            >>> quality_2 == quality_1
            True
            >>> quality_2 == quality_2
            True
            >>> quality_2 == quality_3
            False

            >>> quality_3 == quality_1
            False
            >>> quality_3 == quality_2
            False
            >>> quality_3 == quality_3
            True

        Returns true or false.
        """
        return abjad.StorageFormatManager.compare_objects(self, argument)

    def __hash__(self):
        """
        Hashes chord quality.

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
        Gets string representation of chord quality.

        ..  container:: example

            >>> quality = abjadext.tonality.ChordQuality('major')
            >>> str(quality)
            'major'

        Returns string.
        """
        return self.quality_string

    ### PRIVATE METHODS ###

    def _get_format_specification(self):
        values = [self.quality_string]
        return abjad.FormatSpecification(
            client=self,
            repr_is_indented=False,
            storage_format_is_indented=False,
            storage_format_args_values=values,
        )

    ### PUBLIC PROPERTIES ###

    @property
    def is_uppercase(self):
        """
        Is true when chord quality is uppercase.

        ..  container:: example

            >>> abjadext.tonality.ChordQuality('major').is_uppercase
            True

            >>> abjadext.tonality.ChordQuality('minor').is_uppercase
            False

        Returns true or false.
        """
        return self.quality_string in self._uppercase_quality_strings

    @property
    def quality_string(self):
        """
        Gets quality string.

        ..  container:: example

            >>> abjadext.tonality.ChordQuality('major').quality_string
            'major'

            >>> abjadext.tonality.ChordQuality('minor').quality_string
            'minor'

        Returns string.
        """
        return self._quality_string
