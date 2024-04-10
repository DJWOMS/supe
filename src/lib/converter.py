from functools import wraps
from asyncio import iscoroutinefunction
from typing import Type, Any, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from pydantic import BaseModel
    from dataclasses import dataclass

PydanticDTO = TypeVar("PydanticDTO", bound="BaseModel")
DataclassDTO = TypeVar("DataclassDTO", bound="dataclass")


class Converter:
    def __init__(self, dto: PydanticDTO | DataclassDTO | None = None):
        self.dto = dto

    # def check_dto(self, dto: PydanticDTO | DataclassDTO | None) -> bool:
    #     return isinstance(dto, BaseModel) or isinstance(dto, DataclassDTO)

    def to_list_dto_pydantic(self, instances: list[Any], dto: PydanticDTO) -> list[PydanticDTO]:
        return [self.to_dto_pydantic(instance, dto) for instance in instances]

    def to_dto_pydantic(self, instance: Any, dto: PydanticDTO) -> PydanticDTO:
        return dto.validate_model(instance)

    def to_list_dto_dataclass(self, instances: list[Any], dto: DataclassDTO) -> list[DataclassDTO]:
        return [self.to_dto_dataclass(instance, dto) for instance in instances]

    def to_dto_dataclass(self, instance: Any, dto: DataclassDTO) -> DataclassDTO:
        return dto.from_dict(**instance.to_dict())

    # def __call__(self, func):
    #     def wrapper(*args, **kwargs):
    #         print("Декоратор получил параметр:", self.dto)
    #         result = func(*args, **kwargs)
    #         if isinstance(self.dto, PydanticDTO):
    #             return self.to_list_dto_pydantic(result, self.dto)
    #         return result
    #     return wrapper

    # def to_list_model(self, instances: list[Any]) -> list[Any]:
    #     return [self.to_model(instance) for instance in instances]

    # def to_model(self, dto: Any) -> Any:
    #     return instance


class to_list_dto_dataclass(Converter):
    def __init__(self, dto: DataclassDTO):
        self.dto = dto

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)
            if result is None:
                return None
            return self.to_list_dto_dataclass(result, self.dto)
        return wrapper


class to_dto_dataclass(Converter):
    def __init__(self, dto: DataclassDTO):
        self.dto = dto

    def __call__(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)
            if result is None:
                return None
            return self.to_dto_dataclass(result, self.dto)
        return wrapper


def class_to_dto_dataclass(all_class_dto: DataclassDTO, **methods):
    """
    :param dto:
    :param methods:
    :return:

    **methods:
     method_name=DTO
    """
    def class_decorator(cls):
        def new_method(self):
            print("Class method has been decorated")
            return cls.original_method(self)

        cls.original_method = cls.class_method
        cls.class_method = new_method
        if methods:
            for method_name, dto in methods.items():
                return to_dto_dataclass(dto)(attr)
        return to_dto_dataclass(all_class_dto)(attr)
    # return class_decorator
        

        # class NewClass(cls):
        #     def __init__(self, *args, **kwargs):
        #         self._obj = super().__init__(*args, **kwargs)

        #     def __getattribute__(self, item):
        #         try:
        #             x = super().__getattribute__(item)
        #         except AttributeError:
        #             pass
        #         else:
        #             return x
        #         print("X"*1000)
        #         attr = self._obj.__getattribute__(item)
        #         print("attr" * 100)
        #         print(attr)
        #         if isinstance(attr, type(self.__init__)):
        #             if methods:
        #                 for method_name, dto in methods.items():
        #                     return to_dto_dataclass(dto)(attr)
        #             return to_dto_dataclass(all_class_dto)(attr)
        #         else:
        #             return attr
        # return NewClass
    return class_decorator
