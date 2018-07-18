import string
import random


def generate_code(size):
        final = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(final) for _ in range(size))


def code_gen(instance, size=6):
    new_code = generate_code(size)
    L = instance.__class__
    qs = L.objects.filter(shortcode=new_code).exists()
    if qs:
        return code_gen(instance=instance, size=size)    
    return new_code


def check_url(instance, URL):
    U = instance.__class__
    qs = U.objects.filter(url=URL).exists()
    if qs:
        return True
    else:
        return False
