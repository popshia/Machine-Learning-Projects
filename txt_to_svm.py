import os


def Read_Split_And_Write(input_dir, label, rgb_output, gradient_output):
    for file in os.listdir(input_dir):
        if file.endswith('.txt'):
            with open(os.path.join(input_dir, file), 'r') as input:
                for line in input:
                    input_num = 0
                    for single_str in line.split(' '):
                        if single_str != "\n":
                            input_num += 1

                    rgb_output.write(label + " ")
                    gradient_output.write(label + " ")

                    for times in range(int(input_num / 5)):
                        rgb_output.write(str(times*5+1))
                        rgb_output.write(":")
                        rgb_output.write(line.split(' ')[times*5])
                        rgb_output.write(" ")

                        rgb_output.write(str(times*5+2))
                        rgb_output.write(":")
                        rgb_output.write(line.split(' ')[times*5+1])
                        rgb_output.write(" ")

                        rgb_output.write(str(times*5+3))
                        rgb_output.write(":")
                        rgb_output.write(line.split(' ')[times*5+2])
                        rgb_output.write(" ")

                        gradient_output.write(str(times*5+4))
                        gradient_output.write(":")
                        gradient_output.write(line.split(' ')[times*5+3])
                        gradient_output.write(" ")

                        gradient_output.write(str(times*5+5))
                        gradient_output.write(":")
                        gradient_output.write(line.split(' ')[times*5+2])
                        gradient_output.write(" ")

                    rgb_output.write("\n")
                    gradient_output.write("\n")


if __name__ == '__main__':
    parent_dir = os.path.join(os.getcwd(), 'train')
    rgb_output = open(os.path.join(parent_dir, 'rgb_scale'), 'w')
    gradient_output = open(os.path.join(parent_dir, 'gradient_scale'), 'w')

    input_dir = os.path.join(os.getcwd(), 'train', 'heart')
    Read_Split_And_Write(input_dir, '+1', rgb_output, gradient_output)
    input_dir = os.path.join(os.getcwd(), 'train', 'non-heart')
    # Read_Split_And_Write( input_dir, '-1', rgb_output, gradient_output )

    parent_dir = os.path.join(os.getcwd(), 'test')
    rgb_output = open(os.path.join(parent_dir, 'rgb_scale'), 'w')
    gradient_output = open(os.path.join(parent_dir, 'gradient_scale'), 'w')

    input_dir = os.path.join(os.getcwd(), 'test', 'heart')
    # Read_Split_And_Write( input_dir, '+1', rgb_output, gradient_output )
    input_dir = os.path.join(os.getcwd(), 'test', 'non-heart')
    # Read_Split_And_Write( input_dir, '-1', rgb_output, gradient_output )
