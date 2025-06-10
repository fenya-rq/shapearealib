class PositiveNumber:
    @staticmethod
    def validate(value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Value type should be integer or float! Passed value: {value}')
        if value <= 0:
            raise ValueError(f'Value should be greater then 0! Passed value: {value}')
        return value
