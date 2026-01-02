import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.abc import x
import warnings
import platform

# Ignore unnecessary numerical warnings
warnings.filterwarnings('ignore')

# ================= Configuration Console =================

# 1. Input Formula (supports sympy syntax)
# Tip: Use capital 'I' for imaginary unit (e.g., exp(I*x)), or 'j' will be auto-replaced
formula_str = 'exp(I * x)'

# 2. [Arbitrary Axis Configuration]
# Syntax Rules:
# - "i", "1.5i" : Imaginary part * multiplier
# - "x", "-x"   : Input variable x * multiplier
# - "1", "2.5"  : Real part * multiplier
# ------------------------------------------------
x_axis_setup = '1'  # X-axis = Real part * 1 (e.g., 1 * cos(x))
y_axis_setup = 'i'  # Y-axis = Imaginary part * 1 (e.g., 1 * sin(x))
# Result should be a circle/ellipse

# 3. Define calculation range for variable x
x_start, x_end = 0, 2 * np.pi
points = 1000

# 4. Other Visual Settings
show_grid = True
keep_square_aspect = True  # Recommended: True, otherwise ellipses look like circles

# =========================================================


def set_font_style():
    """Set Matplotlib font settings (Cross-platform compatibility)"""
    sys_str = platform.system()
    if sys_str == 'Windows':
        # Fallback to SimHei if available, otherwise standard fonts apply
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial']
    elif sys_str == 'Darwin':
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Arial']
    else:
        plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False


def parse_axis_config(config_str, x_input, z_values):
    """
    Parse user input string (e.g., "2.5i", "-x", "3")
    """
    # Preprocessing: lowercase, remove spaces
    s = str(config_str).lower().strip().replace(' ', '')

    scale = 1.0
    source_type = 'real'  # Default to Real part
    label_suffix = ''
    num_str = s

    # --- 1. Identify data source type (use endswith to prevent ambiguity like 'xi') ---
    if s.endswith('i'):
        source_type = 'imag'
        num_str = s[:-1]  # Remove trailing i
        label_suffix = ' (Imag)'
    elif s.endswith('x'):
        source_type = 'input'
        num_str = s[:-1]  # Remove trailing x
        label_suffix = ' (Input x)'
    else:
        source_type = 'real'
        num_str = s
        label_suffix = ' (Real)'

    # --- 2. Identify multiplier ---
    if num_str == '' or num_str == '+':
        scale = 1.0
    elif num_str == '-':
        scale = -1.0
    else:
        try:
            scale = float(num_str)
        except ValueError:
            print(
                f"⚠️ Warning: Could not parse multiplier '{num_str}', source string: '{config_str}', defaulting to 1.0"
            )
            scale = 1.0

    # --- 3. Calculate Data ---
    data = None
    if source_type == 'real':
        data = np.real(z_values) * scale
    elif source_type == 'imag':
        data = np.imag(z_values) * scale
    elif source_type == 'input':
        data = x_input * scale

    # Generate clearer label
    label = f'Source: {source_type}\nScale: {scale}'
    return data, label, label_suffix


def run_arbitrary_plot():
    set_font_style()

    # --- A. Math Calculation ---
    print(f'🧮 Calculating: f(x) = {formula_str} ...')
    try:
        # Preprocessing: Allow user to use 'j' for imaginary unit, replace with sympy's 'I'
        # Note: Simple replacement. Might affect variables named with 'j', but usually OK for math formulas
        safe_formula = formula_str.replace('j', 'I')

        expr = sp.sympify(safe_formula)
        # Use complex to prevent numpy warnings on sqrt(-1)
        f = sp.lambdify(x, expr, modules='numpy')

        t_vals = np.linspace(x_start, x_end, points)

        # Calculate complex results
        try:
            z_vals = f(t_vals)
        except Exception:
            # Handle case where f(x) = constant
            z_vals = np.full_like(t_vals, complex(expr.evalf()))

        # Force cast to complex128 to ensure real/imag attributes are available
        z_vals = np.array(z_vals, dtype=complex)

    except Exception as e:
        print(f'❌ Formula parsing error: {e}')
        return

    # --- B. Parse Axis Config and Generate Data ---
    x_data, x_label_txt, x_suffix = parse_axis_config(x_axis_setup, t_vals, z_vals)
    y_data, y_label_txt, y_suffix = parse_axis_config(y_axis_setup, t_vals, z_vals)

    # --- C. Plotting ---
    plt.figure(figsize=(10, 6))

    # Plot main curve
    plt.plot(x_data, y_data, label=f'f(x)={formula_str}', color='purple', linewidth=2)

    # Mark start point (to observe trajectory direction)
    plt.scatter(x_data[0], y_data[0], color='red', s=50, label='Start (x=0)', zorder=5)

    # Plot reference zero lines
    plt.axhline(0, color='black', linewidth=1, alpha=0.3)
    plt.axvline(0, color='black', linewidth=1, alpha=0.3)

    # Label settings
    plt.xlabel(f'X Axis Config: {x_axis_setup}{x_suffix}', fontsize=12)
    plt.ylabel(f'Y Axis Config: {y_axis_setup}{y_suffix}', fontsize=12)
    plt.title(f'Parametric Plot: X=[{x_axis_setup}] vs Y=[{y_axis_setup}]', fontsize=14)

    if show_grid:
        plt.grid(True, linestyle=':', alpha=0.6)

    if keep_square_aspect:
        plt.axis('equal')

    plt.legend()
    plt.tight_layout()
    print('✅ Plotting complete')
    plt.show()


if __name__ == '__main__':
    run_arbitrary_plot()
