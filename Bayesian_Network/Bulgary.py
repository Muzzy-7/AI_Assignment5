# 1. Update the import here:
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 2. Update the class name here:
model = DiscreteBayesianNetwork([
    ('Burglar', 'Alarm'),
    ('Earthquake', 'Alarm'),
    ('Alarm', 'JohnCalls'),
    ('Alarm', 'MaryCalls')
])

# Burglary is very low (0.1%)
cpd_burglar = TabularCPD(variable='Burglar', variable_card=2, 
                         values=[[0.999], [0.001]])

# Earthquake is very low (0.2%)
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, 
                            values=[[0.998], [0.002]])

# Alarm is triggered by Burglar and Earthquake
# Columns represent: [B=F & E=F], [B=F & E=T], [B=T & E=F], [B=T & E=T]
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, 
                       values=[[0.999, 0.71, 0.06, 0.05],  # P(Alarm=False)
                               [0.001, 0.29, 0.94, 0.95]], # P(Alarm=True)
                       evidence=['Burglar', 'Earthquake'], 
                       evidence_card=[2, 2])

# John calls if he hears the alarm
cpd_john = TabularCPD(variable='JohnCalls', variable_card=2, 
                      values=[[0.95, 0.10],   # P(John=F | Alarm=F, T)
                              [0.05, 0.90]],  # P(John=T | Alarm=F, T)
                      evidence=['Alarm'], evidence_card=[2])

# Mary calls if she hears the alarm
cpd_mary = TabularCPD(variable='MaryCalls', variable_card=2, 
                      values=[[0.99, 0.30],   # P(Mary=F | Alarm=F, T)
                              [0.01, 0.70]],  # P(Mary=T | Alarm=F, T)
                      evidence=['Alarm'], evidence_card=[2])

model.add_cpds(cpd_burglar, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)
assert model.check_model()

infer = VariableElimination(model)

print("Scenario: John and Mary both called.")
result = infer.query(variables=['Burglar'], evidence={'JohnCalls': 1, 'MaryCalls': 1})
print(result)