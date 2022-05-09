def getNumeric():
    while True:
        try:
            res = int(input())
            break
        except ValueError:
            print("Numbers only please!")
    return res


def pretty_filter(result):
    pr_ty = ''
    for r in result:
        pr_ty += f"Brand: {r[0]}, Name of product: {r[1]}, Price: {r[2]} \n"
    return pr_ty


def pretty_advanced_filter(result):
    res = result[:30]
    pr_ty = ''
    for r in res:
        pr_ty += f"Brand: {r[0]}, Name of product: {r[1]}, Classification : {r[3]}, Country: {r[4]} Price: {r[5]} \n"
    return pr_ty
