"""Defining constants"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Returns the amount of time the cake has left to bake."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Returns the amount of time taken in minutes to prep each layer"""
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Returns the amount of time elapsed preparing and baking"""
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
