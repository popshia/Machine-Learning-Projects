import os

def Read_Split_And_Write(input_dir, label, rgb_output, gradient_output):
    for file in sorted(list(filter(lambda x: '.txt' in x, os.listdir(input_dir)))):
        with open(os.path.join(input_dir, file), 'r') as input:
            rgb_count, gradient_count = 1, 1

            for line in input:
                feature_count = 0

                for feature_value in line.split(' '):
                    if feature_value != "\n":
                        feature_count += 1

                rgb_output.write(label + " ")
                gradient_output.write(label + " ")

                for times in range(int(feature_count / 5)):
                    rgb_output.write( str(rgb_count) + ":" + line.split( ' ' )[ times*5 ] + " " )
                    rgb_count += 1
                    rgb_output.write( str(rgb_count) + ":" + line.split( ' ' )[ times*5+1 ] + " " )
                    rgb_count += 1
                    rgb_output.write( str(rgb_count) + ":" + line.split( ' ' )[ times*5+2 ] + " " )
                    rgb_count += 1

                    gradient_output.write( str(gradient_count) + ":" + line.split( ' ' )[ times*5+3 ] + " " )
                    gradient_count += 1
                    gradient_output.write( str(gradient_count) + ":" + line.split( ' ' )[ times*5+4 ] + " " )
                    gradient_count += 1

        rgb_count, gradient_count = 1, 1
        rgb_output.write("\n")
        gradient_output.write("\n")


if __name__ == '__main__':
    parent_dir = os.path.join(os.getcwd(), 'train')
    rgb_output = open(os.path.join(parent_dir, 'rgb_scale'), 'a')
    gradient_output = open(os.path.join(parent_dir, 'gradient_scale'), 'a')

    input_dir = os.path.join(os.getcwd(), 'train', 'heart')
    Read_Split_And_Write(input_dir, '+1', rgb_output, gradient_output)
    input_dir = os.path.join(os.getcwd(), 'train', 'non-heart')
    Read_Split_And_Write( input_dir, '-1', rgb_output, gradient_output )

    parent_dir = os.path.join(os.getcwd(), 'test')
    rgb_output = open(os.path.join(parent_dir, 'rgb_scale'), 'a')
    gradient_output = open(os.path.join(parent_dir, 'gradient_scale'), 'a')

    input_dir = os.path.join(os.getcwd(), 'test', 'heart')
    Read_Split_And_Write( input_dir, '+1', rgb_output, gradient_output )
    input_dir = os.path.join(os.getcwd(), 'test', 'non-heart')
    Read_Split_And_Write( input_dir, '-1', rgb_output, gradient_output )
