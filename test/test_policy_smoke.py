from impactflow import CausalDecisionModel, Lever, External, Outcome


def test_policy_outcome_and_external_name():
    lever = Lever('Investment', 2.0, [0.0, 10.0])
    uptake = External('Uptake', 3.0, [0.0, 10.0])
    benefit = Outcome('Benefit', ['Investment', 'Uptake']).fit(lambda x, y: 2*x+y)
    model = CausalDecisionModel([lever])
    model.add_elements([uptake, benefit])
    assert abs(float(model.call('Benefit')([4.0]))-11.0) < 1e-8
    assert model.external_names == ['Uptake']
