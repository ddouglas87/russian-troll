from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import logging

def get_model_eval(path):
    with open(Path(path)/'eval_results.txt', encoding='utf-8') as fi:
        accuracy = []
        loss = []
        step = []
        
        eval_accuracy = None
        eval_loss = None
        global_step = None
        for line in fi:
            if line.startswith('eval_accuracy'):
                eval_accuracy = float(line[16:-1])
            elif line.startswith('eval_loss'):
                eval_loss = float(line[12:-1])
            elif line.startswith('global_step'):
                global_step = int(line[14:-1])
            elif line == '==================================================\n':
                if eval_accuracy and eval_loss:
                    accuracy.append(eval_accuracy)
                    loss.append(eval_loss)
                    step.append(global_step)
                eval_accuracy = None
                eval_loss = None
                global_step = None
    
    return pd.DataFrame({'step': step, 'accuracy': accuracy,'loss': loss})

def draw_plot_annotations(plot, df, column):
    # Inspired by https://stackoverflow.com/questions/24108063/matplotlib-two-different-colors-in-the-same-annotate
    min = df[column].min()
    last = df[column][len(df)-1]
    max = df[column].max()
    min_loc = df[df[column] == df[column].min()]['step'].values[0] / df['step'][len(df)-1]
    max_loc = df[df[column] == df[column].max()]['step'].values[0] / df['step'][len(df)-1]
    ylim = plot.axes.get_ylim()
    
    plot.annotate('{:.0%}'.format(last), xy=(1, last), xytext=(4, -2), 
                  xycoords=('axes fraction', 'data'), textcoords='offset points')
    
    if min_loc > 0 and min_loc < 1 and ylim[0]+0.1 < min:
        plot.annotate('{:.0%}'.format(min), xy=(min_loc, min+0.005), xytext=(0,-25), 
                      textcoords='offset points', ha='center', va='bottom', xycoords=('axes fraction', 'data'),
                      arrowprops=dict(arrowstyle='-', color='red'))
    if max_loc > 0  and max_loc < 1 and ylim[1]-0.1 > max:
        plot.annotate('{:.0%}'.format(max), xy=(max_loc, max-0.005), xytext=(0, 18),
                      textcoords='offset points', ha='center', va='bottom', xycoords=('axes fraction', 'data'),
                      arrowprops=dict(arrowstyle='-', color='red'))

def plot_model_eval(path, title=''):
    if title == '':
        title = path
    
    try:
        df = get_model_eval(path)
        last_step = df['step'][len(df)-1]

        fig, ax = plt.subplots()
        fig.set_figwidth(last_step/2000)
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
        plot = df.plot(x='step', title=title, ax=ax)
        draw_plot_annotations(plot, df, 'accuracy')
        draw_plot_annotations(plot, df, 'loss')

        plt.show()
    except:
        logging.warning("File {} not found.".format((Path(path)/'eval_results.txt').absolute()))