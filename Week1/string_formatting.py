import string
def formatted_coords(ra,dec,precision=2):
    formatted_ra = f"{ra:.{precision}f}"
    formatted_dec = f"{dec:.{precision}f}"
    return f"RA: {formatted_ra}, Dec: {formatted_dec}"
