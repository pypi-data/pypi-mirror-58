import tensorflow as tf

__all__ = [
  'elbo_norm'
]

def elbo_norm(X_original, X_reconstructed, code_mean, code_std, sigma_reconstructed=1.0, beta=None, exact=False):
  """
  Return Evidence Lower Bound for normally distributed (z | X), (X | z) and z:
    P(z | X) = N(`code_mean`, `code_std`);
    P(X | z) = N(`X_reconstructed`, `sigma_reconstructed`);
    P(z) = N(0, 1).

  :param X_original: original sample
  :param X_reconstructed: a sample from P(X | z)
  :param code_mean: mean of P(z | X)
  :param code_std: variance of P(z | X)
  :param sigma_reconstructed: variance for reconstructed sample, i.e. X | z ~ N(X_original, sigma_reconstructed)
    If a scalar, `Var(X | z) = sigma_reconstructed * I`, if tensor then `Var(X | z) = diag(sigma_reconstructed)`
  :param beta: coefficient for beta-VAE
  :param exact: if true returns exact value of ELBO, otherwise returns rearranged ELBO equal to the original
    up to a multiplicative constant, possibly increasing computational stability for low `sigma_reconstructed`.

  :return: (rearranged) ELBO.
  """
  reconstruction_loss = tf.reduce_mean((X_original - X_reconstructed) ** 2)

  code_penalty = tf.reduce_mean(
   tf.reduce_sum(code_std ** 2 + code_mean ** 2 - 2 * tf.log(code_std), axis=1)
  )

  if beta is None:
    ### code_penalty above is missing 1/2 coefficient.
    beta = tf.constant(0.5, dtype='float32')
  else:
    beta = tf.constant(beta / 2, dtype='float32')

  if exact:
    if is_tensor(sigma_reconstructed):
      normalization = 1 / 2 / sigma_reconstructed ** 2
    else:
      normalization = tf.constant(1 / 2 / sigma_reconstructed ** 2, dtype='float32')

    return normalization * reconstruction_loss + beta * code_penalty
  else:
    if is_tensor(sigma_reconstructed):
      normalization = 2 * sigma_reconstructed ** 2
    else:
      normalization = tf.constant(2 * sigma_reconstructed ** 2, dtype='float32')

    return reconstruction_loss + beta * normalization * code_penalty
