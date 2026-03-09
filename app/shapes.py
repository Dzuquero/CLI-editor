
import uuid
from dataclasses import dataclass, asdict

@dataclass
class Shape:
    id: str
    def to_dict(self):
        return asdict(self)

@dataclass
class Point(Shape):
    x: float
    y: float
    type: str = "point"

@dataclass
class Segment(Shape):
    x1: float
    y1: float
    x2: float
    y2: float
    type: str = "segment"

@dataclass
class Circle(Shape):
    x: float
    y: float
    r: float
    type: str = "circle"

@dataclass
class Square(Shape):
    x: float
    y: float
    side: float
    type: str = "square"
