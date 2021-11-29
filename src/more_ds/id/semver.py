import re
from typing import ClassVar, Pattern


class SemVer(str):
    """Semantic version numbers.

    Semantic version numbers take the form X.Y.Z
    where X, Y, and Z are non-negative integers,
    and MUST NOT contain leading zeroes.
    X is the major version,
    Y is the minor version,
    and Z is the patch version.
    Each element MUST increase numerically.
    For instance: 1.9.0 -> 1.10.0 -> 1.11.0.

    See also: https://semver.org/ (where the above "definition" was taken from)

    This class allows semantic version numbers to be prefixed with "v".
    Eg "v1.11.0".
    However,
    their canonical form,
    as outputted by the :meth:`.__str__` and :meth:`.__repr__` methods,
    will not include that prefix.

    In addition,
    the minor and patch version can be left unspecified.
    :class:`SemVer` will assume them to be equal to 0 in that case.

    This class was specifically made a subclass of :class:`str`
    to allow for seamless JSON serialization.
    """

    PAT: ClassVar[Pattern[str]] = re.compile(
        r"""
        ^v?                     # Optionally start with a 'v' (for version)
        (?P<major>\d+)          # A major version number is compulsory
        (?:\.                   # Optionally followed by a '.'
            (?P<minor>\d+)      # ... and a minor version number
            (?:\.               # Optionally followed by a '.'
                (?P<patch>\d+)  # ... and a patch version number
            )?
        )?$                     # And nothing else
        """,
        re.VERBOSE,
    )
    major: int
    minor: int
    patch: int

    def __init__(self, version: str) -> None:
        """Create a SemVer using a str that could be interpreted as an semantic version number.

        Examples:
            >>> SemVer("1.0.0")
            SemVer("1.0.0")

            >>> SemVer("v54")
            SemVer("54.0.0")

            >>> SemVer("v3.9.0")
            SemVer("3.9.0")

        Args:
            version: A semantic version number, optionally prefixed with a "v".

        Raises:
            ValueError: if the string supplied is not a semantic version number.
        """
        if m := SemVer.PAT.match(version):
            self.major = int(m.group("major"))
            if minor_match := m.group("minor"):
                self.minor = int(minor_match)
                if patch_match := m.group("patch"):
                    self.patch = int(patch_match)
                else:
                    self.patch = 0
            else:
                self.minor = self.patch = 0
        else:
            raise ValueError(f"Argument '{version}' is not a semantic version number.")

    # IMPORTANT: All the comparisons operators have been overridden as we explicitly don't want
    # to fall back to the `str` versions. After all, we want the comparisons to only take the
    # numerical `major`, `minor` and `patch` versions into account and not the `str`
    # representation that might happen to include the prefix or the `str` representation of
    # numerical values ("10" < "2"). This is also the reason we can't rely on `@total_ordering`

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, SemVer):
            return NotImplemented
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)

    def __le__(self, other: object) -> bool:
        if not isinstance(other, SemVer):
            return NotImplemented

        return (self.major, self.minor, self.patch) <= (other.major, other.minor, other.patch)

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, SemVer):
            return NotImplemented
        return (self.major, self.minor, self.patch) > (other.major, other.minor, other.patch)

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, SemVer):
            return NotImplemented

        return (self.major, self.minor, self.patch) >= (other.major, other.minor, other.patch)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SemVer):
            return False

        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __str__(self) -> str:
        """Return string representation of semantic version without a "v" prefix."""
        return f"{self.major}.{self.minor}.{self.patch}"

    def __repr__(self) -> str:
        """Return Python parseable representation of a SemVer instance."""
        return f'SemVer("{str(self)}")'

    def __hash__(self) -> int:
        return hash(str(self))
