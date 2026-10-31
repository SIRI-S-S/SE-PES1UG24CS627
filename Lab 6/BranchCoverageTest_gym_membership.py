import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# MEMBERSHIP COST - BRANCH TESTS

def test_invalid_plan():
    with pytest.raises(ValueError):
        membership_cost("weekly", 25, False, False)


def test_invalid_age():
    with pytest.raises(ValueError):
        membership_cost("monthly", 13, False, False)


def test_age_boundary():
    assert membership_cost("monthly", 14, False, False) == 1500


def test_senior_discount():
    assert membership_cost("monthly", 60, False, False) == 1125


def test_student_discount():
    assert membership_cost("monthly", 25, True, False) == 1350


def test_regular_customer():
    assert membership_cost("monthly", 25, False, False) == 1500


def test_trainer_non_yearly():
    assert membership_cost("monthly", 25, False, True) == 3500


def test_trainer_yearly():
    assert membership_cost("yearly", 25, False, True) == 13500


# GYM ENTRY - BRANCH TESTS

def test_inactive_membership():
    assert can_enter(10, False, False, "M") is False


def test_before_opening():
    assert can_enter(4, True, False, "M") is False


def test_opening_boundary():
    assert can_enter(5, True, False, "M") is True


def test_closing_boundary():
    assert can_enter(22, True, False, "M") is True


def test_after_closing():
    assert can_enter(23, True, False, "M") is False


def test_women_slot_female():
    assert can_enter(10, True, True, "F") is True


def test_women_slot_male():
    assert can_enter(10, True, True, "M") is False


def test_regular_slot():
    assert can_enter(10, True, False, "M") is True


# BMI - BRANCH TESTS

def test_invalid_height():
    with pytest.raises(ValueError):
        bmi_category(60, 0)


def test_underweight():
    assert bmi_category(45, 1.70) == "underweight"


def test_normal_weight():
    assert bmi_category(65, 1.70) == "normal"


def test_overweight():
    assert bmi_category(80, 1.70) == "overweight"


def test_obese():
    assert bmi_category(100, 1.70) == "obese"


def test_bmi_boundaries():
    assert bmi_category(18.5, 1) == "normal"
    assert bmi_category(25, 1) == "overweight"
    assert bmi_category(30, 1) == "obese"
