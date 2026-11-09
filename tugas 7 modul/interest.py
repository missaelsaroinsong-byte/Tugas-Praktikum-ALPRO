
def compound_interest(principal, rate, years):
    return principal * (1 + rate) ** years


def simple_interest(principal, rate, years):
    return principal * (1 + rate * years)
