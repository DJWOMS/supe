import inspect
from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class BaseDTO:
    def to_dict(self) -> dict[str, Any]:
        return {k: str(v) for k, v in asdict(self).items()}

    def model_dump(self) -> dict[str, Any]:
        return self.to_dict()

    @classmethod
    def from_dict(cls, **kwargs):
        cls_fields = {field for field in inspect.signature(cls).parameters}

        native_args, new_args = {}, {}
        for name, val in kwargs.items():
            if name in cls_fields:
                native_args[name] = val
            # else:
            #     new_args[name] = val

        ret = cls(**native_args)

        # for new_name, new_val in new_args.items():
        #     setattr(ret, new_name, new_val)
        return ret



