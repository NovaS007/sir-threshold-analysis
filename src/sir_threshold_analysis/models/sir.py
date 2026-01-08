from typing import Tuple


class SIRModel:
    """
    SIR epidemiological model class.
    Attributes:
        beta (float): Transmission rate.
        gamma (float): Recovery rate.
        N (int): Total population size.
    Methods:
        derivatives(t, y): Compute the derivatives for the SIR model.
        euler_step(t, y, dt): Perform a single Euler integration step.
        simulate(y0, t_end, dt): Simulate the SIR model over time.
    """

    def __init__(self,
                 beta: float,
                 gamma: float,
                 population_size: int):
        """
        Initialize the SIR model with parameters.
        Args:
            beta (float): Transmission rate.
            gamma (float): Recovery rate.
            population_size (int): Total population size.
        """
        self.beta = beta
        # transmission rate (beta) = contact_rate * transmission_probability
        # transmission probability = R0 / (contact_rate * infectious_period)
        self.gamma = gamma
        # recovery rate = 1 / infectious period
        self.N = population_size
        # N = S + I + R

    # Compute the derivatives for the SIR model
    def derivatives(self,
                    _t: float,
                    y: Tuple[float, float, float]) -> Tuple[float, float, float]:
        """
        Compute the derivatives for the SIR model.
        Args:
            _t (float): Unused variable but included for compatibility.
            y (tuple): Current state (S, I, R).
        Returns:
            Tuple of derivatives (dS, dI, dR) with respect to unit time t.
        """

        S, I, R = y

        dS = -self.beta * S * I / self.N
        dI = self.beta * S * I / self.N - self.gamma * I
        dR = self.gamma * I

        return dS, dI, dR

    # Simple Euler method for numerical integration
    def euler_step(self,
                   t: float,
                   y: Tuple[float, float, float],
                   dt: float) -> Tuple[float, float, float]:
        """
        Perform a single Euler integration step.
        Args:
            t (float): Current time.
            y (tuple): Current state (S, I, R).
            dt (float): Time step.
        Returns:
            Tuple of updated state (S, I, R) after time step dt.
        """

        dS, dI, dR = self.derivatives(t, y)

        return (
            y[0] + dt * dS,
            y[1] + dt * dI,
            y[2] + dt * dR,
        )

    def simulate(self,
                 y0: Tuple[float, float, float],
                 t_end: float,
                 dt: float) -> list[Tuple[float, float, float, float]]:
        """
        Simulate the SIR model over time.
        Args:
            y0 (tuple): Initial state (S0, I0, R0).
            t_end (float): End time for the simulation.
            dt (float): Time step for the simulation.
        Returns:
            List of tuples containing (time, S, I, R) at each time step.
        """

        t = 0.0
        y = y0
        history = []

        while t <= t_end:
            history.append((t, *y))
            y = self.euler_step(t, y, dt)
            t += dt

        return history