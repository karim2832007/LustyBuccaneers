# Version event: 1
# Version game: 0.1

# PYGAME
init -20 python:
    import pygame
    import time
        
    def rectangle_collide(r1, r2):
        return r1.rect.colliderect(r2.rect)

init python:
    from collections import namedtuple

    def rectangle_intersect(a, b):  
        Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')
        ra = Rectangle(a.rect.x, a.rect.y, a.rect.x + a.rect.width, a.rect.y + a.rect.height)
        rb = Rectangle(b.rect.x, b.rect.y, b.rect.x + b.rect.width, b.rect.y + b.rect.height)
        
        ra_size = float(a.rect.width * a.rect.height)
        rb_size = float(b.rect.width * b.rect.height)
        size = ( ra_size + rb_size ) / 2
        
        dx = min(ra.xmax, rb.xmax) - max(ra.xmin, rb.xmin)
        dy = min(ra.ymax, rb.ymax) - max(ra.ymin, rb.ymin)
        
        if (dx>=0) and (dy>=0):
            overlap = dx*dy
            return int((overlap / size) * 100)
        
        return 0