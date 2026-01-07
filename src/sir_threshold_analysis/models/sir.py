class SIRModel:
    def __init__(self,
                 beta,
                 gamma,
                 population_size):
        self.beta = beta # beta refers to the transmission rate
        self.gamma = gamma # gamma is the recovery rate
        self.N = population_size # population size is equal to S+I+R

    def derivatives(self, t, y):
        # S is amount of the population susceptible to the epidemic
        # I is the amount of the population infected with the epidemic
        # R is the amount of the population recovered from the epidemic
        # All derivatives taken with respect to time
        S, I, R = y

        dS = -self.beta * S * I / self.N
        dI = self.beta * S * I / self.N - self.gamma * I
        dR = self.gamma * I

        return dS, dI, dR

    def euler_step(self, t, y, dt):
        dS, dI, dR = self.derivatives(t, y)

        return (
            y[0] + dt * dS,
            y[1] + dt * dI,
            y[2] + dt * dR,
        )

    def simulate(self, y0, t_end, dt):
        t = 0.0
        y = y0
        history = []

        while t <= t_end:
            history.append((t, *y))
            y = self.euler_step(t, y, dt)
            t += dt

        return history