#!/usr/bin/env python
"""Simple test with logging"""
import sys
import logging
sys.path.insert(0, '../area_under_curve/')
import area_under_curve as auc


logger = logging.getLogger()

logger.setLevel(10)

def main():
    """Simple demo"""
    logging.info("Try out some sample polynomials, bounds, step sizes, and algorithms.")
    trapezoid = auc.get_algorithm("trapezoid")
    midpoint = auc.get_algorithm("midpoint")
    simpson = auc.get_algorithm("simpson")
    bounds_simple_1 = auc.Bounds(0, 10, .1)
    bounds_simple_2 = auc.Bounds(0, 10, 1)
    bounds_symmetric_1 = auc.Bounds(-5, 5, .1)
    polynomial_simple_cubic = auc.Polynomial({3:1})
    polynomial_simple_fractional = auc.Polynomial({.5:1})

    logger.info("-Demo 1")
    logger.info(f"Area={auc.area_under_curve(polynomial_simple_cubic, bounds_simple_1, midpoint)}")

    logger.info("\n-Demo 2 -- larger step size, lower accuracy")
    logger.info(f"Area={auc.area_under_curve(polynomial_simple_cubic, bounds_simple_2, midpoint)}")

    logger.info("\n-Demo 3 -- symmetric bounds and a symmetric function (net area close to zero)")
    logger.info(f"Area={auc.area_under_curve(polynomial_simple_cubic, bounds_symmetric_1, simpson)}")

    logger.info("\n-Demo 4 -- fractional exponents")
    # integral of f(x)=x^.5 is (x^1.5)1.5 + sc, or (10*sqrt(10))/1.5 with these bounds
    logger.info(f"Area={auc.area_under_curve(polynomial_simple_fractional, bounds_simple_1, trapezoid)}")


if __name__ == "__main__":
    main()
