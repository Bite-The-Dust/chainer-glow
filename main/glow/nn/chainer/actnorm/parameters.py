import chainer
import chainer.links as L


class Parameters(chainer.Chain):
    def __init__(self, channels):
        super().__init__()
        with self.init_scope():
            self.scale = L.Scale(axis=1, W_shape=(channels))
            self.bias = L.Bias(axis=1, shape=(channels))
