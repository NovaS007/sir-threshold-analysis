from typing import Tuple

class SEIRDModel:
    """
    SEIRD epidemiological model class.
    Attributes:
        beta (float): Transmission rate.
        sigma (float): Rate of progression from exposed to infectious.
        gamma (float): Recovery rate.
        mu (float): Mortality rate.
        N (int): Total population size.
    Methods:
        derivatives(t, y): Compute the derivatives for the SEIRD model.
    """

    def __init__(self,
                 beta: float,
                 sigma: float,
                 gamma: float,
                 mu: float,
                 population_size: int):
        """
        Initialize the SEIRD model with parameters.
        Args:
            beta (float): Transmission rate.
            sigma (float): Rate of progression from exposed to infectious.
            gamma (float): Recovery rate.
            mu (float): Mortality rate.
            population_size (int): Total population size.
        """
        self.beta = beta
        self.sigma = sigma
        self.gamma = gamma
        self.mu = mu
        self.N = population_size

    def derivatives(self,
                    _t: float,
                    y: Tuple[float, float, float, float, float]
                    ) -> Tuple[float, float, float, float, float]:
        """
        Compute the derivatives for the SEIRD model.
        Args:
            _t (float): Unused variable but included for compatibility.
            y (tuple): Current state (s, e, i, r, d).
        Returns:
            Tuple of partial derivatives (ds, de, di, dr, dd).
        """
        s, e, i, r, d = y

        ds = -self.beta * s * i / self.N
        de = self.beta * s * i / self.N - self.sigma * e
        di = self.sigma * e - self.gamma * i - self.mu * i
        dr = self.gamma * i
        dd = self.mu * i

        return ds, de, di, dr, dd