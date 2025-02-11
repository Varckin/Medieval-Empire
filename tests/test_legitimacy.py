import pytest
from BaseConstants.baseConstants import LegitimacyConstants
from Government.government import Monarchy
from Stability.stability import Stability
from Legitimacy.legitimacy import Legitimacy


@pytest.fixture
def stability():
    return Stability(legitimacy=None, stabilityValue=50)


@pytest.fixture
def monarhy():
    return Monarchy(name="Relax")

@pytest.fixture
def legitimacy(monarhy, stability):
    legitimacy_instance = Legitimacy(governmentType=monarhy, stability=stability)
    stability.legitimacy = legitimacy_instance
    return legitimacy_instance

def test_init(monarhy, stability, legitimacy):
    assert legitimacy.name == "Legitimacy"
    assert legitimacy.governmentType == monarhy
    assert legitimacy.stability == stability
    assert legitimacy.legitimacyValue == 80.0
    assert legitimacy.stabilityModifier == 0
    assert legitimacy.baseCoefficient == LegitimacyConstants.baseCoefficientLegitimacy.value
    assert legitimacy.currentCoefficient == legitimacy.baseCoefficient

def test_change_legitimacy(legitimacy):

    legitimacy.changeLegitimacy(10)
    assert legitimacy.legitimacyValue == 90.0
    
    legitimacy.changeLegitimacy(-20)
    assert legitimacy.legitimacyValue == 70.0

    legitimacy.changeLegitimacy(200)
    assert legitimacy.legitimacyValue == 100.0
    
    legitimacy.changeLegitimacy(-300)
    assert legitimacy.legitimacyValue == 0.0

def test_change_every_turn_legitimacy(legitimacy):
    
    legitimacy.stability.stabilityValue = 70.0
    legitimacy.changeEveryTurnLegitimacy()
    
    assert legitimacy.legitimacyValue == 80.25

def test_stability_influence(legitimacy):

    legitimacy.stabilityInfluence()
    assert legitimacy.stabilityModifier == 0

    legitimacy.stability.stabilityValue = 40.0
    legitimacy.stabilityInfluence()
    assert legitimacy.stabilityModifier == -0.1

    legitimacy.stability.stabilityValue = 80.0
    legitimacy.stabilityInfluence()
    assert legitimacy.stabilityModifier == 0.3

def test_apply_all_modifiers(legitimacy):
    
    initial_coefficient = legitimacy.currentCoefficient
    
    legitimacy.stability.stabilityValue = 70.0
    legitimacy.applyAllModifiers()

    assert legitimacy.currentCoefficient != initial_coefficient
    assert legitimacy.currentCoefficient == legitimacy.baseCoefficient + 0.2
