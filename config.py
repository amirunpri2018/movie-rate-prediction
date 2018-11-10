import argparse


args_list = []
parser = argparse.ArgumentParser()


def add_arg_group(name):
    """
    :param name: argument group, str
    :return: list (argument)
    """
    arg = parser.add_argument_group(name)
    args_list.append(arg)
    return arg


def get_config():
    cfg, un_parsed = parser.parse_known_args()
    return cfg, un_parsed


# Network
network_arg = add_arg_group('Network')
network_arg.add_argument('--mode', type=str, default='non-static', choices=['static', 'non-static'])
network_arg.add_argument('--model', type=str, default='charcnn', choices=['charcnn', 'charrnn'])
network_arg.add_argument('--n_classes', type=int, default=1)
network_arg.add_argument('--use_pre_trained_embeds', type=str, default='c2v', choices=['w2v', 'd2v', 'c2v'],
                         help='using Word/Doc2Vec/Char2Vec as embedding.')
network_arg.add_argument('--n_gru_cells', type=int, default=128,
                         help='the number of CuDNNGRU cells')
network_arg.add_argument('--n_gru_layers', type=int, default=2,
                         help='the number of layers of CuDNNGRU')
network_arg.add_argument('--n_attention_size', type=int, default=128)
network_arg.add_argument('--kernel_size', type=list, default=[10, 9, 7, 5, 3],
                         help='conv1d kernel size')
# For Word2Vec, [2, 3, 4, 5] is recommended
# For Char2Vec, [10, 9, 7, 5, 3] is recommended
network_arg.add_argument('--filter_size', type=int, default=256,
                         help='conv1d filter size')
network_arg.add_argument('--fc_unit', type=int, default=1024)
network_arg.add_argument('--drop_out', type=float, default=.7,
                         help='dropout rate')
network_arg.add_argument('--use_leaky_relu', type=bool, default=False)
network_arg.add_argument('--act_threshold', type=float, default=1e-6,
                         help='used at ThresholdReLU')
network_arg.add_argument('--use_multi_channel', type=bool, default=False)
network_arg.add_argument('--use_se_module', type=bool, default=True)
network_arg.add_argument('--se_ratio', type=int, default=16)

# DataSet
data_arg = add_arg_group('DataSet')
data_arg.add_argument('--embed_size', type=int, default=384,  # 300
                      help='the size of Doc2Vec embedding vector')
data_arg.add_argument('--vocab_size', type=int, default=391587, help='default is w2v vocab size')
data_arg.add_argument('--character_size', type=int, default=251, help='number of korean chars')
data_arg.add_argument('--sequence_length', type=int, default=400,
                      help='the length of the sentence, default is c2v max words cnt')
# For Word2Vec, sequence_length should be 140
# Fro Char2Vec, sequence_length should be 400
data_arg.add_argument('--batch_size', type=int, default=128)
data_arg.add_argument('--n_threads', type=int, default=8,
                      help='the number of workers for speeding up')

# Train/Test hyper-parameters
train_arg = add_arg_group('Training')
train_arg.add_argument('--is_train', type=bool, default=True)
train_arg.add_argument('--epochs', type=int, default=100)
train_arg.add_argument('--logging_step', type=int, default=500)
train_arg.add_argument('--optimizer', type=str, default='adam', choices=['adam', 'sgd', 'adadelta'])
train_arg.add_argument('--grad_clip', type=float, default=5.)
train_arg.add_argument('--lr', type=float, default=2e-4)
train_arg.add_argument('--lr_decay', type=float, default=.95)
train_arg.add_argument('--lr_lower_boundary', type=float, default=2e-5)
train_arg.add_argument('--test_size', type=float, default=.2)

# Korean words Pre-Processing
nlp_model = add_arg_group('NLP')
nlp_model.add_argument('--analyzer', type=str, default='mecab', choices=['mecab', 'hannanum', 'twitter'],
                       help='korean pos analyzer')
nlp_model.add_argument('--use_correct_spacing', type=bool, default=False,
                       help='resolving sentence spacing problem but taking lots of time...')
nlp_model.add_argument('--use_normalize', type=bool, default=True)
nlp_model.add_argument('--vec_lr', type=float, default=2.5e-2)
nlp_model.add_argument('--vec_min_lr', type=float, default=2.5e-2)
nlp_model.add_argument('--vec_lr_decay', type=float, default=2e-3)

# Misc
misc_arg = add_arg_group('Misc')
misc_arg.add_argument('--device', type=str, default='gpu')
misc_arg.add_argument('--query_path', type=str, default='./comments/')
misc_arg.add_argument('--dataset', type=str, default='data.csv')
misc_arg.add_argument('--processed_dataset', type=str, default='tagged_data.csv',
                      help='already processed data file')
misc_arg.add_argument('--pretrained', type=str, default='./ml_model/')
misc_arg.add_argument('--w2v_model', type=str, default='./w2v/ko_w2v.model')
misc_arg.add_argument('--d2v_model', type=str, default='./w2v/ko_d2v.model')
misc_arg.add_argument('--seed', type=int, default=1337)
misc_arg.add_argument('--jvm_path', type=str, default="C:\\Program Files\\Java\\jre-9\\bin\\server\\jvm.dll")
misc_arg.add_argument('--verbose', type=bool, default=True)

# DB
db_arg = add_arg_group('DB')
db_arg.add_argument('--host', type=str, default='localhost')
db_arg.add_argument('--user', type=str, default='root')
db_arg.add_argument('--password', type=str, default='1111')
db_arg.add_argument('--db', type=str, default='movie')
db_arg.add_argument('--charset', type=str, default='utf8')
