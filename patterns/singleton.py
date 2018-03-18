class MetaSingleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        singleton = type(instance)
        if singleton not in MetaSingleton._instances:
            MetaSingleton._instances[singleton] = {}
        instances = MetaSingleton._instances[singleton]
        if instance not in instances:
            instances[instance] = instance
        return instances[instance]
