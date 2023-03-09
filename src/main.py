print('welcome to Spelling Machine, installing libraries')
import sys
import tensorflow_hub as hub
import tensorflow as tf
print('waiting for the model to load')
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-large/5")
import classify
import viewer

def main():
    if len(sys.argv) == 1:
        while True:
            with open('prompt.txt', 'w') as f:
                xin = input("enter your prompt, type enter when finished, enter an empty input to start processing, and enter '!EXIT' to stop program\n")
                if xin == '!EXIT':
                    return
                if len(xin) > 0:
                    f.write(xin + "\n")
                else:
                    break
            f.close()
            classify.main(tf, embed)
            viewer.main(tf)
    else:
        with open('prompt.txt', 'w') as f:
            for i in range(1, len(sys.argv)):
                f.write(sys.argv[i] + "\n")
        f.close()
        classify.main(tf, embed)
        viewer.main(tf)

main()