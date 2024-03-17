# common_config = {
#     'data_dir': r'./',
#     'map_to_seq_hidden': 64,
#     'rnn_hidden': 256,
#     'leaky_relu': False,
# }
from utils.verify_code.config import common_config

train_config = {
    'img_width': 200,
    'img_height': 80,
    'epochs': 10000,
    'train_batch_size': 32,
    'eval_batch_size': 512,
    'lr': 0.0005,
    'show_interval': 10,
    'valid_interval': 500,
    'save_interval': 1000,
    'cpu_workers': 4,
    'reload_checkpoint': True,
    'valid_max_iter': 100,
    'decode_method': 'greedy',
    'beam_size': 10,
    'checkpoints_dir': 'checkpoints/'
}

train_config.update(common_config)
