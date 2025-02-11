import pytest

from BaseConstants.baseConstants import ArmyConstants
from Army.army import Army


class Legitimacy:
    def __init__(self):
        self.legitimacyValue = 80


class Stability:
    def __init__(self):
        self.stabilityValue = 50


@pytest.fixture
def army_instance():
    return Army(legitimacy=Legitimacy(), stability=Stability())

def test_army_initialization(army_instance):
    assert army_instance.name == "Army"
    assert army_instance.size == ArmyConstants.baseSize.value
    assert army_instance.currentSize == army_instance.size
    assert army_instance.attack == ArmyConstants.BaseAttacks.value
    assert army_instance.defense == ArmyConstants.baseDefense.value
    assert army_instance.level == ArmyConstants.baseLevel.value
    assert army_instance.currentLevel == army_instance.level

def test_hire_soldiers(army_instance):
    army_instance.hire(100)
    assert army_instance.currentSize == ArmyConstants.baseSize.value + 100

def test_disband_soldiers(army_instance):
    army_instance.hire(50)
    army_instance.disband(20)
    assert army_instance.currentSize == ArmyConstants.baseSize.value + 30

def test_disband_too_many_soldiers(army_instance):
    army_instance.disband(9999)
    assert army_instance.currentSize == 0

def test_experience_gain(army_instance):
    army_instance.add_Experience(10)
    assert army_instance.currentExperience == ArmyConstants.baseExperience.value + 10

def test_level_up(army_instance):
    army_instance.add_Experience(army_instance.experienceLevelList[0] + 10)
    assert army_instance.currentLevel == ArmyConstants.baseLevel.value + 1
    assert army_instance.currentExperience == 10

def test_consume_food(army_instance):
    expected_food = army_instance.currentSize * army_instance.currentFoodConsumptionPerSoldier
    assert army_instance.consume_food() == int(expected_food)

def test_consume_gold(army_instance):
    expected_gold = army_instance.currentSize * army_instance.currentGoldConsumptionPerSoldier
    assert army_instance.consume_gold() == int(expected_gold)

def test_apply_modifiers(army_instance):
    army_instance.stability.stabilityValue = 60
    army_instance.legitimacy.legitimacyValue = 100
    army_instance.applyAllModifiers()

    expected_attack = (army_instance.attack +
                       army_instance.bonusAttackFromLevel +
                       round((60 - 50) / 60, 2) +
                       round((100 - 80) / 120, 2))

    expected_defense = (army_instance.defense +
                        army_instance.bonusDefenseFromLevel +
                        round((60 - 50) / 80, 2) +
                        round((100 - 80) / 135, 2))

    assert army_instance.currentAttack == expected_attack
    assert army_instance.currentDefense == expected_defense

def test_train(army_instance):
    prev_experience = army_instance.currentExperience
    army_instance.train()
    assert army_instance.currentExperience == prev_experience + army_instance.currentExperienceGain
