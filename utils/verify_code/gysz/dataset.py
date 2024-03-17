import os
import base64
from io import BytesIO
from PIL import Image
import torch
from torch.utils.data import Dataset
import numpy as np



def base64_to_image(base64_str):  # 用 b.show()可以展示
    image = base64.b64decode(base64_str, altchars=None, validate=False)
    image = BytesIO(image)
    image = Image.open(image)
    return image


class Synth90kDataset(Dataset):
    # CHARS = '0123456789abcdefghijklmnopqrstuvwxyz'
    # CHARS = '0123456789+-x=？'
    CHARS = '0123456789'
    CHAR2LABEL = {char: i + 1 for i, char in enumerate(CHARS)}
    LABEL2CHAR = {label: char for char, label in CHAR2LABEL.items()}

    def __init__(self, root_dir=None, image_dir=None, mode=None, file_names=None, img_height=32, img_width=100):
        if mode == "train":
            file_names, texts = self._load_from_raw_files(root_dir, mode)
        else:

            texts = None
        self.root_dir = root_dir
        self.image_dir = image_dir
        self.file_names = file_names
        self.texts = texts
        self.img_height = img_height
        self.img_width = img_width

    def _load_from_raw_files(self, root_dir, mode):

        paths_file = None
        if mode == 'train':
            paths_file = 'picture'
        elif mode == 'test':
            paths_file = 'test'

        texts = []
        # raise Exception(paths_file)
        file_names = os.listdir(os.path.join(root_dir, paths_file))
        for line in file_names:
            print(line)
            file_name, ext = line.strip().split('.')
            # text = file_name.split('_')[-1][:].lower()
            text = file_name.split('_')[-1].lower()
            # file_names.append(file_name + "." + ext)
            texts.append(text)
        print(file_names, texts)
        return file_names, texts

    # def _load_from_raw_files(self, root_dir, mode):
    #
    #     paths_file = None
    #     if mode == 'train':
    #         paths_file = 'train.txt'
    #     elif mode == 'test':
    #         paths_file = 'test.txt'
    #
    #     file_names = []
    #     texts = []
    #     with open(os.path.join(root_dir, paths_file), 'r') as fr:
    #         for line in fr.readlines():
    #
    #             file_name, ext = line.strip().split('.')
    #             text = file_name.split('_')[-1].lower()
    #             file_names.append(file_name + "." + ext)
    #             texts.append(text)
    #     return file_names, texts

    def __len__(self):
        return len(self.file_names)

    def __getitem__(self, index):
        file_name = self.file_names[index]
        file_path = os.path.join(self.image_dir, file_name)
        image = Image.open(file_path).convert('L')  # grey-scale

        image = image.resize((self.img_width, self.img_height), resample=Image.BILINEAR)
        image = np.array(image)
        image = image.reshape((1, self.img_height, self.img_width))
        image = (image / 127.5) - 1.0

        image = torch.FloatTensor(image)
        if self.texts:
            text = self.texts[index]
            target = [self.CHAR2LABEL[c] for c in text]
            target_length = [len(target)]

            target = torch.LongTensor(target)
            target_length = torch.LongTensor(target_length)
            # 如果DataLoader不设置collate_fn,则此处返回值为迭代DataLoader时取到的值
            return image, target, target_length
        else:
            return image


class SimpleData(Synth90kDataset):

    def __init__(self, base64img, img_height=32, img_width=100):
        self.base64img = base64img
        self.img_height = img_height
        self.img_width = img_width

    def __len__(self):
        return 1

    def __getitem__(self, index):
        base64img = self.base64img
        image = base64_to_image(base64img).convert('L')  # grey-scale

        image = image.resize((self.img_width, self.img_height), resample=Image.BILINEAR)
        image = np.array(image)
        image = image.reshape((1, self.img_height, self.img_width))
        image = (image / 127.5) - 1.0

        image = torch.FloatTensor(image)
        return image


def synth90k_collate_fn(batch):
    # zip(*batch)拆包
    images, targets, target_lengths = zip(*batch)
    # stack就是向量堆叠的意思。一定是扩张一个维度，然后在扩张的维度上，把多个张量纳入仅一个张量。想象向上摞面包片，摞的操作即是stack，0轴即按块stack
    images = torch.stack(images, 0)
    # cat是指向量拼接的意思。一定不扩张维度，想象把两个长条向量cat成一个更长的向量。
    targets = torch.cat(targets, 0)
    target_lengths = torch.cat(target_lengths, 0)
    # 此处返回的数据即使train_loader每次取到的数据，迭代train_loader，每次都会取到三个值，即此处返回值。
    return images, targets, target_lengths


if __name__ == '__main__':
    from torch.utils.data import DataLoader
    from config import train_config as config

    img_width = config['img_width']
    img_height = config['img_height']
    data_dir = config['data_dir']
    train_batch_size = config['train_batch_size']
    cpu_workers = config['cpu_workers']

    train_dataset = Synth90kDataset(root_dir=data_dir, mode='train',
                                    img_height=img_height, img_width=img_width)
    train_loader = DataLoader(
        dataset=train_dataset,
        batch_size=train_batch_size,
        shuffle=True,
        num_workers=cpu_workers,
        collate_fn=synth90k_collate_fn)
