from collections import OrderedDict


class _BaseParam:

    def __init__(self, value):
        self.value = value

    def to_param_dict(self):
        return {self.param_name: self.value}


class _BaseStringArrayParam(_BaseParam):

    def to_param_dict(self):
        encoded_param = self.param_name + "[]"
        return {encoded_param: self.value}


class _BaseObjectArrayParam(_BaseParam):

    def to_param_dict(self):
        param_dict = {}
        for index, dictionary in enumerate(self.value):
            for key, value in dictionary.items():
                param_name = "{param_name}[{index}][{key}]".format(
                    param_name=self.param_name, index=index, key=key
                )
                param_dict[param_name] = value
        return OrderedDict(sorted(param_dict.items()))


class SkytableParams:

    class MaxRecordsParam(_BaseParam):
        param_name = "maxRecords"
        kwarg = "max_records"

    class ViewParam(_BaseParam):
        param_name = "view"
        kwarg = param_name

    class PageSizeParam(_BaseParam):
        param_name = "pageSize"
        kwarg = "page_size"

    class FormulaParam(_BaseParam):
        param_name = "filterByFormula"
        kwarg = "formula"

        @staticmethod
        def from_name_and_value(field_name, field_value):
            """
            Create a formula to match cells from from field_name and value
            """
            if isinstance(field_value, dict):
                return field_value

            if isinstance(field_value, str):
                field_value = "'{}'".format(field_value)

            formula = "{{{name}}}={value}".format(name=field_name, value=field_value)
            return formula

    class _OffsetParam(_BaseParam):
        param_name = "offset"
        kwarg = param_name

    class FieldsParam(_BaseStringArrayParam):
        param_name = "fields"
        kwarg = param_name

    class SortParam(_BaseObjectArrayParam):

        param_name = "sort"
        kwarg = param_name

        def __init__(self, value):
            if hasattr(value, "startswith"):
                value = [value]

            self.value = []
            direction = "asc"

            for item in value:
                if not hasattr(item, "startswith"):
                    field_name, direction = item
                else:
                    if item.startswith("-"):
                        direction = "desc"
                        field_name = item[1:]
                    else:
                        field_name = item

                sort_param = {"field": field_name, "direction": direction}
                self.value.append(sort_param)

    @classmethod
    def _discover_params(cls):
        try:
            return cls.filters
        except AttributeError:
            filters = {}
            for param_class_name in dir(cls):
                param_class = getattr(cls, param_class_name)
                if hasattr(param_class, "kwarg"):
                    filters[param_class.kwarg] = param_class
                    filters[param_class.param_name] = param_class
            cls.filters = filters
        return cls.filters

    @classmethod
    def _get(cls, kwarg_name):
        param_classes = cls._discover_params()
        try:
            param_class = param_classes[kwarg_name]
        except KeyError:
            raise ValueError("invalid param keyword {}".format(kwarg_name))
        else:
            return param_class
