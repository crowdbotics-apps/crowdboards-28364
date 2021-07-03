from django.test import TestCase

# Test all models
def TestModel(model):
    """Test all models"""
    print "Testing %s" % model.__name__
    print "=" * len(model.__name__)
    for name, obj in model.__dict__.items():
        if isinstance(obj, models.Model):
            print "Testing %s" % name
            print "-" * len(name)
            TestModel(obj)
    print
