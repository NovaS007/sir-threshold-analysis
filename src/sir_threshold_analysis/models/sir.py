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
            y (tuple): Current state (s, i, r).
        Returns:
            Tuple of partial derivatives (ds, di, dr) with respect to unit time t.
        """

        s, i, r = y

        ds = -self.beta * s * i / self.N
        di = self.beta * s * i / self.N - self.gamma * i
        dr = self.gamma * i

        return ds, di, dr