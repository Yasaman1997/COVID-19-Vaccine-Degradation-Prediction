import random, os
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt

    
    
token2int = {x:i for i, x in enumerate('().ACGUBEHIMSX')}
token2int_seq = {x:i for i, x in enumerate('ACGU')}
token2int_struct = {x:i for i, x in enumerate('().')}
token2int_loop = {x:i for i, x in enumerate('BEHIMSX')}


def seed_everything(seed=0):
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    os.environ['TF_DETERMINISTIC_OPS'] = '1'

    
def plot_metrics(history):
    metric_list = [m for m in list(history.keys()) if m is not 'lr']
    size = len(metric_list)//2
    fig, axes = plt.subplots(size, 1, sharex='col', figsize=(20, size * 5))
    if size > 1:
        axes = axes.flatten()
    else:
        axes = [axes]
    
    for index in range(len(metric_list)//2):
        metric_name = metric_list[index]
        val_metric_name = metric_list[index+size]
        axes[index].plot(history[metric_name], label='Train %s' % metric_name)
        axes[index].plot(history[val_metric_name], label='Validation %s' % metric_name)
        axes[index].legend(loc='best', fontsize=16)
        axes[index].set_title(metric_name)
        axes[index].axvline(np.argmin(history[metric_name]), linestyle='dashed')
        axes[index].axvline(np.argmin(history[val_metric_name]), linestyle='dashed', color='orange')

    plt.xlabel('Epochs', fontsize=16)
    sns.despine()
    plt.show()
    
    
def plot_metrics_agg(history_list):
    metric_list = [m for m in list(history_list[0].keys()) if m is not 'lr']
    size = len(metric_list)//2
    fig, axes = plt.subplots(size, 1, sharex='col', figsize=(20, size * 6))
    if size > 1:
        axes = axes.flatten()
    else:
        axes = [axes]
    
    for idx, history in enumerate(history_list):
        for index in range(len(metric_list)//2):
            metric_name = metric_list[index]
            val_metric_name = metric_list[index+size]
            axes[index].plot(history[metric_name], label=f'Train {metric_name}_Fold{idx+1}')
            axes[index].plot(history[val_metric_name], label=f'Valid {metric_name}_Fold{idx+1}')
            axes[index].legend(loc='best', fontsize=16)
            axes[index].set_title(metric_name)
            axes[index].axvline(np.argmin(history[metric_name]), linestyle='dashed')
            axes[index].axvline(np.argmin(history[val_metric_name]), linestyle='dashed', color='orange')

    plt.xlabel('Epochs', fontsize=16)
    sns.despine()
    plt.show()

    
def preprocess_inputs(df, encoder, cols=['sequence', 'structure', 'predicted_loop_type']):
    if encoder:
        input_lists = df[cols].applymap(lambda seq: [encoder[x] for x in seq]).values.tolist()
    else:
        input_lists = df[cols].values.tolist()
    return np.transpose(np.array(input_lists), (0, 2, 1))


def add_bpps_features(df, database_base_path):
    bpps_nb_mean = 0.077522 # mean of bpps_nb across all training data
    bpps_nb_std = 0.08914   # std of bpps_nb across all training data
    bpps_max = []
    bpps_sum = []
    bpps_scaled = []
    for row in df.itertuples():
        probability = np.load(f'{database_base_path}/bpps/{row.id}.npy')
        bpps_max.append(probability.max(-1).tolist())
        bpps_sum.append((1-probability.sum(-1)).tolist())
        # bpps nb
        bpps_nb = (probability > 0).sum(axis=0) / probability.shape[0]
        bpps_nb = (bpps_nb - bpps_nb_mean) / bpps_nb_std
        bpps_scaled.append(bpps_nb)
        
    return df.assign(bpps_max=bpps_max, bpps_sum=bpps_sum, bpps_scaled=bpps_scaled)


def get_metrics(idxs, y_true, y_pred, target_cols, use_cols):
    metrics = []
    for idx, col in enumerate(target_cols):
        if col in use_cols:
            metrics.append(np.sqrt(np.mean((y_true[idxs, :, idx] - y_pred[idxs, :, idx])**2)))

    return [np.mean(metrics)] + metrics

def evaluate_model(df, y_true, y_pred, target_cols=['reactivity', 'deg_Mg_pH10', 'deg_pH10', 'deg_Mg_50C', 'deg_50C'], use_cols=None):
    if use_cols is None:
        use_cols = target_cols
        
    col_names = use_cols
        
    # SN_filter = 1
    metrics_clean_sn = get_metrics(df[df['SN_filter'] == 1].index, y_true, y_pred, target_cols, use_cols)
    
    # SN_filter = 0
    metrics_noisy_sn = get_metrics(df[df['SN_filter'] == 0].index, y_true, y_pred, target_cols, use_cols)
    
    # signal_to_noise > 1
    metrics_clean_sig = get_metrics(df[df['signal_to_noise'] > 1].index, y_true, y_pred, target_cols, use_cols)
    
    # signal_to_noise <= 1
    metrics_noisy_sig = get_metrics(df[df['signal_to_noise'] <= 1].index, y_true, y_pred, target_cols, use_cols)
    
    # Overall
    metrics = get_metrics(df.index, y_true, y_pred, target_cols, use_cols)
    col_names = ['Overall'] + col_names
    
    metrics_df = pd.DataFrame({'Metric/MCRMSE': col_names, 'Complete': metrics, 'Clean (SN)': metrics_clean_sn, 
                               'Noisy (SN)': metrics_noisy_sn, 'Clean (signal)': metrics_clean_sig, 
                               'Noisy (signal)': metrics_noisy_sig})
    return metrics_df

def get_features_dict(df, cols, encoders, idxs):
    features_dict = {}
    for idx, col in enumerate(cols):
        features_dict[col] = preprocess_inputs(df.loc[idxs], encoders[idx], [col])
    
    return features_dict

def get_targets_dict(df, cols, idxs):
    targets_dict = {}
    for col in cols:
        targets_dict[col] = np.array(df.loc[idxs][[col]].values.tolist()).transpose((0, 2, 1))
    
    return targets_dict

def MCRMSE(y_true, y_pred):
    colwise_mse = tf.reduce_mean(tf.square(y_true - y_pred), axis=1)
    return tf.reduce_mean(tf.sqrt(colwise_mse), axis=1)