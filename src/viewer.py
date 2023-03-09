def main(tf):

    dat1 = tf.io.parse_tensor(tf.io.read_file('output.txt'), out_type=tf.float32)

    x2=0.3
    x1=0.2

    dat1 = tf.math.sigmoid((dat1-(x2+x1)/2)/(x2-x1)*1.9248+1.9248)

    dat2 = tf.io.parse_tensor(tf.io.read_file('output2.txt'), out_type=tf.float32)

    dat = tf.math.multiply(dat1, dat2)

    with open("prompt.txt", 'r') as f:
        prompt = [x[:-1] for x in f.readlines()]

    with open("spell_names.txt", 'r') as f:
        names = [x[:-1] for x in f.readlines()]

    for i in range(len(prompt)):
        comp = []
        for j in range(dat[i].numpy().size):
            comp += [(names[j], float(dat[i][j]))]
        comp.sort(key=lambda x: -x[1])
        k=0
        print("result for:",prompt[i])
        print("_____________________________________")
        while True:
            for _ in range(5):
                print(comp[k][0], ": correlation=", comp[k][1]*10)
                k+=1
            inx = input("type 'M' to see more")
            if len(inx) == 0 or (inx != 'M' and inx != 'm'):
                print("_____________________________________")
                return


