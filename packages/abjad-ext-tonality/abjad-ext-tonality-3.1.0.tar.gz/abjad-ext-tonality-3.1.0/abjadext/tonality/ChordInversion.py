import abjad


class ChordInversion(object):
    """
    Chord inversion.

    ..  container:: example

        >>> abjadext.tonality.ChordInversion(1)
        ChordInversion(1)

    """

    ### CLASS VARIABLES ###

    __slots__ = ("_number",)

    _inversion_name_to_inversion_number = {
        "root": 0,
        "root position": 0,
        "first": 1,
        "second": 2,
        "third": 3,
        "fourth": 4,
    }

    _inversion_number_to_inversion_name = {
        0: "root position",
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
    }

    _seventh_chord_inversion_to_figured_bass_string = {
        0: "7",
        1: "6/5",
        2: "4/3",
        3: "4/2",
    }

    _triadic_inversion_to_figured_bass_string = {0: "", 1: "6", 2: "6/4"}

    ### INITIALIZER ###

    def __init__(self, number=0):
        argument = number
        if isinstance(argument, int):
            number = argument
        elif isinstance(argument, str):
            number = self._inversion_name_to_inversion_number[argument]
        else:
            message = "can not initialize chord inversion."
            raise ValueError(message)
        self._number = number

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        """
        Is true when ``argument`` is a chord inversion with number equal to
        that of this chord inversion.

        ..  container:: example

            >>> inversion_1 = abjadext.tonality.ChordInversion(0)
            >>> inversion_2 = abjadext.tonality.ChordInversion(0)
            >>> inversion_3 = abjadext.tonality.ChordInversion(1)

            >>> inversion_1 == inversion_1
            True
            >>> inversion_1 == inversion_2
            True
            >>> inversion_1 == inversion_3
            False

            >>> inversion_2 == inversion_1
            True
            >>> inversion_2 == inversion_2
            True
            >>> inversion_2 == inversion_3
            False

            >>> inversion_3 == inversion_1
            False
            >>> inversion_3 == inversion_2
            False
            >>> inversion_3 == inversion_3
            True

        Returns true or false.
        """
        return abjad.StorageFormatManager.compare_objects(self, argument)

    def __hash__(self):
        """
        Hashes chord inversion.

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

    ### PRIVATE METHODS ###

    def _get_format_specification(self):
        values = [self.number]
        return abjad.FormatSpecification(
            client=self,
            repr_is_indented=False,
            storage_format_is_indented=False,
            storage_format_args_values=values,
        )

    ### PUBLIC METHODS ###

    def extent_to_figured_bass_string(self, extent):
        """
        Changes `extent` to figured bass string.

        ..  container:: example

            >>> inversion = abjadext.tonality.ChordInversion(0)
            >>> inversion.extent_to_figured_bass_string(5)
            ''
            >>> inversion.extent_to_figured_bass_string(7)
            '7'

            >>> inversion = abjadext.tonality.ChordInversion(1)
            >>> inversion.extent_to_figured_bass_string(5)
            '6'
            >>> inversion.extent_to_figured_bass_string(7)
            '6/5'

            >>> inversion = abjadext.tonality.ChordInversion(2)
            >>> inversion.extent_to_figured_bass_string(5)
            '6/4'
            >>> inversion.extent_to_figured_bass_string(7)
            '4/3'

            >>> inversion = abjadext.tonality.ChordInversion(3)
            >>> inversion.extent_to_figured_bass_string(7)
            '4/2'

        Returns string.
        """
        if extent == 5:
            return self._triadic_inversion_to_figured_bass_string[self.number]
        elif extent == 7:
            return self._seventh_chord_inversion_to_figured_bass_string[self.number]
        else:
            raise NotImplementedError

    ### PUBLIC PROPERTIES ###

    @property
    def name(self):
        """
        Gets name.

        ..  container:: example

            >>> abjadext.tonality.ChordInversion(0).name
            'root position'

            >>> abjadext.tonality.ChordInversion(1).name
            'first'

            >>> abjadext.tonality.ChordInversion(2).name
            'second'

        Returns string.
        """
        return self._inversion_number_to_inversion_name[self.number]

    @property
    def number(self):
        """
        Number of chord inversion.

        ..  container:: example

            >>> abjadext.tonality.ChordInversion(0).number
            0

            >>> abjadext.tonality.ChordInversion(1).number
            1

            >>> abjadext.tonality.ChordInversion(2).number
            2

        Returns nonnegative integer.
        """
        return self._number

    @property
    def title(self):
        """
        Title of chord inversion.

        ..  container:: example

            >>> abjadext.tonality.ChordInversion(0).title
            'RootPosition'

            >>> abjadext.tonality.ChordInversion(1).title
            'FirstInversion'

            >>> abjadext.tonality.ChordInversion(2).title
            'SecondInversion'

        Returns string.
        """
        name = self._inversion_number_to_inversion_name[self.number]
        if name == "root position":
            return "RootPosition"
        return "{}Inversion".format(name.title())
