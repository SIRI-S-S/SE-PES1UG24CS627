
import pytest
from gym_membership import membership_cost, can_enter, bmi_category


# 1. MEMBERSHIP COST TESTS

def test_membership_plans():
    assert membership_cost("monthly", 30, False, False) == 1500
    assert membership_cost("quarterly", 30, False, False) == 4000
    assert membership_cost("yearly", 30, False, False) == 12000


def test_invalid_plan():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_invalid_age():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


def test_senior_citizen_discount():
    assert membership_cost("monthly", 60, False, False) == 1125


def test_student_discount():
    assert membership_cost("monthly", 25, True, False) == 1350


def test_trainer_charges():
    assert membership_cost("monthly", 30, False, True) == 3500


def test_yearly_trainer_discount():
    assert membership_cost("yearly", 30, False, True) == 13500


def test_senior_student_priority():
    assert membership_cost("monthly", 65, True, False) == 1125


# 2. GYM ENTRY TESTS

def test_inactive_membership():
    assert can_enter(10, False, False, "M") is False


def test_before_opening_time():
    assert can_enter(4, True, False, "M") is False


def test_after_closing_time():
    assert can_enter(23, True, False, "M") is False


def test_women_only_slot_female():
    assert can_enter(10, True, True, "F") is True


def test_women_only_slot_male():
    assert can_enter(10, True, True, "M") is False


def test_regular_gym_slot():
    assert can_enter(10, True, False, "M") is True


# 3. BMI CATEGORY TESTS

def test_invalid_height():
    with pytest.raises(ValueError, match="invalid height"):
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
    assert bmi_category(18.5, 1.0) == "normal"
    assert bmi_category(25, 1.0) == "overweight"
    assert bmi_category(30, 1.0) == "obese"
