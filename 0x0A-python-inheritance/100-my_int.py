#!/usr/bin/python3
"""reverse roles
"""


class MyInt(int):
    """inherits from int

    Args:
        int (_int_): _inbuilt python object int_
    """
    def __eq__(self, other):
        """reverses the function of eq

        Args:
            other (_int_): _object to compare self to_

        Returns:
            _Bool_: _False if the two objects are equal_
        """
        return int(self) != other

    def __ne__(self, other):
        """reverses the function of ne

        Args:
            other (_int_): _object to compare self to_

        Returns:
            _Bool_: _True if the two objects are equal_
        """
        return int(self) == other
