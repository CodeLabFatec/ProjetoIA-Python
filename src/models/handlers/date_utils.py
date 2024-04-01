from datetime import datetime

class DateUtils:

    def valida_data_hora(value):
        if value == '' or value is None:
            return None
        
        if isinstance(value, str):
            value = datetime.strptime(value, '%a, %d, %b %Y %H:%M:%S %Z')

        return value.strftime('%Y-%m-%d %H:%M:%S')

    def valida_data(value):
        if value == '' or value is None:
            return None
        if isinstance(value, str):
            value = datetime.strptime(value, '%a, %d, %b %Y %H:%M:%S %Z')

        return value.strftime('%Y-%m-%d')