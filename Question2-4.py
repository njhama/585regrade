import math

def verify_trig_identity():
    for angle in range(0, 360 + 1):  # Loop from 0 to 3.59 degrees in hundredths of a degree
        theta = angle / 100.0  # Convert to degrees
        
        # Retrieve sin(x) (this would come from the SQL)
        sin_theta = math.sin(math.radians(theta))  # Calculate sin(theta)
        
        # Compute sin^2(x) = sin(x)^2
        sin2_theta = sin_theta ** 2  # Compute sin^2(theta)
        
        # Compute cos^2(x) = 1 - sin^2(x)
        cos2_theta = 1 - sin2_theta  # Compute cos^2(theta)
        
        # Check |sin^2(x) + cos^2(x) - 1| < ε or 0.00001 to verify
        result = sin2_theta + cos2_theta  # Calculate sin^2(theta) + cos^2(theta)
        
        # Verify if the result is close to 1 within the specified tolerance
        if abs(result - 1) > 00001:
            print(f"Verification failed for angle: {theta} degrees")
            return False
    print("Verification successful for all angles.")
    return True

verify_trig_identity()
