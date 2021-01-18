def hist_func_mplot(data_set):
    import matplotlib.pyplot as plt
    plt.hist(data_set, )

def categorical_columns(x_data, data_set):
    import seaborn as sns
    sns.countplot(x=x_data, data=data_set)

def catplot_multicolumn(data_set, x_data, y_data, hue="class", kind="bar"):
    import seaborn as sns
    data_sns= sns.load_dataset(data_set)
    sns.catplot(x=x_data, y=y_data, hue="class", kind="bar", data=data_sns)
    