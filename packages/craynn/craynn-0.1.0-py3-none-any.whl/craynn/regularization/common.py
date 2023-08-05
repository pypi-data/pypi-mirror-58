import tensorflow as tf

from ..parameters import glorot_scaling

__all__ = [
  'reg_l1', 'reg_l2', 'reg_elastic_net',
  'norm_preserving_l2'
]

def reg_l2():
  def reg(param):
    return tf.reduce_sum(param() ** 2)

  return reg

def reg_l1():
  def reg(param):
    return tf.reduce_sum(tf.abs(param()))

  return reg

def reg_elastic_net(alpha=0.1):
  def reg(param):
    return (1 - alpha) * reg_l2()(param) + alpha * reg_l1()(param)
  return reg


def norm_preserving_l2(scale_f=glorot_scaling):
  def reg(param):
    scale = scale_f(param.shape)
    norm = tf.sqrt(
      tf.reduce_mean(param() ** 2)
    )

    return (norm - scale) ** 2

  return reg