import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


# Makes a simple line plot of the SIR model data
def plot_sir(history: list[tuple[float, float, float, float]]) -> None:
    """
    Plot the SIR model results over time.
    Args:
        history (list): List of tuples containing (time, S, I, R) at each time step.
    """

    # Convert history to DataFrame for easier plotting
    df = pd.DataFrame(history, columns=['Time', 'Susceptible', 'Infected', 'Recovered'])

    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['Susceptible'], label='Susceptible', color='blue')
    plt.plot(df['Time'], df['Infected'], label='Infected', color='red')
    plt.plot(df['Time'], df['Recovered'], label='Recovered', color='green')

    plt.title('SIR Model Simulation')
    plt.xlabel('Time')
    plt.ylabel('Number of Individuals')
    plt.legend()
    plt.grid()
    plt.show()
    input("Press Enter to close plot...")
