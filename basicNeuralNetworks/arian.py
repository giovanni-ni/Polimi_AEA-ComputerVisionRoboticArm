def whiteOnBlack(input, output):
 
    file_in = open(input, 'r')
    file_out = open(output, 'w')

    file_out.write(file_in.readline())

    for line in file_in:
        line = line.split(',')
        #print(line)
        image = line[1:]
        image = [str(255 - int(x)) for x in image]
        file_out.write(line[0] + ',' + ','.join(image) + '\n')
    return output

input = './dataset/mnist_train.csv'
output = './dataset/mnist_train_white.csv'

output = whiteOnBlack(input, output)