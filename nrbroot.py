# Eynar Roshev

def newton_sqrt(n, guess, convergence=2):
    """Uses the Newton-Raphson method of finding the square root of n.
    guess: initial estimate.
    convergence: number of decimal places at which the approximation is
                 considered accurate.
    """
    if (n == 1):
        return n
    approximation = (guess + (n/guess))/2
    rapprox = round(approximation, convergence)
    rguess = round(guess, convergence)
    if (rapprox == rguess):
        return approximation
    else:
        return newton_sqrt(n, approximation, convergence)