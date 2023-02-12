class BaseClass:
    def init_attribute_from(obj: object, attrs: dict, attr_name: str, default_value: any):
        if attrs.get(attr_name) is None and not default_value is None:
            setattr(obj, attr_name, default_value)
        elif not attrs.get(attr_name) is None:
            setattr(obj, attr_name, attrs.get(attr_name))
