from .easyCalc import EasyCalculator

# list dependencies
dependencies = ['mcBasicLib']


def load(logger, core):
    # Function "load" is required by mana9er-core.
    return EasyCalculator(logger, core)
