#!/usr/bin/env python
"""Find approximate area under curve:  Supports simpson, trapezoid, and
midpoint algorithms,  n-degree single variable polynomials, and variable step size
"""
import ast
import getopt
import math
import sys
import logging
from dataclasses import dataclass

LOGGER = logging.getLogger()
LOGGER.setLevel(10)

USAGE = """ -p|--poly {DegreeN1:CoefficientM1, DegreeN2:CoefficientM2, ...}
-l|--lower <lower_bound> -u|--upper <upper_bound> -s|--step <step> 
-a|--algorithm <simpson | trapezoid | midpoint>
  defaults: step_size:1, lower_bound:0, upper_bound:10, algorithm:trapezoid

e.g. To evaluate the area of y=x^2 + 2x -2 from [1-50] with .1 width sums and the midpoint algorithm:
 python area_under_curve.py --poly "{2:1, 1:2, 0:-2}" --lower 1 --upper 50 --step .1 --algorithm midpoint
"""

FULL_USAGE = USAGE

class Polynomial:
    """Single variable polynomial class supporting n degrees"""
    def __init__(self, coefficient_dict):
        """ The coefficient dict keys are the term orders, and the values are the coefficients
            e.g
            f(x) = 3x^2 would be expressed as {2:3}
            f(x) = 9x^5 + 3 would be {5:9, 0:3}
        """
        self.fractional_exponents = False

        self.coefficient_dict = coefficient_dict
        if any_negative(coefficient_dict):
            raise ValueError("Only positive exponents supported")

        self.fractional_exponents = any_non_int_numbers(coefficient_dict)

    def format_term(self, degree, value):
        """string format a single term"""
        value_formatted = str(value)
        if value == 1:
            value_formatted = ""
        if value == 0:
            return None
        if degree == 0:
            return str(value)
        if degree == 1:
            return f"{value_formatted}x"
        return f"{value_formatted}x^{degree}"

    def __str__(self):
        """string format the entire polynomial"""
        terms = []
        degrees = list(self.coefficient_dict)
        degrees = sorted(degrees, reverse=True)
        for degree in degrees:
            term_formatted = (self.format_term(degree, self.coefficient_dict[degree]))
            if term_formatted:
                terms.append(term_formatted)
        if not terms:
            return "f(x)=0"
        return f"f(x)={' + '.join(terms)}"

    def evaluate(self, value):
        """Evaluate the polynomial at a given value"""
        total = 0
        for degree in self.coefficient_dict:
            coefficient = self.coefficient_dict[degree]
            if self.fractional_exponents and value < 0:
                raise ValueError("Fractional exponents not supported for negative inputs.")
            current_term = math.pow(value, degree)* coefficient
            total += current_term
        return total

class Bounds:
    """Range of values class"""
    def __init__(self, lower_bound, upper_bound, step_size):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.step_size = step_size
        if step_size <= 0:
            raise ValueError("step size must be > 0")
        if upper_bound <= lower_bound:
            raise ValueError("invalid bounds")
        self.full_range = self.float_range(lower_bound, upper_bound, step_size)

    def __str__(self):
        return f"Bounds: [{self.lower_bound} - {self.upper_bound}], step_size: {self.step_size}"

    def float_range(self, lower_bound, upper_bound, step_size):
        """Create range of floats"""
        float_list = []
        current = lower_bound
        float_list.append(current)
        # Final number should be almost equal to upper bound.
        # Adding fraction of step_size offset to account for rounding errors.
        while current + step_size < (upper_bound + (step_size * .1)):
            current += step_size
            float_list.append(current)
        return float_list

@dataclass
class Parameters:
    """Contains several groups of parameters"""
    polynomial: Polynomial
    bounds: Bounds
    algorithm: str

    @classmethod
    def factory(cls, polynomial_coefficients, #pylint: disable=too-many-arguments
                lower, upper, step, algorithm):
        """Create parameters object from polynomial, bounds, and algorithm parameters"""
        bounds = Bounds(lower, upper, step)
        polynomial = Polynomial(polynomial_coefficients)
        return cls(polynomial, bounds, algorithm)


# Misc helper functions

def is_number(string):
    """Simple check to see if string is valid number"""
    try:
        float(string)
        return True
    except ValueError as err:
        LOGGER.error(f"Error: {string} {str(err)}")
        return False

def any_non_int_numbers(collection):
    """Returns true if any numbers in the collection are not integers"""
    return any(map(lambda n: not isinstance(n, int), collection))

def any_negative(collection):
    """Returns true if any numbers in the collection are < 0"""
    return any(map(lambda n: n < 0, collection))

def has_property(name):
    """Simple function property decorator"""
    def wrap(func):
        """Wrapper function"""
        setattr(func, name, True)
        return func
    return wrap

# Argument parsing
def parse_commandline_arguments(argv): # pylint: disable=too-many-return-statements,too-many-branches
    """Parse command line arguments and return a parameters
    object with Bounds, Polynomial, and Algorithm
    """
    #defaults
    lower = 0
    upper = 10
    step_size = 1
    algorithm = "trapezoid"
    polynomial_coefficients = {}
    try:
        opts, _ = getopt.getopt(argv, "hl:u:s:a:p:",
                                ["lower=", "upper=", "step=",
                                 "algorithm=", "polynomial=", "help"])

        non_numerical_params = ["-a", "--algorithm", "-p", "--polynomial", "-h", "--help"]
        numerical_params = list(filter(lambda t: t[0] not in non_numerical_params, opts))
        if any(map(lambda n: not is_number(n[1]), numerical_params)):
            logging.error("Error in numerical arguments.")
            return None
    except getopt.GetoptError as err:
        LOGGER.error(f"Option error: {str(err)}")
        return None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            LOGGER.info(FULL_USAGE)
            sys.exit(0)
        elif opt in ("-l", "--lower"):
            lower = float(arg)
        elif opt in ("-u", "--upper"):
            upper = float(arg)
        elif opt in ("-s", "--step"):
            step_size = float(arg)
        elif opt in ("-a", "--algorithm"):
            algorithm = arg
        elif opt in ("-p", "--polynomial"):
            polynomial_coefficients = parse_polynomial_coefficients(arg)
        if step_size <= 0:
            LOGGER.error(f"step size must be > 0: {step_size}")
            return None
        if lower >= upper:
            LOGGER.error(f"invalid bounds: {lower} {upper}")
            return None
        if (lower < 0 or upper < 0) and any_non_int_numbers(polynomial_coefficients):
            LOGGER.error("Fractional exponents not supported for negative values.")
            return None
    algorithm_function = get_algorithm(algorithm)
    if not algorithm_function:
        LOGGER.error(f"Algorithm : {algorithm} not found!")
        return None
    if not polynomial_coefficients:
        LOGGER.error("Polynomial not specified or invalid")
        return None
    if any_negative(polynomial_coefficients):
        LOGGER.error("Only positive exponents supported")
        return None
    return Parameters.factory(polynomial_coefficients,
                              lower, upper, step_size, algorithm_function)


def parse_polynomial_coefficients(dict_literal):
    """Try to parse string into dictionary, return None on failure"""
    coefficient_dict = {}
    try:
        coefficient_dict = ast.literal_eval(dict_literal)
    except SyntaxError as errs:
        LOGGER.error(f"Syntax Error parsing polynomial args: {dict_literal} {str(errs)}")
    except ValueError as errv:
        logging.error(f"Value Error parsing polynomial args: {dict_literal} {str(errv)}")
        return None
    if not isinstance(coefficient_dict, dict):
        LOGGER.error(f"Malformed dictionary: {coefficient_dict}")
        return None
    return coefficient_dict

# Algorithms and utilities
@has_property("algorithm")
def midpoint(poly, lower, upper):
    """Calculate midpoint slice from two polynomial evaluations and step size"""
    value = poly.evaluate((upper+lower)/2.0)
    return (upper - lower) * value

@has_property("algorithm")
def trapezoid(poly, lower, upper):
    """Calculate trapezoid slice from two polynomial evaluations and step size"""
    lower_value = poly.evaluate(lower)
    upper_value = poly.evaluate(upper)
    return (upper - lower) * ((lower_value + upper_value)/2.0)

@has_property("algorithm")
def simpson(poly, lower, upper):
    """Calculate parabola (Simpson) slice from two polynomial evaluations and step size"""
    lower_value = poly.evaluate(lower)
    upper_value = poly.evaluate(upper)
    midpoint_value = poly.evaluate((lower+upper)/2.0)
    return ((upper - lower) / 6.0) * (lower_value + 4 * midpoint_value + upper_value)

def get_algorithm(algorithm_name):
    """Get algorithm function by name by looking up in globals with the 'algorithm' attribute set"""
    if algorithm_name in globals():
        algorithm = globals()[algorithm_name]
        if "algorithm" in dir(algorithm):
            return globals()[algorithm_name]
        # TODO Cleanup
        return None
    LOGGER.error(f"Algorithm {algorithm_name} not found or invalid!")
    return None


# High-level implementation
def area_under_curve(poly, bounds, algorithm):
    """Finds the area under a polynomial between the specified bounds
    using a rectangle-sum (of width 1) approximation.
    """
    LOGGER.info(poly)
    LOGGER.info(bounds)
    LOGGER.info(f"Algorithm: {algorithm.__name__}")
    range_upper_index = len(bounds.full_range) - 1
    total_area = 0
    for range_index, val in enumerate(bounds.full_range):
        # Can't calculate trapezoid with only lower bound value, so we're done summing.
        if range_index == range_upper_index:
            return total_area
        total_area += algorithm(poly, val, bounds.full_range[range_index + 1])
    return total_area
# Entrypoints
def area_under_curve_argv(args):
    """Command-line entrypoint"""
    parsed_parameters = parse_commandline_arguments(args[1:])
    if not parsed_parameters:
        print(FULL_USAGE)
        sys.exit(2)
    area = area_under_curve(parsed_parameters.polynomial,
                            parsed_parameters.bounds, parsed_parameters.algorithm)
    print(f"Total Area ({parsed_parameters.algorithm.__name__}) = {area}")


if __name__ == '__main__':
    FULL_USAGE = f'{__doc__}\nUsage: python {sys.argv[0]} {USAGE}'
    area_under_curve_argv(sys.argv)
