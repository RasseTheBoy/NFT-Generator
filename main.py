import numpy as np, argparse
from random     import choice, randint
from os     import listdir
from PIL    import Image, ImageDraw
from tqdm   import tqdm


# ----------------------------------------------------------------


def fprint(text):
    print(f'{text}\n')


def percentage_chance(percentage):
    if percentage > randint(0, 100):
        return True
    else:
        return False


def get_x(to_get):
    return Image.open(to_get + '\\' + choice(listdir(to_get))).convert('RGBA')


def get_rgb_value(min_val, max_val):
    rgb_values = tuple([randint(min_val, max_val) for _ in range(3)])
    return rgb_values


def save_img(img):
    output_lst = listdir('Output')
    img_nam = '0' * (3-len(str(len(output_lst)))) + str(len(output_lst)) + '.png'
    img.save('Output\\' + img_nam)


# ----------------------------------------------------------------


def generate_background():
    def get_gradient_2d(start, stop, width, height, is_horizontal):
        if is_horizontal:
            return np.tile(np.linspace(start, stop, width), (height, 1))
        else:
            return np.tile(np.linspace(start, stop, height), (width, 1)).T

    def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
        result = np.zeros((height, width, len(start_list)), dtype=float)
        for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
            result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)
        return result

    if percentage_chance(10):
        img = Image.fromarray(np.uint8(get_gradient_3d(500, 500, get_rgb_value(0, 255), get_rgb_value(0, 255), (True, False, False)))).convert('RGBA')
    else:
        img = Image.new('RGBA',(500,500), get_rgb_value(150, 255))

    return img


def generate_head():
    img = get_x('Head')
    width, height = img.size

    fill_pos = (int(0.5 * width), int(0.5 * height))
    color = (randint(100, 255), randint(100, 255), randint(100, 255), 255)

    ImageDraw.floodfill(img, xy=fill_pos, value=color)
    return img


def generate_NFT():
    final_img = generate_background()
    final_img = Image.alpha_composite(final_img, generate_head())
    if percentage_chance(30):
        final_img = Image.alpha_composite(final_img, get_x('Extra'))
    for x in ['Eyebrows', 'Eyes', 'Mouth', 'Nose', 'Hat']:
        final_img = Image.alpha_composite(final_img, get_x(x))

    return final_img


def save_gif(NFT_amnt, img_lst, all=False):
    if all:
        img_lst[0].save('GIF output\\gif_all_output.gif', format='GIF', append_images=img_lst, save_all=True, duration=250, loop=0)
        fprint('Created: gif_all_output.gif')
    else:
        file_nam = 'gif_output_' + str(len([file_nam for file_nam in listdir('GIF output')if 'all' not in file_nam])) + '.gif'
        img_lst[0].save('GIF output\\' + file_nam, format='GIF', append_images=img_lst, save_all=True, duration=250, loop=0)
        fprint(f'Created: {file_nam}')

# ----------------------------------------------------------------


def get_parser():
    parser = argparse.ArgumentParser(description='Generate some funny and wacky NFTs!')
    parser.add_argument('-a', '--amount', type=int, help='Amount of NFTs to generate', default=10)
    parser.add_argument('-g', '--gif', action=argparse.BooleanOptionalAction, help='Create .gif file of all the newly generated NFTs')
    parser.add_argument('-ga', '--gif_all', action=argparse.BooleanOptionalAction, help='Create a .gif file of all the generated NFTs')

    args = parser.parse_args()
    return args.amount, args.gif, args.gif_all


def main(NFT_amnt=10, gif_t_f=False, gif_all_t_f=False):
    pbar = tqdm(range(NFT_amnt), desc='Generating NFTs')
    img_lst = []
    for x in pbar:
        pbar.set_postfix_str(f'Generating image {x}')
        img = generate_NFT()
        save_img(img)
        img_lst.append(img)

    if gif_t_f:
        save_gif(NFT_amnt, img_lst)


    if gif_all_t_f:
        img_lst = [Image.open(f'Output\\{img_nam}') for img_nam in listdir('Output')]
        save_gif(len(img_lst), img_lst, all=True)



if __name__ == '__main__':
    amnt, gif_t_f, gif_all_t_f = get_parser()
    main(amnt, gif_t_f, gif_all_t_f)
