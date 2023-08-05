import tensorflow as tf

__all__ = [
  'logit_binary_crossentropy', 'logit_categorical_crossentropy', 'logit_crossentropy',
  'binary_crossentropy', 'categorical_crossentropy'
]

def logit_binary_crossentropy(target, predictions, weights=None):
  assert len(predictions.shape) == 1, 'Predictions for a binary loss must be a 1D-tensor.'
  losses = target * tf.nn.softplus(-predictions) + (1 - target) * tf.nn.softplus(predictions)

  if weights is not None:
    return tf.reduce_mean(weights * losses)
  else:
    return tf.reduce_mean(losses)

def logit_categorical_crossentropy(target, predictions, weights=None):
  assert len(predictions.shape) == 2, 'Predictions for a categorical loss must be a 1D-tensor.'
  normed_predictions = predictions - tf.reduce_max(predictions, axis=1)[:, None]
  neg_log_softmax = tf.math.reduce_logsumexp(normed_predictions, axis=1)[:, None] - normed_predictions

  losses = tf.reduce_sum(target * neg_log_softmax, axis=1)

  if weights is not None:
    return tf.reduce_mean(weights * losses)
  else:
    return tf.reduce_mean(losses)

def logit_crossentropy(target, predictions, weights=None):
  if len(target.shape) == 1:
    return logit_binary_crossentropy(target, predictions, weights)
  else:
    return logit_categorical_crossentropy(target, predictions, weights)

def binary_crossentropy(target, predictions, eps=1e-3, weights=None):
  assert len(predictions.shape) == 1, 'Predictions for binary loss must be a 1D-tensor.'

  losses = target * tf.math.log(predictions + eps) + (1 - target) * tf.math.log(1 - predictions + eps)

  if weights is not None:
    return -tf.reduce_mean(weights * losses)
  else:
    return -tf.reduce_mean(losses)

def categorical_crossentropy(target, predictions, weights=None):
  assert len(predictions.shape) == 2, 'Predictions for a categorical loss must be a 1D-tensor.'

  losses = target * tf.math.log(predictions)
  if weights is not None:
    return -tf.reduce_mean(weights * losses)
  else:
    return -tf.reduce_mean(losses)

def crossentropy(target, predictions, weights=None):
  if len(target.shape) == 1:
    return binary_crossentropy(target, predictions, weights)
  else:
    return categorical_crossentropy(target, predictions, weights)

def _concat(p_neg, p_pos, keep_priors=True):
  predictions = tf.concat([
    p_neg,
    p_pos
  ], axis=0)

  target = tf.concat([
    tf.zeros_like(p_neg),
    tf.ones_like(p_pos),
  ], axis=0)

  if not keep_priors:
    n_neg = tf.shape(p_neg)[0]
    n_pos = tf.shape(p_pos)[1]

    total = n_neg + n_pos

    w_neg = 0.5 * total / n_neg
    w_pos = 0.5 * total / n_pos

    weights = tf.concat([
      w_neg * tf.ones_like(p_neg),
      w_pos * tf.ones_like(p_pos),
    ])
  else:
    weights = None

  return target, predictions, weights

def per_class_logit_crossentropy(predictions_negative, predictions_positive, keep_priors=True):
  target, predictions, weights = _concat(predictions_negative, predictions_positive, keep_priors=keep_priors)

  return logit_binary_crossentropy(target, predictions, weights )
