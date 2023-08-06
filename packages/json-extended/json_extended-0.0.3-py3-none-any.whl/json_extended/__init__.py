import uuid
import json as _json
import decimal
from datetime import date
from datetime import datetime
from datetime import timezone

try:
    import dataclasses
except ImportError:
    dataclasses = None

class JSONEncoder(_json.JSONEncoder):
    """The defualt JSON encoder. This on extends the default
    encoder by also supporting ``datetime``, ``UUID`` and
    ``dataclasses``.

    ``datetime`` objects are serialized as isoformatt datetime strings.
    """
    def default(self, o):
        if isinstance(o, datetime):
            if o.tzinfo is None:
                o = o.astimezone(timezone.utc)
            return o.isoformat()
        if isinstance(o, date):
            return o.isoformat()
        if isinstance(o, uuid.UUID):
            return str(o)
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0: return float(o)
            else: return int(o)
        if dataclasses and dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(self, o)

def _dump_arg_defaults(kwargs):
    """Inject default argument for dump functions."""
    kwargs.setdefault('sort_keys', False)
    kwargs.setdefault('cls', JSONEncoder)

def dumps(obj, **kwargs):
    """Serialize ``obj`` to a JSON-formatted string."""
    _dump_arg_defaults(kwargs)
    return _json.dumps(obj, **kwargs)

def dump(obj, fp, **kwargs):
    _dump_arg_defaults(kwargs)
    _json.dump(obj, fp, **kwargs)

loads = _json.loads
load  = _json.load
