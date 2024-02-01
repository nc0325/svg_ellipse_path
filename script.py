import re

def format_number(n):
    return round(n, 0 if n.is_integer() else 1)

def convert_ellipse_to_path(ellipse):
    # Extract attributes from ellipse
    cx = float(re.search(r'cx="([^"]+)"', ellipse).group(1))
    cy = float(re.search(r'cy="([^"]+)"', ellipse).group(1))
    rx = float(re.search(r'rx="([^"]+)"', ellipse).group(1))
    ry = float(re.search(r'ry="([^"]+)"', ellipse).group(1))

    # Define control points for the quadratic Bezier curve approximation of an ellipse

    kappa = ((2**0.5) * 2 - 1) / 2
    control_rx = rx * kappa
    control_ry = ry * kappa
    print(control_rx)
    print(control_ry)


    # Create the path data commands
    # M = moveto, Q = quadratic Bezier curveto, Z = close path
    d = (
        f'M{format_number(cx - rx)} {format_number(cy)} '
        f'Q{format_number(cx - control_rx)} {format_number(cy - control_ry)} {format_number(cx)} {format_number(cy - ry)} '
        f'Q{format_number(cx + control_rx)} {format_number(cy - control_ry)} {format_number(cx + rx)} {format_number(cy)} '
        f'Q{format_number(cx + control_rx)} {format_number(cy + control_ry)} {format_number(cx)} {format_number(cy + ry)} '
        f'Q{format_number(cx - control_rx)} {format_number(cy + control_ry)} {format_number(cx - rx)} {format_number(cy)} Z'
    )

    style = re.search(r'style="([^"]+)"', ellipse).group(1)
    path = f'<path d="{d}" style="{style}"/>'
    return path

# Example usage
ellipse = '<ellipse cx="100" cy="100" rx="50" ry="20" style="fill: none; stroke: red; stroke-width: 2" />'
path = convert_ellipse_to_path(ellipse)
print(path)


# Hi, What communication tools are you using? Skype or Telegram?
# I hope to work with you long term.
# These are my contact information.
# skype: live:.cid.b8144cf89d38b550
# discord: Webdev#9696
# telegram: https://t.me/webdev39
# 
# Thanks.