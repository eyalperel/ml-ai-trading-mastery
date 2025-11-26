"""
Vector class implementation - Day 1
Building linear algebra from scratch to understand ML foundations
"""
import math

class Vector:
    """A simple vector class for learning linear algebra"""
    
    def __init__(self, components):
        """
        Initialize vector with a list of numbers
        
        Args:
            components: list of numbers (int or float)
        
        Example:
            v = Vector([1, 2, 3])
        """
        
        self.components = components
    
    def __repr__(self):
        """
        String representation of vector
        Should return something like: Vector([1, 2, 3])
        """
        
        return f"Vector({self.components})"
    
    def __len__(self):
        """
        Return the dimension (size) of the vector
        
        Example:
            v = Vector([1, 2, 3])
            len(v)  # Should return 3
        """
        
        return len(self.components)
    
    def add(self, other):
        """
        Vector addition (element-wise)
        
        Args:
            other: Another Vector object
        
        Returns:
            New Vector object with the sum
        
        Example:
            v1 = Vector([1, 2])
            v2 = Vector([3, 4])
            v3 = v1.add(v2)  # Should be Vector([4, 6])
        """
        
        elements = [self.components[i] + other.components[i] for i in range(len(other))]
        return Vector(elements)
    
    def scalar_multiply(self, scalar):
        """
        Scalar multiplication
        
        Args:
            scalar: A number (int or float)
        
        Returns:
            New Vector object scaled by scalar
        
        Example:
            v = Vector([1, 2, 3])
            v2 = v.scalar_multiply(2)  # Should be Vector([2, 4, 6])
        """
        
        elements = [scalar * self.components[i] for i in range(len(self.components))]
        return Vector(elements)
    
    def dot(self, other):
        """
        Dot product (inner product)
        
        Args:
            other: Another Vector object
        
        Returns:
            A scalar (number)
        
        Example:
            v1 = Vector([1, 2, 3])
            v2 = Vector([4, 5, 6])
            v1.dot(v2)  # Should return 1*4 + 2*5 + 3*6 = 32
        """
        
        dotProduct = 0
        for i in range(len(other.components)):
            dotProduct += self.components[i]*other.components[i]
        return dotProduct
    
    def norm(self, p=2):
        """
        Calculate the p-norm of the vector

        Args:
            p: The norm type (default=2 for Euclidean)
               - p=1: Manhattan norm (sum of absolute values)
               - p=2: Euclidean norm (standard length)
               - p=float('inf'): Max norm (largest absolute value)

        Returns:
            A scalar (float) - the p-norm of the vector

        Examples:
            v = Vector([3, 4])
            v.norm()      # 5.0 (Euclidean: sqrt(3² + 4²))
            v.norm(1)     # 7.0 (Manhattan: |3| + |4|)
            v.norm(float('inf'))  # 4.0 (Max: max(|3|, |4|))
        """
        if p == float('inf'):
            # L-infinity norm: maximum absolute value
            return max(abs(x) for x in self.components)
        elif p == 1:
            # L1 norm (Manhattan): sum of absolute values
            return sum(abs(x) for x in self.components)
        elif p == 2:
            # L2 norm (Euclidean): sqrt of sum of squares
            normVal = 0
            for i in range(len(self.components)):
                normVal += self.components[i]**2
            return math.sqrt(normVal)
        else:
            # General Lp norm: (sum of |x|^p)^(1/p)
            return sum(abs(x)**p for x in self.components) ** (1/p)
     
    def angle_with(self, other):
        """
        Calculate angle between two vectors
        
        Args:
            other: Another Vector object
        
        Returns:
            Tuple of (angle_radians, angle_degrees)
        
        Example:
            v1 = Vector([1, 0])
            v2 = Vector([0, 1])
            v1.angle_with(v2)  # Should return (π/2, 90.0) - orthogonal vectors
        """
        # Hint: cos(θ) = (a·b) / (||a|| ||b||)
        # Use math.acos() to get angle from cosine
        # Convert radians to degrees: degrees = radians * 180 / math.pi
        dotVal = self.dot(other=other)
        normValThis = self.norm()
        normValOther = other.norm()
        angle_radians = math.acos(dotVal / (normValThis * normValOther))
        angle_degrees = angle_radians * 180 / math.pi
        return angle_radians, angle_degrees

    def is_orthogonal(self, other, tolerance=1e-10):
        """
        Check if two vectors are orthogonal (perpendicular)
        
        Args:
            other: Another Vector object
            tolerance: Small number for floating point comparison
        
        Returns:
            Boolean - True if orthogonal, False otherwise
        
        Example:
            v1 = Vector([1, 0])
            v2 = Vector([0, 1])
            v1.is_orthogonal(v2)  # Should return True
        """
        return abs(self.dot(other)) <= tolerance

    def projection_onto(self, other):
        """
        Project this vector onto another vector
        
        Args:
            other: Another Vector object (the vector to project onto)
        
        Returns:
            New Vector object - the projection
        
        Example:
            v1 = Vector([3, 4])
            v2 = Vector([1, 0])
            v1.projection_onto(v2)  # Should return Vector([3, 0])
        """
        dotVal = self.dot(other=other)
        normValOther = other.norm()
        return other.scalar_multiply(dotVal / other.dot(other))
        

    def __sub__(self, other):
        """
        Vector subtraction using - operator
        
        Args:
            other: Another Vector object
        
        Returns:
            New Vector object with the difference
        
        Example:
            v1 = Vector([5, 7, 9])
            v2 = Vector([1, 2, 3])
            v3 = v1 - v2  # Should be Vector([4, 5, 6])
        """
        otherFlipped = other.scalar_multiply(-1)
        return self.add(otherFlipped)


    def rms(self):
        """Root-mean-square value: norm(x) / sqrt(n)"""
        return self.norm() / math.sqrt(len(self.components))

    def distance(self, other):
        """
        Calculate the Euclidean distance to another vector.

        Trading application: Measuring similarity between market states

        Args:
            other: Another Vector object

        Returns:
            A scalar (float) - the distance between vectors

        Example:
            v1 = Vector([1, 2, 3])
            v2 = Vector([4, 6, 8])
            v1.distance(v2)  # Should return ~7.07
        """
        return (self - other).norm()
    
    def mean(self):
        """Average of elements"""
        return sum(self.components) / len(self.components)
    
    def de_mean(self):
        """
        Return de-meaned vector (subtract mean from each element).

        Trading: Returns are often de-meaned for statistical analysis

        Returns:
            New Vector object with mean = 0

        Example:
            v = Vector([1, 2, 3, 4, 5])
            v.de_mean()  # Vector([-2.0, -1.0, 0.0, 1.0, 2.0])
        """
        mean_val = self.mean()
        return Vector([x - mean_val for x in self.components])
    
    def std(self):
        """
        Standard deviation: RMS of de-meaned vector.
    
        Trading: This IS volatility for returns
        """
        return self.de_mean().rms()
    
    def standardize(self):
        """
        Return standardized vector (z-scores): (x - mean) / std
    
        Trading: Feature normalization for ML models
        """
        return self.de_mean().scalar_multiply(1 / self.std())
    
    def correlation_with(self, other):
        """
        Calculate correlation coefficient with another vector.

        Correlation measures LINEAR relationship between two variables.
        Range: [-1, 1]
        - +1: Perfect positive correlation
        -  0: No linear correlation
        - -1: Perfect negative correlation

        Formula: corr(a,b) = (a_demean · b_demean) / (||a_demean|| ||b_demean||)

        Trading application:
        - Pairs trading: Find highly correlated stocks
        - Diversification: Low correlation reduces portfolio risk
        - Factor models: Correlation between returns and factors

        Args:
            other: Another Vector object

        Returns:
            float: Correlation coefficient in [-1, 1]

        Example:
            >>> returns_spy = Vector([0.01, -0.02, 0.03, -0.01])
            >>> returns_qqq = Vector([0.02, -0.03, 0.04, -0.01])
            >>> returns_spy.correlation_with(returns_qqq)
            0.9987  # Highly correlated!
        """
        # De-mean both vectors (center them at zero)
        a_demean = self.de_mean()
        b_demean = other.de_mean()

        # Calculate dot product of de-meaned vectors
        numerator = a_demean.dot(b_demean)

        # Calculate norms of de-meaned vectors
        denominator = a_demean.norm() * b_demean.norm()

        # Handle edge case: if either vector has zero variance (std = 0)
        if denominator == 0:
            return 0.0  # Undefined correlation, return 0

        return numerator / denominator
        











# Test your implementation
if __name__ == "__main__":
    print("="*60)
    print("VECTOR CLASS - COMPREHENSIVE TESTS")
    print("="*60)

    # Test 1: Creation and representation
    print("\n[Test 1] __init__ and __repr__")
    print("-" * 40)
    v1 = Vector([1, 2, 3])
    print(f"Vector created: {v1}")
    print(f"Expected: Vector([1, 2, 3])")

    # Test 2: Length/Dimension
    print("\n[Test 2] __len__ (dimension)")
    print("-" * 40)
    print(f"Dimension of {v1}: {len(v1)}")
    print(f"Expected: 3")

    # Test 3: Vector addition
    print("\n[Test 3] add()")
    print("-" * 40)
    v2 = Vector([4, 5, 6])
    v3 = v1.add(v2)
    print(f"{v1} + {v2} = {v3}")
    print(f"Expected: Vector([5, 7, 9])")

    # Test 4: Scalar multiplication
    print("\n[Test 4] scalar_multiply()")
    print("-" * 40)
    v4 = v1.scalar_multiply(2)
    print(f"2 * {v1} = {v4}")
    print(f"Expected: Vector([2, 4, 6])")
    v5 = v1.scalar_multiply(-1)
    print(f"-1 * {v1} = {v5}")
    print(f"Expected: Vector([-1, -2, -3])")

    # Test 5: Dot product
    print("\n[Test 5] dot()")
    print("-" * 40)
    dot_result = v1.dot(v2)
    print(f"{v1} · {v2} = {dot_result}")
    print(f"Expected: 32 (calculation: 1*4 + 2*5 + 3*6 = 32)")

    # Test 6: Norm (Euclidean length)
    print("\n[Test 6] norm()")
    print("-" * 40)
    v6 = Vector([3, 4])
    print(f"||{v6}|| = {v6.norm()}")
    print(f"Expected: 5.0 (calculation: sqrt(3² + 4²) = sqrt(25) = 5)")
    v7 = Vector([1, 2, 3])
    print(f"||{v7}|| = {v7.norm():.4f}")
    print(f"Expected: {(1**2 + 2**2 + 3**2)**0.5:.4f}")

    # Test 7: Angle between vectors
    print("\n[Test 7] angle_with()")
    print("-" * 40)
    v8 = Vector([1, 0])
    v9 = Vector([0, 1])
    angle_rad, angle_deg = v8.angle_with(v9)
    print(f"Angle between {v8} and {v9}:")
    print(f"  Radians: {angle_rad:.4f}")
    print(f"  Degrees: {angle_deg:.4f}")
    print(f"  Expected: 1.5708 radians (π/2), 90 degrees")

    v10 = Vector([1, 1])
    v11 = Vector([1, 0])
    angle_rad2, angle_deg2 = v10.angle_with(v11)
    print(f"Angle between {v10} and {v11}:")
    print(f"  Degrees: {angle_deg2:.4f}")
    print(f"  Expected: 45 degrees")

    # Test 8: Orthogonality
    print("\n[Test 8] is_orthogonal()")
    print("-" * 40)
    print(f"Are {v8} and {v9} orthogonal? {v8.is_orthogonal(v9)}")
    print(f"Expected: True (perpendicular vectors)")

    v12 = Vector([1, 1])
    v13 = Vector([1, -1])
    print(f"Are {v12} and {v13} orthogonal? {v12.is_orthogonal(v13)}")
    print(f"Expected: True (dot product = 0)")

    v14 = Vector([1, 2])
    v15 = Vector([2, 3])
    print(f"Are {v14} and {v15} orthogonal? {v14.is_orthogonal(v15)}")
    print(f"Expected: False (dot product = 8)")

    # Test 9: Projection
    print("\n[Test 9] projection_onto()")
    print("-" * 40)
    v16 = Vector([3, 4])
    v17 = Vector([1, 0])
    proj = v16.projection_onto(v17)
    print(f"Projection of {v16} onto {v17}: {proj}")
    print(f"Expected: Vector([3.0, 0.0])")

    v18 = Vector([1, 2])
    v19 = Vector([2, 1])
    proj2 = v18.projection_onto(v19)
    print(f"Projection of {v18} onto {v19}: {proj2}")
    print(f"Expected: Vector([1.6, 0.8])")

    # Test 10: Subtraction
    print("\n[Test 10] __sub__")
    print("-" * 40)
    v20 = Vector([5, 7, 9])
    v21 = Vector([1, 2, 3])
    v22 = v20 - v21
    print(f"{v20} - {v21} = {v22}")
    print(f"Expected: Vector([4, 5, 6])")

    # Test 11: RMS (Root Mean Square)
    print("\n[Test 11] rms()")
    print("-" * 40)
    v23 = Vector([1, 2, 3, 4])
    rms_val = v23.rms()
    print(f"RMS of {v23}: {rms_val:.4f}")
    expected_rms = math.sqrt((1**2 + 2**2 + 3**2 + 4**2) / 4)
    print(f"Expected: {expected_rms:.4f} (calculation: sqrt((1²+2²+3²+4²)/4))")

    # Test 12: Distance
    print("\n[Test 12] distance()")
    print("-" * 40)
    v24 = Vector([1, 2, 3])
    v25 = Vector([4, 6, 8])
    dist = v24.distance(v25)
    print(f"Distance from {v24} to {v25}: {dist:.4f}")
    expected_dist = math.sqrt((4-1)**2 + (6-2)**2 + (8-3)**2)
    print(f"Expected: {expected_dist:.4f} (calculation: ||[3, 4, 5]|| = sqrt(50))")

    # Test 13: Mean
    print("\n[Test 13] mean()")
    print("-" * 40)
    v26 = Vector([1, 2, 3, 4, 5])
    mean_val = v26.mean()
    print(f"Mean of {v26}: {mean_val}")
    print(f"Expected: 3.0 (calculation: (1+2+3+4+5)/5 = 15/5)")

    # Test 14: De-mean (Centering)
    print("\n[Test 14] de_mean()")
    print("-" * 40)
    v27 = Vector([1, 2, 3, 4, 5])
    v27_demeaned = v27.de_mean()
    print(f"Original: {v27}")
    print(f"De-meaned: {v27_demeaned}")
    print(f"Expected: Vector([-2.0, -1.0, 0.0, 1.0, 2.0])")
    print(f"Mean of de-meaned vector: {v27_demeaned.mean():.10f}")
    print(f"Expected: ~0.0")

    # Test 15: Standard Deviation
    print("\n[Test 15] std()")
    print("-" * 40)
    v28 = Vector([2, 4, 6, 8])
    std_val = v28.std()
    print(f"Standard deviation of {v28}: {std_val:.4f}")
    # Manual calculation: mean=5, de_mean=[-3,-1,1,3], squares=[9,1,1,9], sum=20, /4=5, sqrt=2.236
    print(f"Expected: ~2.2361 (population std)")

    # Test 16: Standardize (Z-scores)
    print("\n[Test 16] standardize()")
    print("-" * 40)
    v29 = Vector([2, 4, 6, 8])
    v29_std = v29.standardize()
    print(f"Original: {v29}")
    print(f"Standardized: {v29_std}")
    print(f"Expected: Vector([-1.3416, -0.4472, 0.4472, 1.3416]) approximately")
    print(f"Mean of standardized: {v29_std.mean():.10f}")
    print(f"Std of standardized: {v29_std.std():.10f}")
    print(f"Expected mean: ~0.0, Expected std: ~1.0")

    print("\n" + "="*60)
    print("ALL TESTS COMPLETED!")
    print("="*60)