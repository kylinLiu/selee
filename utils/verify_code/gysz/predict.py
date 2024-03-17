"""Usage: predict.py [-m MODEL] [-s BS] [-d DECODE] [-b BEAM] [IMAGE ...]

-h, --help    show this
-m MODEL     model file [default: ./checkpoints/crnn.pt]
-s BS       batch size [default: 256]
-d DECODE    decode method (greedy, beam_search or prefix_beam_search) [default: beam_search]
-b BEAM   beam size [default: 10]

"""
import glob
import os

from docopt import docopt
import torch
from tqdm import tqdm
from torch.utils.data import DataLoader

from utils.verify_code.gysz.config import common_config as config
from utils.verify_code.gysz.dataset import Synth90kDataset, SimpleData
from utils.verify_code.model import CRNN
from utils.verify_code.ctc_decoder import ctc_decode


def predict(crnn, dataloader, label2char, decode_method, beam_size):
    crnn.eval()
    pbar = tqdm(total=len(dataloader), desc="Predict")

    all_preds = []
    with torch.no_grad():
        for data in dataloader:
            device = 'cuda' if next(crnn.parameters()).is_cuda else 'cpu'

            images = data.to(device)

            logits = crnn(images)
            log_probs = torch.nn.functional.log_softmax(logits, dim=2)

            preds = ctc_decode(log_probs, method=decode_method, beam_size=beam_size,
                               label2char=label2char)
            all_preds += preds

            pbar.update(1)
        pbar.close()

    return all_preds


def show_result(paths, preds):
    print('\n===== result =====')
    for path, pred in zip(paths, preds):
        text = ''.join(pred)
        print(f'{path} > {text}')


def main(base64img):
    current_path = os.path.abspath(os.path.dirname(__file__))
    arguments = docopt(__doc__)

    # images_glob = './demo/*.jpg'
    # image_dir = "./demo"
    # images = glob.glob(images_glob)
    # file_names = [path[path.find("\\") + 1:] for path in images]
    reload_checkpoint = os.path.join(current_path, './checkpoints/crnn.pt')

    batch_size = int(arguments['-s'])
    decode_method = arguments['-d']
    beam_size = int(arguments['-b'])

    img_height = config['img_height']
    img_width = config['img_width']

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'device: {device}')

    # predict_dataset = Synth90kDataset(image_dir = image_dir, file_names = file_names,mode="test",
    #                                   img_height=img_height, img_width=img_width)
    predict_dataset = SimpleData(base64img=base64img,
                                 img_height=img_height, img_width=img_width)
    predict_loader = DataLoader(
        dataset=predict_dataset,
        batch_size=batch_size,
        shuffle=False)

    num_class = len(Synth90kDataset.LABEL2CHAR) + 1
    crnn = CRNN(1, img_height, img_width, num_class,
                map_to_seq_hidden=config['map_to_seq_hidden'],
                rnn_hidden=config['rnn_hidden'],
                leaky_relu=config['leaky_relu'])
    crnn.load_state_dict(torch.load(reload_checkpoint, map_location=device))
    crnn.to(device)

    preds = predict(crnn, predict_loader, Synth90kDataset.LABEL2CHAR,
                    decode_method=decode_method,
                    beam_size=beam_size)
    return ''.join(preds[0])
    # show_result(images, preds)


if __name__ == '__main__':
    main()
