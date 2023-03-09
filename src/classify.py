

def main(tf, embed):
    selector = tf.io.parse_tensor(tf.io.read_file('tensors.txt'), out_type=tf.float32)
    name_sel = tf.io.parse_tensor(tf.io.read_file('tensor_names.txt'), out_type=tf.float32)

    with open("prompt.txt", 'r') as f:
        prompt = [x[:-1] for x in f.readlines()]

    embeddings = embed(prompt)

    selector = tf.linalg.normalize(selector, axis=1)[0]
    embeddings = tf.linalg.normalize(embeddings, axis=1)[0]
    name_sel = tf.linalg.normalize(name_sel, axis=1)[0]

    scores = tf.linalg.matmul(name_sel, embeddings, transpose_b=True)

    result = []

    for i in range(len(prompt)):
        tmp = []
        for j in range(len(scores)):
            tmp += [float(scores[j][i])]
        result += [tmp]

    result = tf.constant(result)
    tf.io.write_file(
        "output.txt", tf.io.serialize_tensor(result)
    )

    result = []

    scores = tf.linalg.matmul(selector, embeddings, transpose_b=True)

    result = []

    for i in range(len(prompt)):
        tmp = []
        for j in range(len(scores)):
            tmp += [float(scores[j][i])]
        result += [tmp]

    result = tf.constant(result)
    tf.io.write_file(
        "output2.txt", tf.io.serialize_tensor(result)
    )
