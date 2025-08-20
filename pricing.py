def calc_price(i, h, b, m, t):
    return round(({"bike": 5, "motorbike": 15}[i] * h) * 
                 (1 - (0 if t in range(7, 11) or t in range(17, 21)
                      else (1 - (b if i == "bike" else m) / (b + m)) * 0.4)), 2)
