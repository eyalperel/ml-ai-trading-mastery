"""
Test suite for Vector class - Days 1-3
Run with: python test_vector_basics.py
"""

from vector_basics import Vector
import math

def test_basic_creation():
    """Test vector creation and representation"""
    v = Vector([1, 2, 3])
    assert len(v) == 3
    assert v.components == [1, 2, 3]
    print("✓ Basic creation")

def test_addition():
    """Test vector addition"""
    v1 = Vector([1, 2])
    v2 = Vector([3, 4])
    v3 = v1.add(v2)
    assert v3.components == [4, 6]
    print("✓ Addition")

def test_scalar_multiply():
    """Test scalar multiplication"""
    v = Vector([1, 2, 3])
    v2 = v.scalar_multiply(2)
    assert v2.components == [2, 4, 6]
    print("✓ Scalar multiplication")

def test_dot_product():
    """Test dot product"""
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    result = v1.dot(v2)
    assert result == 32  # 1*4 + 2*5 + 3*6
    print("✓ Dot product")

def test_norm():
    """Test Euclidean norm"""
    v = Vector([3, 4])
    assert abs(v.norm() - 5.0) < 1e-10
    print("✓ Norm (Euclidean)")

def test_angle():
    """Test angle calculation"""
    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    angle_rad, angle_deg = v1.angle_with(v2)
    assert abs(angle_rad - math.pi/2) < 1e-10  # 90 degrees
    print("✓ Angle")

def test_orthogonal():
    """Test orthogonality check"""
    v1 = Vector([1, 0, 0])
    v2 = Vector([0, 1, 0])
    assert v1.is_orthogonal(v2)
    print("✓ Orthogonality")

def test_projection():
    """Test projection"""
    v = Vector([3, 4])
    b = Vector([1, 0])
    proj = v.projection_onto(b)
    assert abs(proj.components[0] - 3.0) < 1e-10
    assert abs(proj.components[1] - 0.0) < 1e-10
    print("✓ Projection")

def test_subtraction():
    """Test vector subtraction"""
    v1 = Vector([5, 7])
    v2 = Vector([2, 3])
    v3 = v1.__sub__(v2)
    assert v3.components == [3, 4]
    print("✓ Subtraction")

# DAY 3 TESTS - Add these as you implement the methods

def test_norms():
    """Test different norm types"""
    v = Vector([3, 4])
    assert abs(v.norm(2) - 5.0) < 1e-10  # L2 norm
    assert abs(v.norm(1) - 7.0) < 1e-10  # L1 norm (Manhattan)
    assert abs(v.norm(float('inf')) - 4.0) < 1e-10  # L-infinity (max)
    print("✓ Multiple norms")

def test_rms():
    """Test RMS value"""
    v = Vector([1, 2, 3, 4])
    expected_rms = v.norm() / (len(v) ** 0.5)
    assert abs(v.rms() - expected_rms) < 1e-10
    print("✓ RMS value")

def test_distance():
    """Test distance calculation"""
    v1 = Vector([1, 2])
    v2 = Vector([4, 6])
    dist = v1.distance(v2)
    assert abs(dist - 5.0) < 1e-10
    # Test symmetry
    assert abs(v1.distance(v2) - v2.distance(v1)) < 1e-10
    print("✓ Distance")

def test_mean():
    """Test mean calculation"""
    v = Vector([1, 2, 3, 4, 5])
    assert abs(v.mean() - 3.0) < 1e-10
    print("✓ Mean")

def test_de_mean():
    """Test de-meaning"""
    v = Vector([1, 2, 3, 4, 5])
    demeaned = v.de_mean()
    assert abs(demeaned.mean()) < 1e-10  # Mean should be ~0
    print("✓ De-mean")

def test_std():
    """Test standard deviation"""
    v = Vector([1, 2, 3, 4, 5])
    demeaned = v.de_mean()
    std_manual = demeaned.rms()
    assert abs(v.std() - std_manual) < 1e-10
    print("✓ Standard deviation")

def test_standardize():
    """Test standardization (z-scores)"""
    v = Vector([10, 20, 30, 40, 50])
    z = v.standardize()
    assert abs(z.mean()) < 1e-10  # Mean ~0
    assert abs(z.std() - 1.0) < 1e-10  # Std ~1
    print("✓ Standardization")

def run_all_tests():
    """Run all tests"""
    print("\n" + "="*50)
    print("RUNNING VECTOR CLASS TESTS")
    print("="*50 + "\n")
    
    # Days 1-2 tests (should already pass)
    print("--- Days 1-2 Tests ---")
    test_basic_creation()
    test_addition()
    test_scalar_multiply()
    test_dot_product()
    test_norm()
    test_angle()
    test_orthogonal()
    test_projection()
    test_subtraction()
    
    # Day 3 tests (implement today)
    print("\n--- Day 3 Tests ---")
    try:
        test_norms()
        test_rms()
        test_distance()
        test_mean()
        test_de_mean()
        test_std()
        test_standardize()
    except AttributeError as e:
        print(f"⚠ Some Day 3 methods not yet implemented: {e}")
    
    print("\n" + "="*50)
    print("ALL IMPLEMENTED TESTS PASSED ✓")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_all_tests()