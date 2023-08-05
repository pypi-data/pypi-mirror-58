import tensorflow as tf

__all__ = [
  'mse', 'mae',
  'gmm_neg_log_likelihood',
]

def mse(target, predictions, weights=None):
  assert len(target.shape) == len(predictions.shape), 'target and predictions have different dimensionality'

  if weights is None:
    return tf.reduce_mean((target - predictions) ** 2)
  else:
    return tf.reduce_mean(weights * (target - predictions) ** 2)

def mae(target, predictions, weights=None):
  assert len(target.shape) == len(predictions.shape), 'target and predictions have different dimensionality'

  if weights is None:
    return tf.reduce_mean(tf.abs(target - predictions))
  else:
    return tf.reduce_mean(weights * tf.abs(target - predictions))

def gmm_neg_log_likelihood(target, means, log_sigmas, logit_priors=None):
  sigmas = tf.exp(log_sigmas)
  se = ((target[:, None] - means) / sigmas) ** 2

  if logit_priors is None:
    neg_log_likelihoods = -tf.reduce_logsumexp(
      -log_sigmas - 0.5 * se,
      axis=1
    )
  else:
    neg_log_likelihoods = -tf.reduce_logsumexp(
      -log_sigmas - 0.5 * se + tf.nn.log_softmax(logit_priors),
      axis=1
    )

  return tf.reduce_mean(neg_log_likelihoods)