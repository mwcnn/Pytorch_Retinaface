# config.py

cfg_mnet = {
    'name': 'mobilenet0.25',
    'min_sizes': [[16, 32], [64, 128], [256, 512]],
    'steps': [8, 16, 32],
    'variance': [0.1, 0.2],
    'clip': False,
    'loc_weight': 2.0,
    'gpu_train': True,
    'batch_size': 8, #default = 32
    'ngpu': 1, #default = 1
    'epoch': 1, #default = 250
    'decay1': 190,
    'decay2': 220,
    'image_size': 640,
    'pretrain': True,
    'return_layers': {'stage1': 1, 'stage2': 2, 'stage3': 3},
    'in_channel': 32,
    'out_channel': 64,
    'defian_layer': True,
    'bifpn': False
}

cfg_re50 = {
    'name': 'Resnet50',
    'min_sizes': [[16, 32], [64, 128], [256, 512]],
    'steps': [8, 16, 32],
    'variance': [0.1, 0.2],
    'clip': False,
    'loc_weight': 2.0,
    'gpu_train': True,
    'batch_size': 8, #default = 24
    'ngpu': 1, #default = 4
    'epoch': 1, #default = 100
    'decay1': 70,
    'decay2': 90,
    'image_size': 840,
    'pretrain': True,
    'return_layers': {'layer2': 1, 'layer3': 2, 'layer4': 3},
    'in_channel': 256,
    'out_channel': 256,
    'defian_layer': True,
    'bifpn': False
}

cfg_gnet = {
    'name': 'ghostnet',
    'min_sizes': [[16, 32], [64, 128], [256, 512]],
    'steps': [8, 16, 32],
    'variance': [0.1, 0.2],
    'clip': True,
    'loc_weight': 2.0,
    'gpu_train': True,
    'batch_size': 16,
    'ngpu': 1,
    'epoch': 100,
    'decay1': 190,
    'decay2': 220,
    'image_size': 640,
    'pretrain': False,
    'return_layers': {'blocks1': 1, 'blocks2': 2, 'blocks3': 3},
    # 'return_layers': {'stage1': 1, 'stage2': 2, 'stage3': 3},
    'in_channel': 32,
    'out_channel': 64,
    'defian_layer': True,
    'bifpn': False
}

cfg_mnetv3 = {
    'name': 'mobilev3',
    'min_sizes': [[16, 32], [64, 128], [256, 512]],
    'steps': [8, 16, 32],
    'variance': [0.1, 0.2],
    'clip': True,
    'loc_weight': 2.0,
    'gpu_train': True,
    'batch_size': 16,
    'ngpu': 1,
    'epoch': 350,
    'decay1': 190,
    'decay2': 220,
    'image_size': 680,
    'pretrain': False,
    'return_layers': {'bneck1': 1, 'bneck2': 2, 'bneck3': 3},
    'in_channel': 32,
    'out_channel': 64,
    'defian_layer': True,
    'bifpn': False
}