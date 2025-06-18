# Sample AI Controller for HJK Infinity Core

def manage_energy(input_voltage, current_flow):
    energy = input_voltage * current_flow
    if energy > 100:
        return 'Lock Energy'
    return 'Store Energy'

print(manage_energy(5, 20))