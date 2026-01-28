def scale_image(size, scale):
    # Unpack and convert dimensions (e.g., "1920x1080")
    width, height = map(int, size.split('x'))
    return f'{round(width*scale)}x{round(height*scale)}'
