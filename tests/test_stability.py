import pytest
from Stability.stability import Stability
from BaseConstants.baseConstants import StabilityConstants

class Legitimacy:
    def __init__(self, legitimacyValue):
        self.legitimacyValue = legitimacyValue

@pytest.fixture
def stability_instance():
    return Stability(legitimacy=Legitimacy(60))

def test_init(stability_instance):
    assert stability_instance.stabilityValue == 50.0
    assert stability_instance.baseStability == StabilityConstants.baseStability.value
    assert stability_instance.baseStabilizationCoefficient == StabilityConstants.baseStabilizationCoefficient.value
    assert stability_instance.currentStabilizationCoefficient == stability_instance.baseStabilizationCoefficient

@pytest.mark.parametrize("legitimacy_value, expected_modifier", [
    (80, 0.2),
    (60, 0.0),
    (40, -0.2),
    (100, 0.4),
    (20, -0.4),
])
def test_legitimacy_modifier(legitimacy_value, expected_modifier):
    stability = Stability(Legitimacy(legitimacy_value))
    stability.legitimacyInfluence()
    assert stability.legitimacyModifier == expected_modifier


def test_change_stability(stability_instance):
    stability_instance.changeStability(10)
    assert stability_instance.stabilityValue == 60.0

    stability_instance.changeStability(-20)
    assert stability_instance.stabilityValue == 40.0

def test_stability_bounds(stability_instance):
    stability_instance.changeStability(500)
    assert stability_instance.stabilityValue == 100.0

    stability_instance.changeStability(-200)
    assert stability_instance.stabilityValue == 0.0

def test_stabilization_process():
    stability = Stability(Legitimacy(60), 80)
    stability.stabilizationOfStability()
    assert stability.stabilityValue < 80

    stability = Stability(Legitimacy(60), 30)
    stability.stabilizationOfStability()
    assert stability.stabilityValue > 30

def test_apply_all_modifier():
    stability_high = Stability(Legitimacy(80), 80)
    stability_high.applyAllModifiers()
    assert stability_high.currentStabilizationCoefficient > stability_high.baseStabilizationCoefficient

    stability_low = Stability(Legitimacy(30), 30)
    stability_low.applyAllModifiers()
    assert stability_low.currentStabilizationCoefficient < stability_low.baseStabilizationCoefficient
