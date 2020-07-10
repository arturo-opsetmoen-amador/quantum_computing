import cirq as c

# Create a qubit

qubit = c.GridQubit(0, 0)

# Create a quantum circuit

q_circuit = c.Circuit(
    c.X(qubit)**0.5, # Square root of the NOT gate.
    c.measure(qubit, key='m') # Define it as a measurement.
)

print("Circuit:")
print(q_circuit)

# Run a simulation of the circuit n-times
n_times = 2000
simulator = c.Simulator()
result = simulator.run(q_circuit, repetitions = n_times)
print("Results:")
print(result)


