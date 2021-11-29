import pytest

from more_ds.id import SemVer


def test_semver_init() -> None:
    """Test SemVer initialization (including raising ValueError's)"""
    sv = SemVer("1.2.3")
    assert sv.major == 1
    assert sv.minor == 2
    assert sv.patch == 3

    sv_no_patch = SemVer("1.2")
    assert sv_no_patch.major == 1
    assert sv_no_patch.minor == 2
    assert sv_no_patch.patch == 0  # default when not explicitly specified

    sv_no_minor = SemVer("1")
    assert sv_no_minor.major == 1
    assert sv_no_minor.minor == 0  # default when not explicitly specified
    assert sv_no_minor.patch == 0  # default when not explicitly specified

    sv_with_v_prefix = SemVer("v1.2.3")
    assert sv_with_v_prefix.major == 1
    assert sv_with_v_prefix.minor == 2
    assert sv_with_v_prefix.patch == 3

    invalid_semver_values = ("1.0.0.0", "-1.0.0", "fubar")
    for isv in invalid_semver_values:
        with pytest.raises(ValueError):
            SemVer(isv)


def test_semver_str() -> None:
    """Test SemVer str representation."""
    assert str(SemVer("1.2.3")) == "1.2.3"
    assert str(SemVer("1.2")) == "1.2.0"
    assert str(SemVer("1")) == "1.0.0"

    assert str(SemVer("v1.2.3")) == "1.2.3"
    assert str(SemVer("v1.2")) == "1.2.0"
    assert str(SemVer("v1")) == "1.0.0"


def test_semver_repr() -> None:
    """Test SemVer repr representation."""
    assert repr(SemVer("1.2.3")) == 'SemVer("1.2.3")'
    assert repr(SemVer("1.2")) == 'SemVer("1.2.0")'
    assert repr(SemVer("1")) == 'SemVer("1.0.0")'

    assert repr(SemVer("v1.2.3")) == 'SemVer("1.2.3")'
    assert repr(SemVer("v1.2")) == 'SemVer("1.2.0")'
    assert repr(SemVer("v1")) == 'SemVer("1.0.0")'


def test_semver_lt() -> None:
    assert not SemVer("v1.0.0") < SemVer("1.0.0")
    assert not SemVer("1.0.0") < SemVer("v1.0.0")
    assert SemVer("v1.0.0") < SemVer("1.0.2")
    assert SemVer("v1.0.0") < SemVer("1.2.0")


def test_semver_le() -> None:
    assert SemVer("v1.0.0") <= SemVer("1.0.0")
    assert SemVer("1.0.0") <= SemVer("v1.0.0")
    assert SemVer("v1.0.0") <= SemVer("1.0.2")
    assert SemVer("v1.0.0") <= SemVer("1.2.0")


def test_semver_gt() -> None:
    assert not SemVer("v1.0.0") > SemVer("1.0.0")
    assert not SemVer("1.0.0") > SemVer("v1.0.0")
    assert SemVer("v1.0.2") > SemVer("1.0.0")
    assert SemVer("v1.2.0") > SemVer("1.0.0")


def test_semver_ge() -> None:
    assert SemVer("v1.0.0") >= SemVer("1.0.0")
    assert SemVer("1.0.0") >= SemVer("v1.0.0")
    assert SemVer("v1.0.2") >= SemVer("1.0.0")
    assert SemVer("v1.2.0") >= SemVer("1.0.0")


def test_semver_eq() -> None:
    assert SemVer("v1.0.0") == SemVer("1.0.0")
    assert SemVer("1.0.0") == SemVer("v1.0.0")
    assert SemVer("1.0.2") != SemVer("1.0.0")
    assert SemVer("1.2.0") != SemVer("1.0.0")
