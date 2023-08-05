import tensorflow as tf

def call_masked(layer, inputs, training=None, mask=None, **kwargs):
    try:
        return layer.call_masked(inputs, training=training, mask=mask, **kwargs)
    except AttributeError:
        try:
            out = layer(inputs, training=training, mask=mask, **kwargs)
        except:
            out = layer(inputs, training=training, **kwargs)
        out_mask = compute_mask_if_possible(layer, inputs, mask=mask, **kwargs)
        if out_mask is not None:
            if type(out_mask) == tf.Tensor:
                out_mask = tf.stop_gradient(out_mask)
        return out, out_mask

def compute_mask_if_possible(layer, inputs, mask=None, **kwargs):
    if layer.supports_masking:
        out_mask = layer.compute_mask(inputs, mask, **kwargs)
    else:
        out_mask = mask
    return out_mask