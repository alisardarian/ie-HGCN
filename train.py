import random
import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim
from sklearn.metrics import f1_score, average_precision_score, roc_auc_score

# import warnings
# import sklearn.exceptions
# warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)

from util import *
from model import HGCN


cuda = True # Enables CUDA training.
fastmode = True # Validate during training pass.
seed = 87 # Random seed.
epochs = 2000 # Number of epochs to train.P
lr = 0.01 # Initial learning rate.
weight_decay = 5e-4 # Weight decay (L2 loss on parameters).



# np.random.seed(seed)
# torch.manual_seed(sumeed)
# if cuda and torch.cuda.is_available():
#     torch.cuda.manual_seed(seed)



def train(epoch):

	model.train()
	optimizer.zero_grad()
	output = model(ft_dict, adj_dict)



	# m_logits = torch.sigmoid(output['m'])
	
	# # class_weight = (label['m'][0].sum().type_as(m_logits)) / (label['m'][0].sum(0).type_as(m_logits))
	# # class_weight = (label['m'][0].sum(0).type_as(m_logits)) / (label['m'][0].sum().type_as(m_logits))

	# # label_1_sum = label['m'][0].sum(0)
	# # label_0_sum = label['m'][0].shape[0] - label_1_sum
	# # label_1_weight = label_0_sum.type_as(m_logits) / label['m'][0].shape[0]
	# # label_0_weight = label_1_sum.type_as(m_logits) / label['m'][0].shape[0]


	# idx_train = label['m'][1]
	# x_train = m_logits[idx_train]
	# y_train = label['m'][0][idx_train].type_as(x_train)

	# # weight_train = y_train.type_as(label_1_weight) * label_1_weight + (1-y_train).type_as(label_0_weight) * label_0_weight
	# # loss_train_elem = F.binary_cross_entropy(x_train, y_train, reduction='none')
	# # loss_train = torch.mul(loss_train_elem, weight_train).sum()

	# # loss_train = F.binary_cross_entropy(x_train, y_train, reduction='none', weight=class_weight).mean(0).sum()
	
	# loss_train = F.binary_cross_entropy(x_train, y_train, reduction='none').mean(0).sum()

	# # micro_f1_train = f1_score(y_train.data.cpu(), (x_train.round().type_as(torch.IntTensor())).data.cpu(), average='micro')
	# # macro_f1_train = f1_score(y_train.data.cpu(), (x_train.round().type_as(torch.IntTensor())).data.cpu(), average='macro')
	# roc_train = roc_auc_score(y_train.data.cpu(), x_train.data.cpu())
	# ap_train = average_precision_score(y_train.data.cpu(), x_train.data.cpu())



	# p_logits = F.log_softmax(output['p'], dim=1)
	a_logits = F.log_softmax(output['a'], dim=1)
	# c_logits = F.log_softmax(output['c'], dim=1)

	# idx_train_p = label['p'][1]
	# x_train_p = p_logits[idx_train_p]
	# y_train_p = label['p'][0][idx_train_p]
	# loss_train_p = F.nll_loss(x_train_p, y_train_p)
	# acc_train_p = accuracy(x_train_p, y_train_p)

	idx_train_a = label['a'][1]
	x_train_a = a_logits[idx_train_a]
	y_train_a = label['a'][0][idx_train_a]
	# loss_train_a = F.nll_loss(x_train_a, y_train_a)
	loss_train = F.nll_loss(x_train_a, y_train_a)
	acc_train_a = accuracy(x_train_a, y_train_a)

	# idx_train_c = label['c'][1]
	# x_train_c = c_logits[idx_train_c]
	# y_train_c = label['c'][0][idx_train_c]
	# loss_train_c = F.nll_loss(x_train_c, y_train_c)
	# acc_train_c = accuracy(x_train_c, y_train_c)
	
	# loss_train = 0.03*loss_train_p + 0.965*loss_train_a + 0.005*loss_train_c



	loss_train.backward()
	optimizer.step()



	if not fastmode:
		model.eval()
		output = model(ft_dict, adj_dict)


	# idx_val = label['m'][2]
	# x_val = m_logits[idx_val]
	# y_val = label['m'][0][idx_val].type_as(x_val)
	
	# # weight_val = y_val.type_as(label_1_weight) * label_1_weight + (1-y_val).type_as(label_0_weight) * label_0_weight
	# # loss_val_elem = F.binary_cross_entropy(x_val, y_val, reduction='none')
	# # loss_val = torch.mul(loss_val_elem, weight_val).sum()

	# # loss_val = F.binary_cross_entropy(x_val, y_val, reduction='none', weight=class_weight).mean(0).sum()
	
	# loss_val = F.binary_cross_entropy(x_val, y_val, reduction='none').mean(0).sum()
	

	# # micro_f1_val = f1_score(y_val.data.cpu(), (x_val.round().type_as(torch.IntTensor())).data.cpu(), average='micro')
	# # macro_f1_val = f1_score(y_val.data.cpu(), (x_val.round().type_as(torch.IntTensor())).data.cpu(), average='macro')
	# roc_val = roc_auc_score(y_val.data.cpu(), x_val.data.cpu())
	# ap_val = average_precision_score(y_val.data.cpu(), x_val.data.cpu())



	# idx_val_p = label['p'][2]
	# x_val_p = p_logits[idx_val_p]
	# y_val_p = label['p'][0][idx_val_p]
	# loss_val_p = F.nll_loss(x_val_p, y_val_p)
	# acc_val_p = accuracy(x_val_p, y_val_p)

	idx_val_a = label['a'][2]
	x_val_a = a_logits[idx_val_a]
	y_val_a = label['a'][0][idx_val_a]
	# loss_val_a = F.nll_loss(x_val_a, y_val_a)
	loss_val = F.nll_loss(x_val_a, y_val_a)
	acc_val_a = accuracy(x_val_a, y_val_a)

	# idx_val_c = label['c'][2]
	# x_val_c = c_logits[idx_val_c]
	# y_val_c = label['c'][0][idx_val_c]
	# loss_val_c = F.nll_loss(x_val_c, y_val_c)
	# acc_val_c = accuracy(x_val_c, y_val_c)
	
	# loss_val = 0.03*loss_val_p + 0.965*loss_val_a + 0.005*loss_val_c



	# print(
	# 	  'epoch: {:3d}'.format(epoch),
	# 	  'train loss: {:.4f}'.format(loss_train.item()),
	# 	  'train roc: {:.4f}'.format(roc_train),
	# 	  'train ap: {:.4f}'.format(ap_train),
	# 	  # 'train micro f1: {:.4f}'.format(micro_f1_train),
	# 	  # 'train macro f1: {:.4f}'.format(macro_f1_train),
	# 	  'val loss: {:.4f}'.format(loss_val.item()),
	# 	  'val roc: {:.4f}'.format(roc_val),
	# 	  'val ap: {:.4f}'.format(ap_val),
	# 	  # 'val micro f1: {:.4f}'.format(micro_f1_val),
	# 	  # 'val macro f1: {:.4f}'.format(macro_f1_val),
	# 	 )


	print(
		  'epoch: {:3d}'.format(epoch),
		  'train loss: {:.4f}'.format(loss_train.item()),
		  # 'train acc p: {:.4f}'.format(acc_train_p.item()),
		  'train acc a: {:.4f}'.format(acc_train_a.item()),
		  # 'train acc c: {:.4f}'.format(acc_train_c.item()),
		  'val loss: {:.4f}'.format(loss_val.item()),
		  # 'val acc p: {:.4f}'.format(acc_val_p.item()),
		  'val acc a: {:.4f}'.format(acc_val_a.item()),
		  # 'val acc c: {:.4f}'.format(acc_val_c.item()),
		 )



def test():
	model.eval()
	output = model(ft_dict, adj_dict)



	# idx_test = label['m'][3]
	# x_test = torch.sigmoid(output['m'])[idx_test]
	# y_test = label['m'][0][idx_test].type_as(x_test)
	# # micro_f1_test = f1_score(y_test.data.cpu(), (x_test.round().type_as(torch.IntTensor())).data.cpu(), average='micro')
	# # macro_f1_test = f1_score(y_test.data.cpu(), (x_test.round().type_as(torch.IntTensor())).data.cpu(), average='macro')
	# roc_test = roc_auc_score(y_test.data.cpu(), x_test.data.cpu())
	# ap_test = average_precision_score(y_test.data.cpu(), x_test.data.cpu())



	# idx_test_p = label['p'][3]
	# x_test_p = F.log_softmax(output['p'], dim=1)[idx_test_p]
	# y_test_p = label['p'][0][idx_test_p]
	# acc_test_p = accuracy(x_test_p, y_test_p)

	idx_test_a = label['a'][3]
	x_test_a = F.log_softmax(output['a'], dim=1)[idx_test_a]
	y_test_a = label['a'][0][idx_test_a]
	acc_test_a = accuracy(x_test_a, y_test_a)

	# idx_test_c = label['c'][3]
	# x_test_c = F.log_softmax(output['c'], dim=1)[idx_test_c]
	# y_test_c = label['c'][0][idx_test_c]
	# acc_test_c = accuracy(x_test_c, y_test_c)
	


	# print('\n'
	# 	  'test roc: {:.4f}'.format(roc_test),
	# 	  'test ap: {:.4f}'.format(ap_test),
	# 	  # 'test micro f1: {:.4f}'.format(micro_f1_test),
	# 	  # 'test macro f1: {:.4f}'.format(macro_f1_test),
	# 	 )


	
	print('\n'
		  # 'test acc p: {:.4f}'.format(acc_test_p.item()),
		  'test acc a: {:.4f}'.format(acc_test_a.item()),
		  # 'test acc c: {:.4f}'.format(acc_test_c.item())
		 )


if __name__ == '__main__':
	


	runs = 1
	for r in range(runs):


		# eq_hidden = [32]  # imdb128
		# label, ft_dict, adj_dict  = load_imdb128()
		# output_layer_shape = dict.fromkeys(ft_dict.keys(), 17)


		# eq_hidden = [128,64,32]  # imdb10197
		# eq_hidden = [64]
		# label, ft_dict, adj_dict = load_imdb10197()
		# output_layer_shape = dict.fromkeys(ft_dict.keys(), 19)


		# eq_hidden = [64,32,16]  # dblp4area
		# eq_hidden = [64]
		# label, ft_dict, adj_dict = load_dblp4area()
		# output_layer_shape = dict.fromkeys(ft_dict.keys(), 4)


		eq_hidden = [64,32,16]
		# eq_hidden = [128,128,64]
		# eq_hidden = [128,128,128]
		# eq_hidden = [64,32]
		# eq_hidden = [64]
		label, ft_dict, adj_dict = load_dbis()
		output_layer_shape = dict.fromkeys(ft_dict.keys(), 8)


		layer_shape = []
		input_layer_shape = dict([(k, ft_dict[k].shape[1]) for k in ft_dict.keys()])
		layer_shape.append(input_layer_shape)
		hidden_layer_shape = [dict.fromkeys(ft_dict.keys(), l_hid) for l_hid in eq_hidden]
		layer_shape.extend(hidden_layer_shape)
		layer_shape.append(output_layer_shape)


		# Model and optimizer
		net_schema = dict([(k, list(adj_dict[k].keys())) for k in adj_dict.keys()])
		model = HGCN(net_schema=net_schema, layer_shape=layer_shape, label_keys=list(label.keys()))
		optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)


		if cuda and torch.cuda.is_available():
			model.cuda()

			for k in ft_dict:
				ft_dict[k] = ft_dict[k].cuda()
			for k in adj_dict:
				for kk in adj_dict[k]:
					adj_dict[k][kk] = adj_dict[k][kk].cuda()
			for k in label:
				for i in range(len(label[k])):
					label[k][i] = label[k][i].cuda()



		print('run: {:d}\n'.format(r))
		for epoch in range(epochs):
			train(epoch)
		train(epoch)
		test()

		del model