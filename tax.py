def calculate_ontario_income_tax(annual_income):
    """
    Calculates combined federal + Ontario provincial income tax
    based on 2024 tax brackets.
    """

    # Federal tax brackets 2024
    federal_tax = 0
    federal_brackets = [
        (57375, 0.15),
        (57375, 0.205),
        (63141, 0.26),
        (75843, 0.29),
        (float('inf'), 0.33)
    ]

    # Ontario provincial tax brackets 2024
    ontario_tax = 0
    ontario_brackets = [
        (51446, 0.0505),
        (51446, 0.0915),
        (60027, 0.1116),
        (219780, 0.1216),
        (float('inf'), 0.1316)
    ]

    def calc_tax(income, brackets):
        tax = 0
        remaining = income
        for limit, rate in brackets:
            if remaining <= 0:
                break
            taxable = min(remaining, limit)
            tax += taxable * rate
            remaining -= taxable
        return tax

    federal_tax = calc_tax(annual_income, federal_brackets)
    ontario_tax = calc_tax(annual_income, ontario_brackets)
    total_tax = federal_tax + ontario_tax

    return {
        "gross": annual_income,
        "federal_tax": round(federal_tax, 2),
        "ontario_tax": round(ontario_tax, 2),
        "total_tax": round(total_tax, 2),
        "after_tax": round(annual_income - total_tax, 2),
        "effective_rate": round((total_tax / annual_income) * 100, 2)
    }


def calculate_hst(amount):
    """Calculates Ontario HST (13%) on an expense amount."""
    hst = round(amount * 0.13, 2)
    total = round(amount + hst, 2)
    return {
        "pre_tax": amount,
        "hst": hst,
        "total": total
    }