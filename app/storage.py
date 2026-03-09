
import uuid
from app.persistence import load_shapes, save_shapes

class Storage:
    def __init__(self):
        self.shapes = load_shapes()

    def list(self):
        return self.shapes

    def add(self, shape):
        shape["id"] = str(uuid.uuid4())
        self.shapes.append(shape)
        save_shapes(self.shapes)
        return shape["id"]

    def delete(self, sid):
        before=len(self.shapes)
        self.shapes=[s for s in self.shapes if s["id"]!=sid]
        save_shapes(self.shapes)
        return len(self.shapes)<before
