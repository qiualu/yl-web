
from django.urls.converters import StringConverter, register_converter


class MobileConverter(StringConverter):
    regex = r"1[3-9]\d{9}"


# register_converter(路由转换类, "调用别名")
register_converter(MobileConverter, "mob")
