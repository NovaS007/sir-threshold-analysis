# this file serves as the UI for the project for now
# will be replaced with a GUI later

from __future__ import annotations
from typing import Any

import sir_threshold_analysis.models.sir as sir
import sir_threshold_analysis.models.seir as seir
import sir_threshold_analysis.models.seird as seird
import sir_threshold_analysis.visualization.plots as plots

def ask_float(prompt: str) -> float:
    while True:
        try:
            return float(input(f"{prompt} ").strip())
        except ValueError:
            print("Please enter a valid number (e.g., 0.25).")


def ask_int(prompt: str) -> int:
    while True:
        try:
            return int(input(f"{prompt} ").strip())
        except ValueError:
            print("Please enter a valid integer (e.g., 1000).")

def create_disease_model() -> object | None:
    # Menu of available models, the dictionary maps user choice to:
    # (label, constructor, list of (param_name, prompt, type))
    model_menu: dict[int, tuple[str, type, list[tuple[str, str, str]]]] = {
        1: (
            "SIR Model",
            sir.SIRModel,
            [
                ("beta", "What is your beta value? (transmission rate)", "float"),
                ("gamma", "What is your gamma value? (recovery rate)", "float"),
                ("population_size", "What is your population size? (total individuals)", "int"),
            ],
        ),
        2: (
            "SEIR Model",
            seir.SEIRModel,
            [
                ("beta", "What is your beta value? (transmission rate)", "float"),
                ("sigma", "What is your sigma value? (exposure rate)", "float"),
                ("gamma", "What is your gamma value? (recovery rate)", "float"),
                ("population_size", "What is your population size? (total individuals)", "int"),
            ],
        ),
        3: (
            "SEIRD Model",
            seird.SEIRDModel,
            [
                ("beta", "What is your beta value? (transmission rate)", "float"),
                ("sigma", "What is your sigma value? (exposure rate)", "float"),
                ("gamma", "What is your gamma value? (recovery rate)", "float"),
                ("mu", "What is your mu value? (death rate)", "float"),
                ("population_size", "What is your population size? (total individuals)", "int"),
            ],
        ),
    }

    print("What model do you want to simulate?")
    for k, (label, _, _) in model_menu.items():
        print(f"{k}: {label}")

    choice = ask_int("Enter the number of your choice:")
    if choice not in model_menu:
        print("Invalid choice. Please select a valid model.")
        return None

    # Get selected model info
    label, ctor, params = model_menu[choice]
    print(f"\nSelected: {label}\n")

    # Gather parameters
    kwargs: dict[str, Any] = {}
    for name, prompt, kind in params:
        if kind == "float":
            kwargs[name] = ask_float(prompt)
        elif kind == "int":
            kwargs[name] = ask_int(prompt)
        else:
            raise ValueError(f"Unknown param kind: {kind}")

    # Create and return the model instance
    return ctor(**kwargs)


def get_compartment_labels(disease: object) -> list[str]:
    if isinstance(disease, sir.SIRModel):
        return ["Susceptible", "Infected", "Recovered"]
    if isinstance(disease, seir.SEIRModel):
        return ["Susceptible", "Exposed", "Infected", "Recovered"]
    if isinstance(disease, seird.SEIRDModel):
        return ["Susceptible", "Exposed", "Infected", "Recovered", "Deceased"]
    raise TypeError(f"Unknown disease model type: {type(disease)}")


def ask_initial_conditions(disease: object, labels: list[str]) -> tuple[float, ...]:
    """
    Ask for initial compartment values, but compute S automatically so totals match population size.
    Defaults: I=1, others (except S) = 0.
    """
    N = int(getattr(disease, "N"))

    # Build defaults for non-S compartments
    # Assume 1 infected initially, others 0
    defaults: dict[str, int] = {lab: 0 for lab in labels}
    if "Infected" in defaults:
        defaults["Infected"] = 1

    print("\nInitial conditions:")
    print(f"Total population N = {N}")
    print("We’ll compute Susceptible automatically as: S = N - (sum of other compartments).")
    print("Press Enter to accept the default shown in brackets.\n")

    values: dict[str, float] = {}

    # Ask for everything except Susceptible
    for lab in labels:
        if lab == "Susceptible":
            continue

        while True:
            raw = input(f"{lab} [{defaults[lab]}]: ").strip()
            if raw == "":
                values[lab] = float(defaults[lab])
                break
            try:
                v = float(raw)
                if v < 0:
                    print("Please enter a value >= 0.")
                    continue
                values[lab] = v
                break
            except ValueError:
                print("Please enter a valid number or press Enter.")

    others_sum = sum(values.values())
    S0 = N - others_sum
    if S0 < 0:
        print(
            f"\nThose initial values sum to {others_sum}, which exceeds N={N}."
            " I’m going to clamp Susceptible to 0, but you probably want to re-enter."
        )
        S0 = 0.0

    # Assemble y0 in the model’s expected order
    y0_list: list[float] = []
    for lab in labels:
        if lab == "Susceptible":
            y0_list.append(float(S0))
        else:
            y0_list.append(float(values[lab]))

    print("\nUsing y0 =", tuple(y0_list))
    return tuple(y0_list)


def ask_time_settings() -> tuple[float, float]:
    print("\nSimulation settings:")
    t_end = ask_float("t_end (how long to simulate):")
    dt = ask_float("dt (time step, e.g., 0.1 or 0.01):")

    if t_end <= 0:
        print("t_end must be > 0; using t_end = 100")
        t_end = 100.0
    if dt <= 0:
        print("dt must be > 0; using dt = 0.1")
        dt = 0.1
    if dt > t_end:
        print("dt > t_end is weird; using dt = t_end/100")
        dt = t_end / 100.0

    return t_end, dt


def main() -> None:
    disease = create_disease_model()
    if disease is None:
        return

    labels = get_compartment_labels(disease)
    y0 = ask_initial_conditions(disease, labels)
    t_end, dt = ask_time_settings()

    # This assumes you have a generic function like:
    plots.plot_simulation(
        disease=disease,
        y0=y0,
        t_end=t_end,
        dt=dt,
        labels=labels,
        title=f"{disease.__class__.__name__} Simulation",
    )

if __name__ == "__main__":
    main()
