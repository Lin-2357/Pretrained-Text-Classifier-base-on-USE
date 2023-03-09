with open("spells.txt", 'r') as f:
    selector = [x[:-1] for x in f.readlines()]

print("total of", len(selector), "spells")

print(selector[:2])

import tensorflow_hub as hub
import tensorflow as tf

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")
ts = embed(selector)

tf.io.write_file(
    "tensors.txt", tf.io.serialize_tensor(ts)
)

with open("spell_names.txt", 'r') as f:
    selector = [x[:-1] for x in f.readlines()]

print(selector[:2])
ts = embed(selector)
tf.io.write_file(
    "tensor_names.txt", tf.io.serialize_tensor(ts)
)

print("embedding finished")