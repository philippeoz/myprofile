import enum
from enum import IntEnum as _IntEnum, Enum as _Enum


@enum.unique
class IntEnum(_IntEnum):
    """
    Classe de enum com metodo para choices, utilizado em coiche fields Django
    """

    @classmethod
    def get_value(cls, name):
        """
        Método que retorna o valor de um atributo do enum.
        """
        return getattr(cls, name).value

    @classmethod
    def choices(cls):
        """
        Metodo que retorna uma lista de tuplas (NAME, VALUE) dos itens do Enum
        :returns: lista de tuplas (NAME, VALUE)
        """
        return [(n.value, n.name.replace('_', ' ').title()) for n in cls]

    @classmethod
    def get_name(cls, value):
        dict_ufs = {
            key: _value.value for (
                key, _value
            ) in dict(cls.__members__).items()
        }
        for key, _value in dict_ufs.items():
            if _value == value:
                return key
        return None


@enum.unique
class Enum(_Enum):
    """
    Classe de enum com metodo para choices, utilizado em coiche fields Django
    """
    @classmethod
    def choices(cls):
        """
        Metodo que retorna uma lista de tuplas (NAME, VALUE) dos itens do Enum
        :returns: lista de tuplas (NAME, VALUE)
        """
        return [(n.value, n.name.replace('_', ' ').title()) for n in cls]

    @classmethod
    def get_name(cls, value):
        dict_ufs = {
            key: _value.value for (
                key, _value
            ) in dict(cls.__members__).items()
        }
        for key, _value in dict_ufs.items():
            if _value == value:
                return key
        return None