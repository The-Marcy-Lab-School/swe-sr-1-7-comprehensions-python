DISCOUNTS = {"member": 10, "staff": 25}


def discount_for(kind):
    return DISCOUNTS.get(kind)


def apply_discount(total, percent_off):
    return total - (total * percent_off / 100)


def checkout(total, customer_kind):
    percent = discount_for(customer_kind)
    return apply_discount(total, percent)
