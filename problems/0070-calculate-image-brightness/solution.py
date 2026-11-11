
def calculate_brightness(img):
    
    if not img:
        return -1

    expected = len(img)
    total_sum = 0
    total_pixel = 0

    for row in img:
        if len(row) != expected:
            return -1
        
        for num in row:
            if num < 0 or num > 255:
                return -1
            
            total_sum += num
            total_pixel += 1
        
    return total_sum / total_pixel



