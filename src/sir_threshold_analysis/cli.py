# this file serves as the UI for the project for now

from sir_threshold_analysis.models.sir import SIRModel
def main():
    print("SIR Threshold Analysis")
    print("=" * 100)
    beta = float(input("Please chose some value for beta: "))
    gamma = float(input("Please chose some value for gama: "))
    susceptible = float(input("Please chose some initial value for susceptible: "))
    infectious = float(input("Please chose some initial value for infectious: "))
    recovered = float(input("Please chose some initial value for recovered: "))
    population = susceptible + infectious + recovered
    sir_model = SIRModel(beta, gamma, population)

    history = sir_model.simulate(
        y0=(susceptible, infectious, recovered),
        t_end=160,
        dt=0.1
    )

    # temporary sanity check
    print(history)

if __name__ == "__main__":
    main()
